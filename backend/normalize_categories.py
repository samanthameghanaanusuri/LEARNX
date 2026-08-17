import json
from app import create_app
from app.models import db, Course

def normalize():
    app = create_app()
    with app.app_context():
        courses = Course.query.all()
        for c in courses:
            if c.id == 1: # Python
                c.category = 'Programming Languages, Programming'
            elif c.id == 2: # Java
                c.category = 'Programming Languages, Programming'
            elif c.id == 3: # HTML
                c.category = 'Web Development'
            elif c.id == 4: # CSS
                c.category = 'Web Development'
            elif c.id == 5: # JS
                c.category = 'Web Development, Programming Languages'
            elif c.id == 6: # C
                c.category = 'Programming Languages'
            elif c.id == 7: # C++
                c.category = 'Programming Languages, C++'
            elif c.id == 8: # Cyber Security
                c.category = 'Cyber Security'
            elif c.id == 9: # DBMS
                c.category = 'Database'
            elif c.id == 10: # DSA
                c.category = 'Data Structures, Programming'
        
        db.session.commit()
        print("Categories normalized successfully.")

if __name__ == '__main__':
    normalize()
