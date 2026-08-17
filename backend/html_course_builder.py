import json
import importlib

def build_html_course():
    course_data = {
        "title": "HTML & Web Development",
        "slug": "html-web-development",
        "description": "Master HTML from scratch. Learn semantic markup, forms, multimedia, and best practices to build modern web pages.",
        "subject": "HTML",
        "difficulty": "Beginner",
        "modules": []
    }

    # Load 10 modules
    for i in range(1, 11):
        mod_name = f"html_course_data.module_{i}"
        mod = importlib.import_module(mod_name)
        course_data["modules"].append(mod.get_module_data())

    return course_data

if __name__ == "__main__":
    course = build_html_course()
    with open("html_course_new.json", "w", encoding="utf-8") as f:
        json.dump(course, f, indent=4)
    print("Generated html_course_new.json")
