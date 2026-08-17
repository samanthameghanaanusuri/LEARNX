import sqlite3

def run():
    conn = sqlite3.connect('backend/instance/learnx.db')
    c = conn.cursor()
    queries = [
        'ALTER TABLE knowledge_state_history ADD COLUMN quiz_question_id INTEGER;',
        'ALTER TABLE knowledge_state_history ADD COLUMN exercise_id INTEGER;',
        'ALTER TABLE knowledge_state_history ADD COLUMN answer_correct BOOLEAN;',
        'ALTER TABLE knowledge_state_history ADD COLUMN evidence_score FLOAT;',
        'ALTER TABLE knowledge_state_history ADD COLUMN evidence_source VARCHAR(50);',
        'ALTER TABLE knowledge_state_history ADD COLUMN passed_tests INTEGER;',
        'ALTER TABLE knowledge_state_history ADD COLUMN total_tests INTEGER;'
    ]
    for q in queries:
        try:
            c.execute(q)
            print(f"Executed: {q}")
        except Exception as e:
            print(f"Skipped {q}: {e}")
    conn.commit()
    conn.close()

if __name__ == '__main__':
    run()
