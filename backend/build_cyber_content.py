import os
import glob

def build_content():
    output_file = "content_cyber.py"
    
    with open(output_file, "w", encoding="utf-8") as outfile:
        # Write course level data
        outfile.write('course_title = "Cyber Security — Beginner to Master"\n')
        outfile.write('course_description = "A comprehensive journey from basic computer networking to advanced penetration testing, digital forensics, and security architecture."\n')
        outfile.write('course_language = "text"\n')
        outfile.write('course_difficulty = "Beginner to Master"\n\n')
        
        # Write modules content
        for i in range(1, 11):
            filename = f"content_cyber_{i}.py"
            if os.path.exists(filename):
                with open(filename, "r", encoding="utf-8") as infile:
                    outfile.write(infile.read())
                    outfile.write("\n\n")
            else:
                print(f"Warning: {filename} not found.")
                
        # Write the list aggregators
        outfile.write("\n\n")
        outfile.write("cyber_lessons = [\n")
        for i in range(1, 21):
            outfile.write(f"    m{i}_lesson,\n")
        outfile.write("]\n\n")
        
        outfile.write("cyber_exercises_list = [\n")
        for i in range(1, 21):
            outfile.write(f"    m{i}_exercises,\n")
        outfile.write("]\n\n")
        
        outfile.write("cyber_quizzes_list = [\n")
        for i in range(1, 21):
            outfile.write(f"    m{i}_quizzes,\n")
        outfile.write("]\n\n")
        
        outfile.write("cyber_module_titles = [\n")
        outfile.write('    "Phase 1: What Cyber Security actually is",\n')
        outfile.write('    "Phase 1: Computer & OS fundamentals",\n')
        outfile.write('    "Phase 1: Networking fundamentals",\n')
        outfile.write('    "Phase 1: TCP/IP, ports, protocols",\n')
        outfile.write('    "Phase 1: Linux fundamentals",\n')
        outfile.write('    "Phase 1: Windows security fundamentals",\n')
        outfile.write('    "Phase 2: CIA Triad, threats, vulnerabilities & risk",\n')
        outfile.write('    "Phase 2: Authentication, authorization & cryptography",\n')
        outfile.write('    "Phase 2: Hashing, encryption, encoding & certificates",\n')
        outfile.write('    "Phase 2: Web security fundamentals",\n')
        outfile.write('    "Phase 2: OWASP Top 10",\n')
        outfile.write('    "Phase 2: Secure coding & input validation",\n')
        outfile.write('    "Phase 3: Reconnaissance & OSINT",\n')
        outfile.write('    "Phase 3: Scanning & enumeration",\n')
        outfile.write('    "Phase 3: Vulnerability assessment",\n')
        outfile.write('    "Phase 3: Web penetration-testing concepts",\n')
        outfile.write('    "Phase 3: Network security & packet analysis",\n')
        outfile.write('    "Phase 3: Malware concepts & defensive analysis",\n')
        outfile.write('    "Phase 4: Logging, monitoring, SIEM & incident response",\n')
        outfile.write('    "Phase 4: Digital forensics, threat hunting & security architecture",\n')
        outfile.write("]\n")

    print(f"Successfully generated {output_file}")

if __name__ == "__main__":
    build_content()
