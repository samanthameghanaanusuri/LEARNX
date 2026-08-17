from flask import current_app

class BayesianKnowledgeTracing:
    def __init__(self, p_init=None, p_learn=None, p_forget=None, p_guess=None, p_slip=None):
        self._default_params = {
            'p_init': 0.40,
            'p_learn': 0.10,
            'p_forget': 0.00,
            'p_guess': 0.20,
            'p_slip': 0.10
        }
        self.p_init = p_init
        self.p_learn = p_learn
        self.p_forget = p_forget
        self.p_guess = p_guess
        self.p_slip = p_slip

    def get_params(self):
        config_params = {}
        try:
            if current_app and 'BKT_PARAMS' in current_app.config:
                config_params = current_app.config['BKT_PARAMS']
        except RuntimeError:
            pass

        return {
            'p_init': self.p_init if self.p_init is not None else config_params.get('p_init', self._default_params['p_init']),
            'p_learn': self.p_learn if self.p_learn is not None else config_params.get('p_learn', self._default_params['p_learn']),
            'p_forget': self.p_forget if self.p_forget is not None else config_params.get('p_forget', self._default_params['p_forget']),
            'p_guess': self.p_guess if self.p_guess is not None else config_params.get('p_guess', self._default_params['p_guess']),
            'p_slip': self.p_slip if self.p_slip is not None else config_params.get('p_slip', self._default_params['p_slip']),
        }

    def map_score_to_evidence(self, score, evidence_source="coding_submission"):
        """
        Maps a raw score to a Bayesian evidence probability [0.0, 1.0].
        This avoids blindly treating a 2/5 coding score as a binary correct/incorrect.
        """
        if evidence_source in ["coding_submission", "project_submission"]:
            # For code and project submissions, use fractional score directly as evidence probability
            return float(score)
        else:
            # Default fallback for simple binary quizzes
            return 1.0 if score else 0.0

    def update_mastery(self, previous_mastery, evidence):
        """
        Updates the probability of mastery using the Bayesian Knowledge Tracing update equations:
        
        1. Posterior probability of knowing given the observation:
           - If correct:
             P(L_{t-1} | Correct) = (L_{t-1} * (1 - S)) / (L_{t-1} * (1 - S) + (1 - L_{t-1}) * G)
           - If incorrect:
             P(L_{t-1} | Incorrect) = (L_{t-1} * S) / (L_{t-1} * S + (1 - L_{t-1}) * (1 - G))
             
        2. Account for transition (learning) and forget parameters:
           L_t = P(L_{t-1} | Obs) * (1 - F) + (1 - P(L_{t-1} | Obs)) * T
        """
        params = self.get_params()
        p_learn = params['p_learn']
        p_forget = params['p_forget']
        p_guess = params['p_guess']
        p_slip = params['p_slip']

        p_known = previous_mastery

        # Probability given a positive (correct) observation
        p_obs_correct = p_known * (1 - p_slip) + (1 - p_known) * p_guess
        p_post_correct = (p_known * (1 - p_slip)) / p_obs_correct if p_obs_correct > 1e-9 else 0.0

        # Probability given a negative (incorrect) observation
        p_obs_incorrect = p_known * p_slip + (1 - p_known) * (1 - p_guess)
        p_post_incorrect = (p_known * p_slip) / p_obs_incorrect if p_obs_incorrect > 1e-9 else 0.0

        # Interpolate based on continuous evidence (e.g., partial score like 0.6)
        p_post = (evidence * p_post_correct) + ((1.0 - evidence) * p_post_incorrect)

        updated_mastery = p_post * (1 - p_forget) + (1 - p_post) * p_learn
        updated_mastery = max(0.0, min(1.0, updated_mastery))
        
        return updated_mastery
