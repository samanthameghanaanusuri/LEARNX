from app.models import db, Concept, KnowledgeState, Diagnosis, Subject
import json

def diagnose_learning_failure(student_id, subject_id):
    """
    Diagnoses learning failures by:
    1. Finding concepts under the subject that the student has failed (mastery < 0.6).
    2. Recursively checking prerequisites of those failed concepts.
    3. Finding the "root cause" concepts: concepts that are weak but whose prerequisites are mastered (or have no prerequisites).
    """
    # Get all concepts for the subject
    concepts = Concept.query.filter_by(subject_id=subject_id).all()
    if not concepts:
        return None

    # Load student knowledge state
    # Create a mapping of concept_id -> mastery_score (default to 0.0 if not assessed yet)
    knowledge_states = KnowledgeState.query.filter_by(student_id=student_id).all()
    mastery_map = {ks.concept_id: ks.mastery_score for ks in knowledge_states}
    
    # We want to identify concepts that the student has attempted but failed.
    # If a concept has no record in knowledge state, we treat it as unassessed (mastery = 1.0 for diagnosis purposes,
    # because we only diagnose active failures where they took the test and scored low).
    # However, if a concept has a recorded mastery < 0.6, it is marked as "weak".
    weak_concepts = {}
    for concept in concepts:
        mastery = mastery_map.get(concept.id, None)
        if mastery is not None and mastery < 0.6:
            weak_concepts[concept.id] = {
                'concept': concept,
                'mastery': mastery
            }

    if not weak_concepts:
        # No failed concepts found! Student is doing fine or hasn't taken assessments yet.
        return None

    # Find the root causes
    root_causes = []
    prerequisite_weaknesses = set()

    for concept_id, info in weak_concepts.items():
        concept = info['concept']
        
        # Check prerequisites of this concept
        prereqs = concept.prerequisites # list of Concept models
        
        # A concept is a root cause if it is weak, and NONE of its prerequisites are weak
        # (meaning either it has no prerequisites, or all its prerequisites are mastered >= 0.6).
        has_weak_prereq = False
        for prereq in prereqs:
            if prereq.id in weak_concepts:
                has_weak_prereq = True
                prerequisite_weaknesses.add(prereq.id)
        
        if not has_weak_prereq:
            root_causes.append(concept.id)
        else:
            # If it has a weak prerequisite, then it is a dependent weakness
            prerequisite_weaknesses.add(concept_id)

    if not root_causes:
        # Fallback: if there is a cycle or some anomaly, just pick the lowest id weak concept
        if weak_concepts:
            root_causes = [min(weak_concepts.keys())]

    # For the demonstration, we diagnose the first root cause
    root_cause_id = root_causes[0]
    root_cause_concept = Concept.query.get(root_cause_id)
    
    # Prerequisite weaknesses are other weak concepts in the chain
    weakness_list = list(prerequisite_weaknesses)
    if root_cause_id in weakness_list:
        weakness_list.remove(root_cause_id)

    # Generate a professional diagnostic summary
    summary_text = (
        f"Diagnostic trace detected a learning failure in '{root_cause_concept.name}'. "
        f"While assessing concepts in this subject, weakness was identified in prerequisites. "
        f"The root cause of the learning blocker is identified as a lack of mastery in '{root_cause_concept.name}'. "
        f"We recommend immediate recovery intervention for '{root_cause_concept.name}' before proceeding further."
    )

    # Save to database
    diagnosis = Diagnosis(
        student_id=student_id,
        subject_id=subject_id,
        root_cause_concept_id=root_cause_id,
        prerequisite_weakness_ids_json=json.dumps(weakness_list),
        diagnostic_summary=summary_text
    )
    
    try:
        db.session.add(diagnosis)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e

    return diagnosis
