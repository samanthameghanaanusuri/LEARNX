course_title = "Cyber Security — Beginner to Master"
course_description = "A comprehensive journey from basic computer networking to advanced penetration testing, digital forensics, and security architecture."
course_language = "text"
course_difficulty = "Beginner to Master"

m1_lesson = """# What Cyber Security Actually Is

## 1. What Is It?

Cyber security is the ongoing process of protecting digital systems, networks, and data from unauthorized access, damage, or theft. It is not a single product you can buy, nor is it a final state you can achieve. It is a continuous practice of risk management.

At the most fundamental level, cyber security is about ensuring that systems behave exactly as they are designed to behave—even when someone is actively trying to force them to do otherwise. It bridges the gap between how a system *should* function and how an attacker *can* make it function.

## 2. Why Do We Need It?

We need cyber security because modern society is completely dependent on digital infrastructure. When that infrastructure fails, the consequences are immediate and severe in the physical world.

**Example 1: Financial Trust**
When you use a banking app, you trust that your $100 transfer goes to your friend and not to an attacker, and that your account balance remains accurate. Without cyber security, digital banking would be impossible because the underlying trust would collapse.

**Example 2: Critical Infrastructure**
Power grids, water purification plants, and hospitals rely on computer systems to operate. If an attacker breaches a hospital network and deploys ransomware (locking the computers), doctors cannot access patient medical records or operate life-saving equipment, directly risking lives.

## 3. Where Is It Used?

- **Everyday Life**: Securing your personal email, social media, and banking applications on your smartphone.
- **Enterprise Businesses**: Protecting customer databases, trade secrets, and employee payroll systems.
- **Governments & Military**: Defending national security intelligence, voter databases, and weapons systems.
- **Industrial Control Systems**: Protecting the physical machinery in factories and power plants.

## 4. How Does It Work?

Cyber security works by identifying what needs to be protected, identifying what could harm it, and placing defensive controls in between.

1. **Identify the Asset**: Determine what data or system is valuable.
2. **Identify the Threat**: Determine who or what might attack the asset (e.g., hackers, malware, insider threats).
3. **Identify the Vulnerability**: Find the weaknesses in the system that the threat could exploit.
4. **Implement Controls**: Deploy defenses (like firewalls, passwords, or encryption) to reduce the risk.
5. **Monitor and Respond**: Continuously watch the system for signs of an attack and react immediately if one occurs.

## 5. Important Terminology

| Term | Meaning |
|------|---------|
| **Asset** | Something of value that needs to be protected (e.g., a database, a laptop, a reputation). |
| **Threat** | Anything capable of causing harm to an asset (e.g., a cybercriminal, a hurricane). |
| **Vulnerability** | A weakness or flaw in a system that a threat can exploit. |
| **Exploit** | A specific technique or tool used by a threat to take advantage of a vulnerability. |
| **Risk** | The likelihood of a threat exploiting a vulnerability and the resulting impact. |

## 6. Architecture / Diagram

```text
The Core Equation of Security

[ Threat ] + [ Vulnerability ] = [ Risk ]
   |                |               |
(Attacker)   (Weak Password)   (Data Stolen)

Mitigation (How we fix it):
[ Threat ] + [ Mitigated Vuln ] = [ Reduced Risk ]
   |                |               |
(Attacker)  (Strong Password + MFA) (Data Safe)
```

## 7. Syntax / Commands / Configuration

In the context of understanding what cyber security is, our "configuration" is setting a security policy. A core concept is the **Principle of Least Privilege**, which means giving a user or program only the absolute minimum access necessary.

```text
# Bad Security Policy
User: Alice
Access: ALL SYSTEMS (Database, HR, Finance)

# Good Security Policy (Least Privilege)
User: Alice (Role: Marketing)
Access: Marketing Shared Drive
Block: Database, HR, Finance
```

## 8. Beginner Example

Imagine your physical house.
- The **Asset** is your expensive television.
- The **Vulnerability** is a window that doesn't lock properly.
- The **Threat** is a burglar roaming your neighborhood.
- The **Risk** is high because the burglar can easily open the broken window and steal the TV.
- The **Security Control** is fixing the lock on the window or installing a security alarm. By doing this, you eliminate the vulnerability, thus reducing the risk.

## 9. Real-World Example

**Situation**: A small business uses a simple website to sell products.
**Weakness (Vulnerability)**: The website owner uses the password "password123" for the administrator account.
**Threat**: An automated bot on the internet scanning for websites with weak passwords.
**Risk**: The bot guesses the password, logs in, and steals the credit card information of all customers.
**Detection**: The business owner notices strange charges on their own test credit card, or customers start complaining about fraud.
**Mitigation**: The owner changes the password to a complex passphrase and enables Two-Factor Authentication (2FA).

## 10. What Happens Internally?

Internally, a computer system has no concept of "good" or "bad." A computer blindly executes the instructions it is given. 

If an attacker logs in with a stolen, valid password, the computer's internal logic says: "This person provided the correct password. Therefore, they are authorized to view this data." 

Cyber security is the process of adding logic to the computer so it can make better decisions. For example, adding logic that says: "Even if the password is correct, if this login attempt is coming from a country the user has never visited, block it and send an alert."

## 11. Common Mistakes

1. **Security as an Afterthought**: Building an application first and trying to "add security" later. Security must be built into the design from day one.
2. **Assuming "Nobody cares about my data"**: Attackers use automated tools to scan the entire internet. They will attack you simply because you are connected, not necessarily because they know who you are.
3. **Relying purely on technology**: Buying an expensive firewall but failing to train employees not to click on phishing emails.
4. **Confusing Compliance with Security**: Thinking that because your company passed a legal security audit, you are immune to hackers. Compliance is the minimum baseline; security is an active defense.

## 12. Defensive Best Practices

1. **Defense in Depth**: Implement multiple overlapping layers of security. If the firewall fails, the antivirus should catch the attack. If the antivirus fails, the data encryption should protect the files.
2. **Principle of Least Privilege**: Never give administrative rights to standard users. 
3. **Assume Breach**: Operate your network under the assumption that an attacker has already bypassed your outer defenses. This forces you to focus on internal monitoring and rapid response.
4. **Keep Systems Updated**: Apply software patches immediately. Most devastating hacks exploit vulnerabilities that were fixed by the vendor months or years ago.

## 13. Security Mindset

A security professional does not look at a system and ask, "How does this work?" They ask:
- *How can I break this?*
- *What is the developer assuming I will do, and what happens if I do the exact opposite?*
- *If I am the attacker, what is the easiest path to the most valuable data?*
- *If a breach happens right now, how long would it take us to notice?*

## 14. Try It Yourself

Perform a personal threat modeling exercise. 
1. Identify your most critical digital asset (e.g., your primary email account).
2. Identify the biggest threat to it (e.g., someone stealing your password).
3. Implement one new security control today to protect it (e.g., go into the settings of your email account and turn on Multi-Factor Authentication).
"""

m1_exercises = [
    {
        "title": "Concept Check: Asset vs Threat",
        "description": "Read the following scenario and identify the Asset and the Threat.\\n\\nScenario: A hospital stores patient medical records on a central server. A ransomware gang attempts to encrypt the server to extort money.\\n\\nTask: What is the Asset, and what is the Threat?",
        "difficulty": "Beginner",
        "starter_code": "Asset: \\nThreat: ",
        "solution_code": "Asset: Patient medical records (or server)\\nThreat: Ransomware gang",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Asset: Patient medical records (or server)\\nThreat: Ransomware gang"}]
    },
    {
        "title": "Guided Lab: The Risk Equation",
        "description": "Risk = Threat + Vulnerability. If you remove the Vulnerability, the Risk goes to near zero.\\n\\nScenario: You leave your laptop (Asset) in a coffee shop. The laptop has no password (Vulnerability). A thief (Threat) steals it.\\n\\nTask: Propose a technical security control that would mitigate the Vulnerability.",
        "difficulty": "Beginner",
        "starter_code": "Security Control: ",
        "solution_code": "Security Control: Set a strong login password and enable full disk encryption.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Security Control: Set a strong login password and enable full disk encryption."}]
    },
    {
        "title": "Hands-on Task: Least Privilege Logic",
        "description": "Write a logical security policy using the Principle of Least Privilege.\\n\\nYou have a user named 'Bob' who works in Customer Support. He needs access to the 'Tickets' system. He does NOT need access to 'Payroll' or 'SourceCode'.\\n\\nFormat your answer like:\\nUser: Bob\\nALLOW: [System]\\nDENY: [System], [System]",
        "difficulty": "Intermediate",
        "starter_code": "User: Bob\\nALLOW: \\nDENY: ",
        "solution_code": "User: Bob\\nALLOW: Tickets\\nDENY: Payroll, SourceCode",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "User: Bob\\nALLOW: Tickets\\nDENY: Payroll, SourceCode"}]
    },
    {
        "title": "Scenario Analysis: Defense in Depth",
        "description": "An employee receives a phishing email containing a malicious attachment. They click the attachment.\\n\\nExplain how 'Defense in Depth' would protect the company. List at least two layers of security that should have stopped this attack.",
        "difficulty": "Intermediate",
        "starter_code": "Layer 1: \\nLayer 2: ",
        "solution_code": "Layer 1: Email spam filter to block the phishing email.\\nLayer 2: Endpoint Antivirus to detect the malicious attachment when clicked.\\n(Optional Layer 3): Security awareness training so the user doesn't click it.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Layer 1: Email spam filter to block the phishing email.\\nLayer 2: Endpoint Antivirus to detect the malicious attachment when clicked.\\n(Optional Layer 3): Security awareness training so the user doesn't click it."}]
    },
    {
        "title": "Debugging Task: Find the Flaw",
        "description": "A developer writes this security logic for a website:\\n`if user_input_password == database_password:\\n    grant_admin_access()`\\n\\nThinking with a Security Mindset, what critical assumption is the developer making about the user logging in? Why is this flawed?",
        "difficulty": "Advanced",
        "starter_code": "Assumption: \\nWhy it's flawed: ",
        "solution_code": "Assumption: The developer assumes that only the real admin knows the password.\\nWhy it's flawed: Passwords can be stolen, leaked, or guessed. Just because the password matches does not guarantee the human typing it is the authorized user. (This is why MFA is needed).",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Assumption: The developer assumes that only the real admin knows the password.\\nWhy it's flawed: Passwords can be stolen, leaked, or guessed. Just because the password matches does not guarantee the human typing it is the authorized user. (This is why MFA is needed)."}]
    },
    {
        "title": "Challenge: Assume Breach Design",
        "description": "Your company has a highly secure perimeter firewall. However, the CEO mandates that you adopt an 'Assume Breach' mindset.\\n\\nBased on this mindset, where should you allocate your security budget next? Inside the network, or making the outer firewall stronger? Explain why.",
        "difficulty": "Challenge",
        "starter_code": "Action: \\nReason: ",
        "solution_code": "Action: Allocate budget inside the network (internal monitoring, endpoint detection, encryption).\\nReason: 'Assume Breach' means accepting that the firewall will eventually be bypassed. Therefore, you must focus on detecting and stopping the attacker once they are already inside the network.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Action: Allocate budget inside the network (internal monitoring, endpoint detection, encryption).\\nReason: 'Assume Breach' means accepting that the firewall will eventually be bypassed. Therefore, you must focus on detecting and stopping the attacker once they are already inside the network."}]
    }
]

m1_quizzes = [
    {
        "question_text": "At its most fundamental level, cyber security is primarily a practice of:",
        "options": ["Buying the most expensive firewalls", "Risk management", "Writing complex code", "Eliminating all threats permanently"],
        "correct_answer": "Risk management",
        "explanation": "Absolute security is impossible. Cyber security is about managing risk to an acceptable level.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "In security terminology, what is an 'Asset'?",
        "options": ["A hacker", "A software bug", "Something of value that needs to be protected", "A protective firewall"],
        "correct_answer": "Something of value that needs to be protected",
        "explanation": "Assets are the things you are trying to secure, such as data, servers, or intellectual property.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "A cybercriminal scanning the internet for outdated servers is an example of a:",
        "options": ["Vulnerability", "Threat", "Control", "Asset"],
        "correct_answer": "Threat",
        "explanation": "A threat is an entity capable of causing harm. The cybercriminal is the threat; the outdated server is the vulnerability.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "Which of the following equations accurately represents the concept of Risk?",
        "options": ["Risk = Asset + Control", "Risk = Threat + Vulnerability", "Risk = Exploit - Asset", "Risk = Firewall + Antivirus"],
        "correct_answer": "Risk = Threat + Vulnerability",
        "explanation": "Risk exists when a Threat overlaps with a Vulnerability that can be exploited to harm an Asset.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "Which principle states that a user should only have the exact access rights necessary to perform their job, and nothing more?",
        "options": ["Defense in Depth", "Assume Breach", "Principle of Least Privilege", "Security through Obscurity"],
        "correct_answer": "Principle of Least Privilege",
        "explanation": "Least privilege limits the potential damage if an account is compromised.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "Why is 'Security by Obscurity' (e.g., hiding a server's IP address instead of using a password) considered a dangerous practice?",
        "options": ["It is too expensive", "Attackers use automated tools that will eventually find hidden assets", "It makes the server run too slowly", "It requires advanced programming skills"],
        "correct_answer": "Attackers use automated tools that will eventually find hidden assets",
        "explanation": "Hiding is not securing. Automated scanners scan every possible IP address on the internet; they will find the hidden server.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "Using an email spam filter, endpoint antivirus, and a network firewall simultaneously is an example of:",
        "options": ["Defense in Depth", "Single Point of Failure", "Least Privilege", "Compliance"],
        "correct_answer": "Defense in Depth",
        "explanation": "Defense in depth uses multiple overlapping layers of security controls.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "What does the 'Assume Breach' mindset require security teams to do?",
        "options": ["Give up and let hackers in", "Focus entirely on the perimeter firewall", "Operate under the assumption that attackers are already inside the network and focus on internal detection", "Turn off all internal security controls"],
        "correct_answer": "Operate under the assumption that attackers are already inside the network and focus on internal detection",
        "explanation": "Assuming a breach forces defenders to look for internal lateral movement and anomalous behavior, rather than just trusting the perimeter.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "A developer writes an application and assumes users will only input numbers into the 'Age' field. A security professional reviewing this application should ask:",
        "options": ["Is the font color correct?", "What happens if a user inputs malicious code instead of a number?", "Will this application run on a Mac?", "Did we pay the software license?"],
        "correct_answer": "What happens if a user inputs malicious code instead of a number?",
        "explanation": "The security mindset involves questioning assumptions and asking how a system handles unexpected or malicious input.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "A company passes a legal compliance audit for data privacy. Does this mean their network is secure from hackers?",
        "options": ["Yes, compliance guarantees security.", "No, compliance is a minimum legal baseline, whereas security is an active, ongoing defense against real-world attackers.", "Yes, hackers cannot legally attack compliant companies.", "No, because compliance only protects physical servers."],
        "correct_answer": "No, compliance is a minimum legal baseline, whereas security is an active, ongoing defense against real-world attackers.",
        "explanation": "Compliance checks boxes; security stops hackers. Many compliant companies suffer massive data breaches.",
        "difficulty": "Advanced"
    }
]

m2_lesson = """# Computer & OS Fundamentals

## 1. What Is It?

To understand how to secure a system, or how an attacker exploits it, you must understand the underlying architecture of a computer and its Operating System (OS). 

A computer consists of hardware: the Central Processing Unit (CPU) that does the thinking, the Random Access Memory (RAM) that holds active data, and the Storage (Hard Drive/SSD) that holds data permanently.

The Operating System (like Windows, Linux, or macOS) is the master software that manages this hardware. It sits directly between the physical hardware and the applications you use (like a web browser or a game). It acts as the ultimate authority, deciding which application gets memory, which user can read a file, and which process gets CPU time.

## 2. Why Do We Need It?

Security professionals must understand OS fundamentals because almost all cyber attacks target the interaction between the OS, the memory, and applications.

**Example 1: Malware Execution**
If you don't understand how a program loads from the hard drive into RAM to become a "Process", you cannot understand how an antivirus tool scans memory to stop malware from running.

**Example 2: Privilege Escalation**
If you don't understand how an OS manages "Users" and "Permissions," you won't understand how a hacker who breaches a low-level web server account manages to trick the OS into making them the "Administrator" (Root).

## 3. Where Is It Used?

- **Digital Forensics**: Investigators analyze the OS's RAM to find decrypted passwords and hidden malicious processes.
- **Vulnerability Research**: Security researchers study how the OS handles memory to find buffer overflow vulnerabilities.
- **Incident Response**: Defenders check the OS's internal logs and process trees to track an attacker's movements.
- **System Administration**: IT teams configure OS-level firewalls and file permissions to harden the system against attacks.

## 4. How Does It Work?

1. **Storage**: Your programs (e.g., `calculator.exe`) rest here.
2. **RAM & Processes**: When you open the calculator, the OS copies the program from storage into RAM. It is now a **Process** (an active, running program).
3. **The Kernel**: The core of the OS is called the Kernel. It lives in a highly protected area of RAM called **Kernel Space**. It has total control over the hardware.
4. **User Space**: Everyday applications run in an isolated area called **User Space**. They cannot talk to the hardware directly.
5. **System Calls**: If the calculator (User Space) wants to draw on the screen or save a file, it must politely ask the Kernel to do it via a **System Call**. The Kernel checks permissions and performs the action.

## 5. Important Terminology

| Term | Meaning |
|------|---------|
| **Kernel Space** | The protected memory area where the core OS runs. Has absolute power. |
| **User Space** | The restricted area where normal applications run. |
| **Process** | A running instance of a program loaded into memory. |
| **Thread** | A smaller unit of execution inside a process. |
| **System Call (Syscall)** | How a user-space application requests a privileged action from the Kernel. |
| **File Permissions** | OS rules dictating which users can Read, Write, or Execute a specific file. |

## 6. Architecture / Diagram

```text
The OS Abstraction Layer

+-------------------------------------------------+
|                  USER SPACE                     |
|  [ Web Browser ]    [ Word Processor ]          |
|         |                   |                   |
|         +--> (System Call)--+                   |
+----------------------|--------------------------+
                       v
+-------------------------------------------------+
|                 KERNEL SPACE                    |
|             (The Operating System)              |
|  [ Memory Manager ]  [ Process Scheduler ]      |
|  [ File System ]     [ Network Stack ]          |
+----------------------|--------------------------+
                       v
+-------------------------------------------------+
|                   HARDWARE                      |
|             CPU, RAM, Hard Drive, NIC           |
+-------------------------------------------------+
```

## 7. Syntax / Commands / Configuration

In a modern OS, you can view the processes running in memory. In Windows, you use Task Manager. In Linux or macOS, you can use the command line:

```bash
# View all currently running processes
ps aux

# Intercept and watch the System Calls made by a program (Linux)
strace ls
```
*Note: `strace` is a powerful tool for malware analysts. If you run a suspicious file and `strace` shows it making system calls to open your SSH keys and send them over the network, you know it is malicious.*

## 8. Beginner Example

Think of the **Kernel** as a bank teller behind bulletproof glass, and **User Space applications** as the customers in the lobby.

A customer (application) cannot reach through the glass and grab cash from the vault (hardware). They must fill out a slip (System Call) and hand it to the teller (Kernel). The teller checks their ID (Permissions), walks into the vault, gets the cash, and hands it back. If a malicious customer tries to ask for someone else's money, the teller denies the request.

## 9. Real-World Example

**Situation**: A user downloads a malicious PDF. The PDF reader application runs in User Space.
**Weakness**: The user is logged into their computer using a full "Administrator" account.
**Risk**: When the malicious PDF exploits a flaw in the reader, the malware inherits the user's Administrator privileges.
**Detection**: The OS logs show the PDF reader suddenly attempting to modify core system files in the `C:\\Windows\\System32` directory.
**Mitigation**: The organization implements the Principle of Least Privilege, forcing users to use "Standard User" accounts. Now, when the malware asks the Kernel to modify system files, the Kernel says "Access Denied."

## 10. What Happens Internally? (Virtual Memory)

When the OS loads a process into RAM, it uses a trick called **Virtual Memory**. 
The OS lies to the process, giving it "fake" memory addresses. The process thinks it has a massive, contiguous block of RAM entirely to itself. Behind the scenes, the OS translates these fake virtual addresses into real physical addresses on the RAM chips.

*Security Impact*: Because every process has its own isolated virtual memory space, Process A (a video game) literally cannot see or access the memory of Process B (your banking browser tab). If malware wants to steal your banking password from memory, it has to find a way to break this OS-enforced isolation.

## 11. Common Mistakes

1. **Running as Root/Admin**: Operating your computer daily on an Administrator account means any malware you accidentally run instantly owns the entire machine.
2. **Ignoring OS Updates**: The OS Kernel is software, and it has bugs. If a hacker finds a bug in the Kernel, they can bypass User Space entirely. OS updates patch these critical Kernel bugs.
3. **Assuming Hidden Files are Secure**: Hiding a folder does not change its OS permissions. A hacker's script will still find it and read it.
4. **Trusting Process Names**: Malware often names itself `svchost.exe` (a legitimate Windows process name). Defenders must look at the process's file path and digital signature, not just its name.

## 12. Defensive Best Practices

1. **Use Standard Accounts**: Reserve Administrator accounts solely for installing software or changing system configurations.
2. **Enable OS Isolation Features**: Ensure features like ASLR (Address Space Layout Randomization) are enabled to make memory exploitation harder.
3. **Audit File Permissions**: Regularly check that sensitive files are only readable by authorized users, utilizing the OS permission system (e.g., chmod in Linux, NTFS permissions in Windows).
4. **Monitor Process Execution**: Use Endpoint Detection tools to monitor what child processes are spawned. (e.g., if Microsoft Word suddenly spawns a command prompt, that is highly suspicious).

## 13. Security Mindset

When analyzing how a program interacts with the OS, ask:
- *What system calls is this program making? Why does a calculator need to access the network?*
- *What user context is this process running under? Is it running as a low-privilege user, or as the SYSTEM?*
- *If I crash this User Space program, can I trick the Kernel into giving me control?*

## 14. Try It Yourself

Open the process viewer on your computer (Task Manager on Windows, Activity Monitor on Mac).
1. Look at the list of running processes. 
2. Notice the "User" column. You will see processes running under your username, but you will also see processes running as "SYSTEM" or "root". 
3. Select a process running as your user and end/kill it. The app closes.
4. (Don't actually do this) but realize that if you tried to kill a "SYSTEM" process, the OS Kernel would deny your request, protecting itself from you!
"""

m2_exercises = [
    {
        "title": "Concept Check: Kernel Space vs User Space",
        "description": "Read the scenario and identify if the action takes place in Kernel Space or User Space.\\n\\nScenario: You are typing a document in Microsoft Word. Microsoft Word is currently processing your keystrokes.\\n\\nOutput exactly one phrase: Kernel Space or User Space.",
        "difficulty": "Beginner",
        "starter_code": "Space: ",
        "solution_code": "User Space",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "User Space"}]
    },
    {
        "title": "Guided Lab: System Calls",
        "description": "User space applications cannot directly touch hardware. \\n\\nScenario: You click 'Save' in your text editor. The editor needs to write data to the hard drive.\\n\\nTask: What is the specific mechanism the editor must use to ask the Operating System to perform this action?",
        "difficulty": "Beginner",
        "starter_code": "Mechanism: ",
        "solution_code": "System Call (or Syscall)",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "System Call (or Syscall)"}]
    },
    {
        "title": "Hands-on Task: Analyze Process Privileges",
        "description": "You are a defender reviewing running processes. You see the following:\\n\\nProcess Name: `calc.exe`\\nUser: `SYSTEM`\\nNetwork Connections: `ESTABLISHED to 185.x.x.x`\\n\\nTask: Based on OS fundamentals, state two reasons why this process is highly suspicious.",
        "difficulty": "Intermediate",
        "starter_code": "Reason 1: \\nReason 2: ",
        "solution_code": "Reason 1: A calculator should not be running as the highly privileged 'SYSTEM' user.\\nReason 2: A calculator has no legitimate reason to establish external network connections.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Reason 1: A calculator should not be running as the highly privileged 'SYSTEM' user.\\nReason 2: A calculator has no legitimate reason to establish external network connections."}]
    },
    {
        "title": "Scenario Analysis: Virtual Memory",
        "description": "An attacker creates a malicious program that tries to read the memory addresses belonging to your password manager program to steal your master password.\\n\\nTask: Explain the OS feature that prevents the malicious program from simply reading the memory of the password manager.",
        "difficulty": "Intermediate",
        "starter_code": "Explanation: ",
        "solution_code": "Explanation: Virtual Memory. The OS isolates each process into its own virtual memory space. The malicious program cannot see or access the physical RAM addresses used by the password manager.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Explanation: Virtual Memory. The OS isolates each process into its own virtual memory space. The malicious program cannot see or access the physical RAM addresses used by the password manager."}]
    },
    {
        "title": "Debugging Task: The Rootkit",
        "description": "You run an antivirus scan in User Space, and it reports the system is 100% clean. However, you know the computer is infected. You discover the malware is a 'Rootkit' operating in Kernel Space.\\n\\nTask: Explain logically why the User Space antivirus failed to detect the Kernel Space rootkit.",
        "difficulty": "Advanced",
        "starter_code": "Explanation: ",
        "solution_code": "Explanation: Because the rootkit lives in the Kernel, it controls the OS. When the User Space antivirus asks the OS via a system call to list all files/processes, the compromised Kernel simply lies and hides the malware's existence.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Explanation: Because the rootkit lives in the Kernel, it controls the OS. When the User Space antivirus asks the OS via a system call to list all files/processes, the compromised Kernel simply lies and hides the malware's existence."}]
    },
    {
        "title": "Challenge: Privilege Escalation",
        "description": "A hacker breaches a web server, gaining access as a low-privilege user named `www-data`. The hacker uploads a script that exploits a buffer overflow bug in the OS Kernel itself.\\n\\nTask: What is the exact security term for what the hacker just achieved by exploiting the Kernel to gain higher access? (Two words)",
        "difficulty": "Challenge",
        "starter_code": "Term: ",
        "solution_code": "Privilege Escalation",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Privilege Escalation"}]
    }
]

m2_quizzes = [
    {
        "question_text": "What is the primary function of the Operating System Kernel?",
        "options": ["To render graphics on the screen", "To manage and control all hardware resources and mediate access for software applications", "To browse the internet securely", "To encrypt user passwords"],
        "correct_answer": "To manage and control all hardware resources and mediate access for software applications",
        "explanation": "The Kernel is the core of the OS. It controls the CPU, memory, and hardware, and enforces security boundaries.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "Normal applications, like a web browser or a video game, run in which area of the OS architecture?",
        "options": ["Kernel Space", "Hardware Space", "User Space", "BIOS Space"],
        "correct_answer": "User Space",
        "explanation": "User space is the restricted area where everyday applications run. They cannot directly access hardware.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "What is a 'Process' in the context of computer architecture?",
        "options": ["An active, running instance of a program loaded into RAM", "A dormant executable file resting on the hard drive", "A piece of hardware that processes graphics", "A system call made to the Kernel"],
        "correct_answer": "An active, running instance of a program loaded into RAM",
        "explanation": "When you execute a program on disk, the OS loads it into memory, and it becomes an active Process.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "How does a User Space application request a privileged action (like saving a file) from the Kernel?",
        "options": ["It writes the file directly to the hard drive", "It issues a System Call (Syscall)", "It modifies the Virtual Memory", "It bypasses the Kernel using a Thread"],
        "correct_answer": "It issues a System Call (Syscall)",
        "explanation": "Syscalls are the formal, secure mechanism applications use to ask the Kernel to perform actions on their behalf.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "What OS feature prevents one process (like a malicious game) from reading the memory of another process (like your password manager)?",
        "options": ["Virtual Memory", "The Hard Drive", "System Calls", "Antivirus"],
        "correct_answer": "Virtual Memory",
        "explanation": "Virtual memory isolates processes by giving each one the illusion of a private memory space, handled via the OS and hardware MMU.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "Why is running a computer using a daily 'Administrator' or 'Root' account considered a major security risk?",
        "options": ["It causes the CPU to overheat", "It prevents the OS from applying updates", "Any malware executed by the user instantly inherits those high privileges, allowing it to modify core OS files", "It disables Virtual Memory"],
        "correct_answer": "Any malware executed by the user instantly inherits those high privileges, allowing it to modify core OS files",
        "explanation": "Operating at Least Privilege (using a standard account) ensures that if malware runs, it doesn't have the permissions needed to destroy the OS.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "A security analyst is investigating a compromised system. They suspect a 'Rootkit' is installed. Where does a rootkit typically reside to be so effective at hiding?",
        "options": ["User Space", "Kernel Space", "In the Web Browser", "In a Word Document"],
        "correct_answer": "Kernel Space",
        "explanation": "Rootkits operate at the Kernel level. Because they control the OS, they can lie to User Space security tools (like antivirus) about what processes are actually running.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "You are monitoring an endpoint and see Microsoft Word (`winword.exe`) spawn a child process called Command Prompt (`cmd.exe`). Based on OS and Process fundamentals, what is the best conclusion?",
        "options": ["This is normal behavior for a word processor", "Microsoft Word is updating itself", "This is highly suspicious; a document application should rarely need to open a command line shell", "The user is typing very fast"],
        "correct_answer": "This is highly suspicious; a document application should rarely need to open a command line shell",
        "explanation": "Malicious macros in Word documents often attempt to spawn shell processes to download malware. Defenders monitor process parent-child relationships to spot this.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "In Linux, what tool can a malware analyst use to intercept and record the exact System Calls a suspicious program is making?",
        "options": ["ps", "top", "strace", "chmod"],
        "correct_answer": "strace",
        "explanation": "strace (system call tracer) allows you to see exactly what the application is asking the Kernel to do (e.g., open files, make network connections).",
        "difficulty": "Advanced"
    },
    {
        "question_text": "What is the primary danger of a 'Buffer Overflow' vulnerability in relation to the OS?",
        "options": ["It deletes files on the hard drive", "It fills up the RAM until the computer crashes", "It allows an attacker to overwrite memory boundaries, potentially tricking the CPU into executing the attacker's malicious code", "It causes network lag"],
        "correct_answer": "It allows an attacker to overwrite memory boundaries, potentially tricking the CPU into executing the attacker's malicious code",
        "explanation": "Buffer overflows manipulate how data is stored in memory (like the Stack), allowing attackers to hijack the execution flow of the process.",
        "difficulty": "Advanced"
    }
]


m3_lesson = """# Networking Fundamentals

## 1. What Is It?

Networking is the practice of connecting computers together so they can share data. A network can be as small as two computers connected by a cable, or as large as the internet, which connects billions of devices globally.

To understand network security, you must first understand how computers talk to each other. When you send an email or load a webpage, the data isn't sent as one giant piece. Instead, the data is chopped up into tiny, manageable pieces called **Packets**. These packets are sent across the network, passed from router to router, until they reach their destination, where they are reassembled.

## 2. Why Do We Need It?

Without networking, computers are isolated islands. Everything that makes modern technology useful—the web, cloud computing, multiplayer gaming, streaming video—relies entirely on networking.

**Example 1: The World Wide Web**
When you type `google.com` into your browser, you are relying on a complex network to ask a server thousands of miles away for a webpage, and send it back to your screen in milliseconds.

**Example 2: Enterprise File Sharing**
In an office, employees need to share documents and access central databases. Instead of passing physical USB drives around, a Local Area Network (LAN) allows instant, secure sharing of resources.

## 3. Where Is It Used?

- **LAN (Local Area Network)**: The network inside your home or a single office building.
- **WAN (Wide Area Network)**: Large networks that connect different cities or countries (the internet is the biggest WAN).
- **WLAN (Wireless LAN)**: Wi-Fi networks.
- **VPN (Virtual Private Network)**: A secure, encrypted "tunnel" created over a public network.

## 4. How Does It Work?

For two computers to talk, they need three basic things:
1. **A Physical Connection**: Cables (Ethernet/Fiber) or Radio Waves (Wi-Fi).
2. **An Address**: Just like houses need street addresses to receive mail, computers need addresses to receive packets. The most common addresses are **MAC Addresses** (physical hardware addresses) and **IP Addresses** (logical network addresses).
3. **A Common Language (Protocol)**: If one computer speaks English and the other speaks French, they can't communicate. Network protocols (like TCP/IP) provide a strict set of rules that all computers agree to follow so they can understand each other's packets.

## 5. Important Terminology

| Term | Meaning |
|------|---------|
| **Packet** | A small chunk of data sent over a network. |
| **IP Address** | The logical address of a device on a network (e.g., `192.168.1.10`). |
| **MAC Address** | The permanent, physical address baked into a device's network card. |
| **Router** | A device that forwards packets between *different* networks (like connecting your home LAN to the internet). |
| **Switch** | A device that connects devices together on the *same* network (LAN). |
| **Protocol** | A standard set of rules for formatting and processing data. |

## 6. Architecture / Diagram

```text
A Basic Home Network

                     [ The Internet ]
                            |
                     (Public IP Address)
                            |
                      [ ISP Modem ]
                            |
                     [ Home Router ] (Acts as Gateway)
                            |
         +------------------+------------------+
         |                                     |
    [ Switch ]                             [ Wi-Fi ]
         |                                     |
   +-----+-----+                         +-----+-----+
   |           |                         |           |
[ PC 1 ]    [ PC 2 ]                 [ Laptop ] [ Smartphone ]
(192.168.1.2) (192.168.1.3)          (192.168.1.4) (192.168.1.5)
```

## 7. Syntax / Commands / Configuration

You can inspect your own network configuration using built-in OS tools.

**On Windows:**
```bash
# View your IP address and network details
ipconfig

# Test connectivity to a specific IP or website (sends tiny ping packets)
ping 8.8.8.8
```

**On Linux/Mac:**
```bash
# View your IP address
ip addr 
# (or 'ifconfig' on older systems/Mac)

# Trace the path packets take to a destination
traceroute google.com
```

## 8. Beginner Example

Think of the postal service.
- The **Packet** is the envelope containing your letter.
- The **IP Address** is the mailing address written on the front.
- The **Router** is the post office. When you drop a letter in a mailbox, the post office reads the address and decides which truck to put it on to get it closer to its destination.

## 9. Real-World Example

**Situation**: An attacker wants to steal sensitive documents from a company's database.
**Weakness**: The database is connected directly to the internet with a public IP address.
**Risk**: Anyone in the world can attempt to send packets to the database and guess its password.
**Detection**: Network monitoring tools flag thousands of connection attempts coming from a foreign country.
**Mitigation**: The company reconfigures their network, placing the database on a private, internal LAN (like `10.0.0.5`). They put a Firewall between the LAN and the Internet. The firewall is configured to block ALL incoming traffic from the internet to the database.

## 10. What Happens Internally? (The OSI Model)

Networking is complex, so engineers divide it into layers. The theoretical standard is the **OSI Model** (Open Systems Interconnection). 

When you send an email, the data starts at the Application layer (Layer 7) and travels down to the Physical layer (Layer 1):
- **L7 Application**: The email program formats the message.
- **L6 Presentation**: Encrypts the data (TLS).
- **L5 Session**: Establishes the connection.
- **L4 Transport**: Chops the data into segments (TCP).
- **L3 Network**: Adds the destination IP Address (Routing).
- **L2 Data Link**: Adds the physical MAC address (Switching).
- **L1 Physical**: Converts it all into electrical electrical signals or light pulses over the cable.

*Security Note: Attackers specialize in different layers. Phishing happens at Layer 7. DDoS attacks often happen at Layer 3 or Layer 4.*

## 11. Common Mistakes

1. **Exposing internal services**: Putting databases or file shares on public IP addresses.
2. **Ignoring physical security**: An attacker doesn't need to hack your firewall if they can just plug a laptop into an exposed ethernet port in your lobby.
3. **Failing to segment networks**: Putting the guest Wi-Fi and the HR database on the same LAN segment. If a guest's phone has malware, it can scan the HR database.
4. **Using unencrypted protocols**: Sending sensitive data over Telnet or FTP, which transmit data (and passwords) in plain, readable text.

## 12. Defensive Best Practices

1. **Network Segmentation**: Divide your network into isolated zones (e.g., Guest, Employee, Servers) using a firewall or VLANs (Virtual LANs).
2. **Default Deny**: Configure firewalls to block all incoming traffic by default, and explicitly allow only what is absolutely necessary.
3. **Network Intrusion Detection (NIDS)**: Deploy sensors that passively listen to network traffic, looking for patterns of known malware or attacks.
4. **Hide Internal IPs (NAT)**: Use Network Address Translation so internal devices use private, non-routable IPs (like `192.168.x.x`), masking them from the public internet.

## 13. Security Mindset

When analyzing a network architecture, ask:
- *What path does data take to get from point A to point B?*
- *Are there any choke points where I can inspect the traffic?*
- *If an attacker compromises a laptop on the Guest Wi-Fi, what else can they see or reach on the network?*

## 14. Try It Yourself

Open your terminal or command prompt.
Type `ping google.com` (or `ping 8.8.8.8`).
You will see replies coming back with a "time" measured in milliseconds (ms). This represents the round-trip time it took for a single packet to leave your computer, travel through your router, across your ISP, to Google's servers, and come back.
"""

m3_exercises = [
    {
        "title": "Concept Check: Router vs Switch",
        "description": "Read the scenario and decide if you need a Router or a Switch.\\n\\nScenario: You have 5 computers in the same office room. You want to connect them together so they can share files with each other on the local network (LAN). You do NOT need to connect them to the internet.\\n\\nTask: Do you need a Router or a Switch?",
        "difficulty": "Beginner",
        "starter_code": "Device: ",
        "solution_code": "Switch",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Switch"}]
    },
    {
        "title": "Guided Lab: IP Addresses",
        "description": "There are Public IP addresses (reachable from the internet) and Private IP addresses (only reachable on a local network).\\n\\nCommon Private IP ranges are:\\n10.x.x.x\\n172.16.x.x to 172.31.x.x\\n192.168.x.x\\n\\nTask: Classify the IP address `8.8.8.8`. Output exactly one word: Public or Private.",
        "difficulty": "Beginner",
        "starter_code": "Type: ",
        "solution_code": "Public",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Public"}]
    },
    {
        "title": "Hands-on Task: Network Segmentation Logic",
        "description": "Your company has three networks:\\n- 10.0.1.x (Guest Wi-Fi)\\n- 10.0.2.x (Employee Laptops)\\n- 10.0.3.x (Financial Servers)\\n\\nTask: Write a simple firewall rule logic to secure the Financial Servers. Format your answer like:\\nALLOW [Source] to [Destination]\\nDENY [Source] to [Destination]",
        "difficulty": "Intermediate",
        "starter_code": "ALLOW \\nDENY ",
        "solution_code": "ALLOW 10.0.2.x to 10.0.3.x\\nDENY 10.0.1.x to 10.0.3.x",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "ALLOW 10.0.2.x to 10.0.3.x\\nDENY 10.0.1.x to 10.0.3.x"}]
    },
    {
        "title": "Scenario Analysis: OSI Layers",
        "description": "An attacker sends millions of junk packets to a web server, overwhelming its network interface card and causing it to drop legitimate connections.\\n\\nTask: Based on the OSI model description, is this attack primarily targeting Layer 7 (Application) or Layer 3/4 (Network/Transport)?",
        "difficulty": "Intermediate",
        "starter_code": "Layer: ",
        "solution_code": "Layer 3/4 (Network/Transport)",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Layer 3/4 (Network/Transport)"}]
    },
    {
        "title": "Debugging Task: The Ping Failure",
        "description": "A user complains they cannot reach a server at `192.168.5.50`.\\n\\nYou run `ping 192.168.5.50` and receive the error: 'Destination Host Unreachable'.\\nYou run `ping 8.8.8.8` (Google) and it succeeds.\\n\\nTask: Based on network fundamentals, where is the most likely problem? Is the user's internet down, or is there an internal routing/server issue?",
        "difficulty": "Advanced",
        "starter_code": "Diagnosis: ",
        "solution_code": "Internal routing/server issue. Because pinging 8.8.8.8 works, the internet connection is fine. The issue is reaching the local/internal IP 192.168.5.50.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Internal routing/server issue. Because pinging 8.8.8.8 works, the internet connection is fine. The issue is reaching the local/internal IP 192.168.5.50."}]
    },
    {
        "title": "Challenge: MAC vs IP Address",
        "description": "Why does a computer need both an IP address and a MAC address?\\n\\nHint: Think about sending a letter. You have the recipient's house address, but how do the mail trucks actually hand off the letter at each stop?\\n\\nTask: Summarize the difference in 1-2 sentences.",
        "difficulty": "Challenge",
        "starter_code": "Difference: ",
        "solution_code": "The IP address is the logical, end-to-end destination across the internet (like a mailing address). The MAC address is the physical hardware address used to deliver the packet hop-by-hop on the local network segments.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "The IP address is the logical, end-to-end destination across the internet (like a mailing address). The MAC address is the physical hardware address used to deliver the packet hop-by-hop on the local network segments."}]
    }
]

m3_quizzes = [
    {
        "question_text": "What is a network 'packet'?",
        "options": ["A physical device used to connect computers", "A small, formatted chunk of data sent over a network", "A type of firewall rule", "A web browser plugin"],
        "correct_answer": "A small, formatted chunk of data sent over a network",
        "explanation": "Data is broken down into packets to be efficiently transmitted across networks.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "Which of the following IP addresses is a Private IP address (commonly used on local LANs and not routable on the public internet)?",
        "options": ["8.8.8.8", "1.1.1.1", "192.168.1.15", "104.21.5.10"],
        "correct_answer": "192.168.1.15",
        "explanation": "Addresses starting with 192.168.x.x, 10.x.x.x, and 172.16-31.x.x are reserved for private, internal networks.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "What is the primary difference between a Router and a Switch?",
        "options": ["A router connects different networks together, while a switch connects devices on the same local network", "A router is for wireless devices, a switch is for wired devices", "A switch connects to the internet, a router connects to the printer", "There is no difference"],
        "correct_answer": "A router connects different networks together, while a switch connects devices on the same local network",
        "explanation": "Switches handle local traffic (Layer 2). Routers handle traffic destined for other networks (Layer 3).",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "In the OSI Model, which layer is responsible for adding logical addressing (IP addresses) and routing packets?",
        "options": ["Layer 1 (Physical)", "Layer 2 (Data Link)", "Layer 3 (Network)", "Layer 7 (Application)"],
        "correct_answer": "Layer 3 (Network)",
        "explanation": "Layer 3 (The Network layer) handles IP addressing and routing.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "If a hacker wants to steal user credentials by intercepting network traffic on a public Wi-Fi hotspot, which defensive practice best protects the users?",
        "options": ["Using a strong Wi-Fi password", "Network Segmentation", "Using encrypted protocols (like HTTPS or a VPN)", "Running an antivirus scan daily"],
        "correct_answer": "Using encrypted protocols (like HTTPS or a VPN)",
        "explanation": "Encryption ensures that even if an attacker intercepts the packets, the data inside is unreadable.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "What does a Firewall do?",
        "options": ["It increases internet speed", "It physically prevents computers from overheating", "It inspects network traffic and allows or blocks it based on a defined set of security rules", "It encrypts all hard drives"],
        "correct_answer": "It inspects network traffic and allows or blocks it based on a defined set of security rules",
        "explanation": "Firewalls act as security guards at the border of a network, making decisions about what traffic is allowed in or out.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "Why is 'Network Segmentation' considered a critical security best practice?",
        "options": ["It makes the network faster for everyone", "If an attacker compromises one part of the network, segmentation prevents them from easily accessing more sensitive areas", "It reduces the electricity cost of running switches", "It allows everyone to access the database without a password"],
        "correct_answer": "If an attacker compromises one part of the network, segmentation prevents them from easily accessing more sensitive areas",
        "explanation": "Segmentation limits the 'blast radius' of an attack.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "What command-line tool is used to send a simple echo request to a destination IP to test if it is reachable?",
        "options": ["ping", "ipconfig", "chmod", "mkdir"],
        "correct_answer": "ping",
        "explanation": "Ping sends ICMP Echo Request packets and waits for an Echo Reply, testing basic connectivity.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "In a corporate environment, a 'Default Deny' firewall policy means:",
        "options": ["All traffic is allowed unless specifically blocked", "All traffic is blocked unless specifically allowed", "Only web traffic is blocked", "The firewall is turned off by default"],
        "correct_answer": "All traffic is blocked unless specifically allowed",
        "explanation": "Default Deny is a highly secure stance. You start with zero access and poke specific holes only for required business functions.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "What is a MAC address?",
        "options": ["The address of an Apple computer", "The logical address assigned by your internet provider", "The permanent, physical hardware address burned into a network interface card", "A type of encrypted password"],
        "correct_answer": "The permanent, physical hardware address burned into a network interface card",
        "explanation": "MAC (Media Access Control) addresses are used for Layer 2 (local) communication on the physical network segment.",
        "difficulty": "Intermediate"
    }
]


m4_lesson = """# TCP/IP, Ports & Protocols

## 1. What Is It?

While "networking" is the physical act of connecting computers, **TCP/IP** (Transmission Control Protocol / Internet Protocol) is the specific suite of rules that makes the modern internet possible. 

Think of IP addresses as the address of an apartment building. But how does the mail carrier know which specific apartment to deliver the mail to? That is where **Ports** come in. 

A Port is a logical endpoint through which network applications communicate. There are 65,535 possible ports on a computer. Specific services (like web servers, email servers, and remote login servers) "listen" on specific, standard port numbers.

## 2. Why Do We Need It?

Without ports, a computer wouldn't know what to do with an incoming packet. 

If a packet arrives at your computer, is it a piece of a YouTube video, a Skype call, or a hacker trying to log in? The **Port number** tells the operating system which application should process the data.

**Example 1: A Web Server**
A standard web server has two main doors open:
- Port 80 (HTTP - Unencrypted web traffic)
- Port 443 (HTTPS - Encrypted web traffic)

**Example 2: Remote Management**
A Linux server administrator might leave Port 22 open. Port 22 is used for SSH (Secure Shell), allowing the admin to remotely log into the server and type commands. 

## 3. Where Is It Used?

Security professionals, penetration testers, and attackers all care deeply about ports.
- **Attackers** perform "Port Scanning" to find out exactly what doors are open on a target building.
- **Defenders** configure firewalls to block access to dangerous or unnecessary ports.
- **Malware** often opens a random high-numbered port (e.g., Port 4444) to create a "backdoor" so the attacker can control the infected machine.

## 4. How Does It Work?

1. **The Request**: Your web browser wants to load a secure website. It creates a packet.
2. **Addressing**: The packet is addressed to the server's IP address, and specifically addressed to **Destination Port 443** (HTTPS). 
3. **The Protocol**: The packet uses **TCP**. TCP is a "reliable" protocol. It requires a handshake before sending data to ensure the server is ready, and it checks to make sure every packet arrives in order.
4. **The Delivery**: The packet arrives at the server. The server's OS sees it is for Port 443, so it hands the data to the web server software (like Apache or Nginx).

*(Note: There is another protocol called UDP. UDP just throws packets at the destination as fast as possible without checking if they arrive. It's used for live video streaming and gaming).*

## 5. Important Terminology

| Term | Meaning |
|------|---------|
| **Port** | A logical communication endpoint (0 to 65535). |
| **TCP** | Transmission Control Protocol. Reliable, connection-oriented data delivery. |
| **UDP** | User Datagram Protocol. Fast, connectionless data delivery (no error checking). |
| **Port Scanning** | Using a tool to probe a computer to see which ports are open and listening. |
| **Protocol** | The specific language spoken over a port (e.g., HTTP is spoken over Port 80). |

## 6. Architecture / Diagram

```text
The Server's "Doors"

IP Address: 192.168.1.10
=======================================
|                                     |
|  [Port 22] ----> SSH Service        |  (Secure remote login)
|                                     |
|  [Port 80] ----> Web Service        |  (Standard HTTP)
|                                     |
|  [Port 443] ---> Secure Web         |  (Encrypted HTTPS)
|                                     |
|  [Port 3306] --> Database           |  (MySQL Database)
|                                     |
=======================================

Firewall Rule:
Allow Port 80, 443 from ANYWHERE.
Allow Port 22 from ADMIN_IP ONLY.
BLOCK ALL OTHER PORTS.
```

## 7. Syntax / Commands / Configuration

You can see which ports are currently open and listening on your own machine using the `ss` (socket statistics) or `netstat` commands.

```bash
# Linux: Show all listening TCP and UDP ports
ss -tuln

# Example Output:
# Netid  State   Local Address:Port   Peer Address:Port
# tcp    LISTEN  0.0.0.0:22           0.0.0.0:*
# tcp    LISTEN  0.0.0.0:80           0.0.0.0:*
```

Attackers and penetration testers use a tool called **Nmap** to scan *other* people's computers to find open ports:
```bash
# Scan a target IP to see what ports are open
nmap 192.168.1.10
```

## 8. Beginner Example

Think of an IP address as a hotel's street address (123 Main St).
Think of the Ports as the room numbers (Room 80, Room 22, Room 443).

If you want to talk to the web server, you mail a letter to `123 Main St, Room 80`.
If you want to manage the server, you mail a letter to `123 Main St, Room 22`.

A port scan is like a burglar walking down the hotel hallway, jiggling every single doorknob (from 1 to 65535) to see which doors are unlocked and what is inside.

## 9. Real-World Example

**Situation**: A hospital installs a new MRI machine. The vendor configures it and leaves Port 3389 (Windows Remote Desktop) open to the internet so they can provide remote tech support.
**Weakness**: Port 3389 is exposed to the entire internet, and protected by a weak password.
**Risk**: Attackers constantly scan the internet for open 3389 ports.
**Detection**: An attacker finds the open port, guesses the password, logs in, and deploys ransomware.
**Mitigation**: The hospital's security team configures the firewall to block Port 3389 from the internet. Remote support must now connect through a secure VPN first.

## 10. What Happens Internally? (The TCP Handshake)

When a computer connects to a TCP port, it doesn't just start sending data. It performs a 3-Way Handshake to establish trust and synchronize.

1. **SYN (Synchronize)**: Client sends a packet saying, "Hello, I want to talk. Are you there?"
2. **SYN-ACK (Synchronize-Acknowledge)**: Server replies, "Hello, I am here and ready to talk."
3. **ACK (Acknowledge)**: Client replies, "Great, I received your acknowledgment. Here comes the data."

*Security Note: A classic DDoS attack called a "SYN Flood" involves an attacker sending millions of SYN packets. The server sends SYN-ACKs and waits for the final ACK... which never comes. The server leaves all these half-open connections waiting until it runs out of memory and crashes.*

## 11. Common Mistakes

1. **Leaving Default Ports Open**: Leaving database ports (like 3306 for MySQL or 27017 for MongoDB) exposed to the public internet. Databases should only be accessible by the web server, never the public.
2. **Using Telnet or FTP**: These ancient protocols operate on Ports 23 and 21. They send data (and passwords) completely unencrypted. Use SSH (22) and SFTP (22) instead.
3. **Security by Obscurity with Ports**: Moving an SSH server from Port 22 to Port 2222. An attacker's port scanner will find it anyway. It does not provide real security.

## 12. Defensive Best Practices

1. **Close Unused Ports**: If a server is just a web server, it only needs ports 80 and 443 open. Close everything else at the firewall.
2. **Egress Filtering**: Don't just block bad traffic coming *in*. Block unexpected traffic going *out*. If a web server suddenly tries to connect to an external server on Port 4444, it's likely compromised and trying to phone home.
3. **Monitor Port Scans**: Configure your Intrusion Detection System (IDS) to alert you if a single IP address tries to connect to 100 different ports in a few seconds (a clear sign of an attacker doing reconnaissance).

## 13. Security Mindset

When analyzing a system's exposed ports, ask:
- *Why is this door open? What application is running behind it?*
- *Who needs to access this door? The whole world, or just one specific internal server?*
- *Is the protocol communicating over this port encrypted?*
- *If a vulnerability is found in the application listening on this port, what privileges does that application have on the OS?*

## 14. Try It Yourself

Open your terminal or command prompt.
If you are on Windows, type: `netstat -an | findstr "LISTENING"`
If you are on Linux/Mac, type: `netstat -tuln` or `ss -tuln`

Look at the output. These are the ports currently open on your machine. Any port listed here is an application waiting for incoming network connections.
"""

m4_exercises = [
    {
        "title": "Concept Check: TCP vs UDP",
        "description": "Read the scenario and decide if the application should use TCP or UDP.\\n\\nScenario: A bank needs to transfer $1,000,000 between accounts. It is absolutely critical that not a single byte of data is lost or corrupted in transit.\\n\\nTask: Should the developers use TCP or UDP?",
        "difficulty": "Beginner",
        "starter_code": "Protocol: ",
        "solution_code": "TCP",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "TCP"}]
    },
    {
        "title": "Guided Lab: Common Ports",
        "description": "Security professionals must memorize common ports.\\n\\nTask: Match the following protocols to their standard port numbers: HTTP, HTTPS, SSH.\\n(Provide your answer as comma separated port numbers in that exact order).",
        "difficulty": "Beginner",
        "starter_code": "Ports: ",
        "solution_code": "80, 443, 22",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "80, 443, 22"}]
    },
    {
        "title": "Hands-on Task: Port Blocking Logic",
        "description": "You are a firewall administrator for a web server. The server needs to serve secure web pages to the public internet, but administrators also need to securely log in via command line from the internal corporate network (10.0.5.0/24).\\n\\nTask: Write the logic to secure these ports. Focus on Ports 443 and 22.",
        "difficulty": "Intermediate",
        "starter_code": "Port 443: ALLOW FROM \\nPort 22: ALLOW FROM ",
        "solution_code": "Port 443: ALLOW FROM Anywhere (or All)\\nPort 22: ALLOW FROM 10.0.5.0/24 (or Internal Network)",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Port 443: ALLOW FROM Anywhere (or All)\\nPort 22: ALLOW FROM 10.0.5.0/24 (or Internal Network)"}]
    },
    {
        "title": "Scenario Analysis: The Shodan Search",
        "description": "A researcher uses Shodan (a search engine for internet-connected devices) and discovers a company's internal MySQL database is listening on Port 3306 on a public IP address.\\n\\nTask: Why is this an architectural failure, and what is the immediate risk?",
        "difficulty": "Intermediate",
        "starter_code": "Analysis: ",
        "solution_code": "Architectural failure: Databases should never be exposed directly to the public internet; they should only accept connections from the backend web server. Risk: Anyone can attempt to brute-force the database password or exploit database vulnerabilities to steal data.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Architectural failure: Databases should never be exposed directly to the public internet; they should only accept connections from the backend web server. Risk: Anyone can attempt to brute-force the database password or exploit database vulnerabilities to steal data."}]
    },
    {
        "title": "Debugging Task: SYN Flood Detection",
        "description": "You are analyzing network logs. You see 50,000 packets per second arriving at your web server's Port 80. All of the packets have the 'SYN' flag set, but you see no 'ACK' packets being sent back by the attacker.\\n\\nTask: What specific type of attack is this, and what is its goal?",
        "difficulty": "Advanced",
        "starter_code": "Attack Type: \\nGoal: ",
        "solution_code": "Attack Type: SYN Flood (a type of DDoS attack).\\nGoal: To exhaust the server's memory by leaving thousands of TCP handshakes half-open, causing the server to crash and denying service to legitimate users.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Attack Type: SYN Flood (a type of DDoS attack).\\nGoal: To exhaust the server's memory by leaving thousands of TCP handshakes half-open, causing the server to crash and denying service to legitimate users."}]
    },
    {
        "title": "Challenge: Egress Traffic",
        "description": "Your firewall blocks all INBOUND traffic except Port 443. However, you notice a strange outbound connection originating from your web server, attempting to connect to an unknown IP address in another country on Port 4444.\\n\\nTask: What has likely happened to the web server, and what is this connection called in cybersecurity terms?",
        "difficulty": "Challenge",
        "starter_code": "What happened: \\nTerm: ",
        "solution_code": "What happened: The server has likely been compromised (infected with malware/rootkit). \\nTerm: The connection is a Reverse Shell (or Callback/C2 communication) where the victim server reaches out to the attacker's command and control server.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "What happened: The server has likely been compromised (infected with malware/rootkit). \\nTerm: The connection is a Reverse Shell (or Callback/C2 communication) where the victim server reaches out to the attacker's command and control server."}]
    }
]

m4_quizzes = [
    {
        "question_text": "What is a network Port?",
        "options": ["A physical hole in the back of the computer", "A logical endpoint that identifies a specific application or service on a computer", "An IP address assigned by a router", "A type of network cable"],
        "correct_answer": "A logical endpoint that identifies a specific application or service on a computer",
        "explanation": "Ports allow the Operating System to route incoming network packets to the correct running application.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "Which port is traditionally used for unencrypted HTTP web traffic?",
        "options": ["Port 22", "Port 443", "Port 80", "Port 3389"],
        "correct_answer": "Port 80",
        "explanation": "Port 80 is the standard for HTTP. Port 443 is the standard for encrypted HTTPS.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "What is the purpose of a 'Port Scan'?",
        "options": ["To encrypt data on a hard drive", "To check which logical doors (ports) on a target computer are open and listening for connections", "To improve internet download speeds", "To block viruses from entering the network"],
        "correct_answer": "To check which logical doors (ports) on a target computer are open and listening for connections",
        "explanation": "Attackers and defenders use port scanners (like Nmap) to discover what services a server is running.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "What is the primary difference between TCP and UDP?",
        "options": ["TCP is for video games; UDP is for web browsing", "TCP requires a handshake and guarantees delivery; UDP sends packets without checking if they arrive", "TCP is less secure than UDP", "UDP uses IP addresses; TCP uses MAC addresses"],
        "correct_answer": "TCP requires a handshake and guarantees delivery; UDP sends packets without checking if they arrive",
        "explanation": "TCP is reliable and ordered. UDP is fast and connectionless.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "What protocol and port should a system administrator use to securely log into a Linux server via the command line over the internet?",
        "options": ["Telnet on Port 23", "FTP on Port 21", "SSH on Port 22", "HTTP on Port 80"],
        "correct_answer": "SSH on Port 22",
        "explanation": "Secure Shell (SSH) encrypts the connection, protecting credentials and commands. Telnet and FTP are unencrypted.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "In the TCP 3-Way Handshake, what is the correct sequence of packets?",
        "options": ["ACK, SYN, SYN-ACK", "SYN, SYN-ACK, ACK", "SYN, ACK, FIN", "GET, POST, ACK"],
        "correct_answer": "SYN, SYN-ACK, ACK",
        "explanation": "Client sends Synchronize (SYN), server replies with Synchronize-Acknowledge (SYN-ACK), client finishes with Acknowledge (ACK).",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "A firewall administrator notices that their internal database server (which should only talk to the internal web server) is accepting connections on Port 3306 from random IP addresses on the public internet. What is the appropriate action?",
        "options": ["Move the database to Port 3307 to hide it", "Configure the firewall to drop all internet traffic destined for Port 3306 on the database", "Install antivirus on the database", "Change the database password"],
        "correct_answer": "Configure the firewall to drop all internet traffic destined for Port 3306 on the database",
        "explanation": "Databases should never be exposed to the public internet. The firewall must block external access entirely.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "What is 'Egress Filtering'?",
        "options": ["Blocking bad traffic from coming into the network", "Filtering out spam emails", "Monitoring and restricting traffic leaving (going out of) the network to prevent malware from communicating with attackers", "Hiding IP addresses using NAT"],
        "correct_answer": "Monitoring and restricting traffic leaving (going out of) the network to prevent malware from communicating with attackers",
        "explanation": "Egress filtering prevents compromised internal machines from reaching out to hacker Command and Control (C2) servers.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "If you wanted to see the listening ports on your own Linux machine to ensure no unauthorized backdoors are running, which command would you use?",
        "options": ["ping", "nmap", "ss -tuln", "traceroute"],
        "correct_answer": "ss -tuln",
        "explanation": "`ss -tuln` (or `netstat -tuln`) lists all TCP/UDP ports currently listening on the local machine.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "A hacker wants to conduct a 'SYN Flood' DDoS attack. How does this attack abuse the TCP protocol?",
        "options": ["By sending massive video files over UDP", "By completing millions of full TCP connections to use up bandwidth", "By sending millions of SYN packets but never sending the final ACK, leaving the server's memory filled with half-open connections", "By guessing the SSH password repeatedly"],
        "correct_answer": "By sending millions of SYN packets but never sending the final ACK, leaving the server's memory filled with half-open connections",
        "explanation": "The server allocates memory for the connection when it receives a SYN. If the ACK never comes, that memory is tied up until it crashes.",
        "difficulty": "Advanced"
    }
]


m5_lesson = """# Linux Fundamentals for Security

## 1. What Is It?

Linux is a family of open-source Unix-like operating systems. Unlike Windows, which is heavily reliant on a graphical user interface (GUI), Linux is designed to be incredibly powerful and fast via the Command Line Interface (CLI)—the terminal.

In cyber security, Linux is the industry standard. The vast majority of the world's web servers, databases, and network appliances (like firewalls and routers) run on Linux. Furthermore, almost all professional hacking, penetration testing, and security analysis tools are built natively for Linux (e.g., Kali Linux or Parrot OS).

## 2. Why Do We Need It?

If you cannot navigate a Linux terminal, you cannot work in cyber security. 

**Example 1: The Attacker**
If an attacker compromises a web server, they don't get a nice desktop with a mouse pointer. They get a reverse shell—a black terminal screen with a blinking cursor. To steal data or move further into the network, they must type Linux commands.

**Example 2: The Defender**
When a company is breached, the Incident Response (IR) team logs into the Linux servers. They must use command-line tools to parse millions of lines of text logs instantly to find out exactly what the attacker did and when.

## 3. Where Is It Used?

- **Web Servers**: Over 70% of the top 10 million websites run on Linux (Apache, Nginx).
- **Cloud Computing**: AWS, Google Cloud, and Azure infrastructure is overwhelmingly Linux-based.
- **Offensive Security**: Penetration testers use specialized Linux distributions pre-loaded with hacking tools.
- **IoT Devices**: Smart TVs, home routers, and connected cameras run lightweight Linux versions.

## 4. How Does It Work?

1. **The Kernel**: The core of Linux. It talks to the hardware.
2. **The Shell**: The program that takes the commands you type in the terminal, interprets them, and passes them to the OS. The most common shell is `bash`.
3. **The File System**: In Windows, you have `C:\\` and `D:\\` drives. In Linux, everything starts at the Root, represented by a single forward slash `/`. Everything is a file or a folder branching off from `/`.
4. **Permissions**: Linux has a strict permission system. Every file is owned by a User and a Group, and has specific Read, Write, and Execute permissions.

## 5. Important Terminology

| Term | Meaning |
|------|---------|
| **Root** | The absolute super-administrator user in Linux (equivalent to SYSTEM/Admin in Windows). |
| **Terminal / CLI** | The text-based interface used to type commands. |
| **Shell (Bash)** | The program that interprets your terminal commands. |
| **Directory** | The Linux term for a folder. |
| **sudo** | "Superuser do". A command that temporarily grants a normal user Root privileges to execute a single command. |

## 6. Architecture / Diagram

```text
The Linux File System Hierarchy

/ (Root Directory)
├── bin/    (Essential command binaries like 'ls', 'cat')
├── etc/    (System configuration files - very important for security!)
├── home/   (Personal folders for normal users: /home/alice)
├── root/   (The personal home folder for the Root user)
├── var/    (Variable data, primarily system Logs in /var/log)
└── tmp/    (Temporary files, often abused by malware to store scripts)
```

## 7. Syntax / Commands / Configuration

Here are the absolute essential commands you must memorize:

```bash
pwd          # Print Working Directory (Where am I right now?)
ls           # List files in the current directory
ls -la       # List ALL files (including hidden ones) with detailed permissions
cd /etc      # Change Directory (move) into the /etc folder
cat file.txt # Read and print the entire contents of a file to the screen
grep "error" # Search for a specific word ("error") inside a file or output
chmod 777    # Change file permissions (777 gives everyone full access - dangerous!)
chown root   # Change the owner of a file to 'root'
```

## 8. Beginner Example

Imagine you are looking for a lost receipt in a giant filing cabinet.
In Windows, you would open file explorer, click through folders, and use the graphical search bar, which might take 3 minutes.

In Linux, you open the terminal and type:
`grep "Receipt" /home/alice/documents/*.txt`
In less than a millisecond, the shell searches every text file in the documents folder and prints out the exact lines containing the word "Receipt". This speed is why professionals use the terminal.

## 9. Real-World Example

**Situation**: A web server is hacked. The attacker wants to leave a "backdoor" program running so they can get back in later.
**Weakness**: The attacker found a folder `/tmp` that allows any user to write and execute files.
**Risk**: The attacker places `malware.sh` in `/tmp` and executes it.
**Detection**: A security analyst logs in and runs `ls -la /tmp`. They see a hidden file called `.malware.sh` owned by the `www-data` web user.
**Mitigation**: The analyst deletes the file using `rm /tmp/.malware.sh` and reconfigures the server so files in `/tmp` cannot be executed (using the `noexec` mount flag).

## 10. What Happens Internally? (Piping)

One of the most powerful features in Linux is the **Pipe** (`|`). 

Internally, when a Linux command finishes, it outputs text (called Standard Output). A pipe takes the output of the command on the left, and literally feeds it as the input to the command on the right.

`cat /var/log/auth.log | grep "Failed password" | wc -l`

1. `cat` reads the massive 5-gigabyte authentication log.
2. The pipe `|` sends that text to `grep`.
3. `grep` filters out everything except lines containing "Failed password".
4. The pipe `|` sends those filtered lines to `wc -l` (word count -lines).
5. The terminal prints `4521`, telling you instantly that there were 4,521 failed login attempts.

## 11. Common Mistakes

1. **Running everything as Root**: Logging in as Root means any typo you make, or any script you run, has the power to instantly delete the entire OS (`rm -rf /`).
2. **Using `chmod 777` to fix permission errors**: If an application complains it can't read a file, lazy developers often run `chmod 777 file`. This grants Read, Write, and Execute permissions to *literally everyone on the system*, including attackers.
3. **Ignoring hidden files**: In Linux, any file that starts with a dot (e.g., `.secret`) is hidden from the standard `ls` command. Attackers hide their malware by simply putting a dot in front of the name.
4. **Not checking command history**: Linux saves everything you type in `~/.bash_history`. If you type a password directly into a command, it is saved in plain text in this file.

## 12. Defensive Best Practices

1. **Disable direct Root login**: Configure SSH so that nobody can log directly into the server as Root. They must log in as a normal user and use `sudo`, leaving an audit trail.
2. **Review `/etc/passwd` and `/etc/shadow`**: Regularly check these files to ensure no unauthorized users have been created.
3. **Monitor the logs**: The `/var/log` directory is the defender's best friend. Set up tools to automatically parse these logs for suspicious activity.
4. **Enforce Least Privilege**: Use `chmod` and `chown` meticulously. A web server process should only be able to read the web files, not the system configuration files.

## 13. Security Mindset

When looking at a Linux system, ask:
- *What user am I currently running as? (`whoami`)*
- *What files in this directory are hidden? (`ls -la`)*
- *If I am an attacker trying to hide a malicious script, where are the folders that allow anyone to write to them? (usually `/tmp` or `/dev/shm`)*
- *Are there any files here that have the 'execute' permission that shouldn't?*

## 14. Try It Yourself

If you are using LEARNX's terminal emulator (or a Linux VM/WSL):
1. Type `pwd` to see where you are.
2. Type `mkdir secret_folder` to create a directory.
3. Type `cd secret_folder` to enter it.
4. Type `echo "This is confidential" > data.txt` to create a file with text in it.
5. Type `cat data.txt` to read it back.
Congratulations, you are using the Linux terminal!
"""

m5_exercises = [
    {
        "title": "Concept Check: Linux File System",
        "description": "In Windows, the core system files are stored in `C:\\Windows`. \\n\\nTask: In Linux, what is the absolute path to the directory that stores the core system configuration files (like password rules and network settings)?",
        "difficulty": "Beginner",
        "starter_code": "Path: ",
        "solution_code": "/etc",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "/etc"}]
    },
    {
        "title": "Guided Lab: Finding Hidden Files",
        "description": "An attacker dropped malware in the `/tmp` directory. When you run `ls /tmp`, you see nothing.\\n\\nTask: What exact command and flag must you run to see all files, including hidden ones, with their detailed permissions?",
        "difficulty": "Beginner",
        "starter_code": "Command: ",
        "solution_code": "ls -la",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "ls -la"}]
    },
    {
        "title": "Hands-on Task: Parsing Logs with Pipes",
        "description": "You suspect someone is trying to guess the SSH password for your server. The log file is located at `/var/log/auth.log`.\\n\\nTask: Write the piped Linux command to print the contents of the log file, and filter it to show only lines containing the word 'Failed'.",
        "difficulty": "Intermediate",
        "starter_code": "Command: ",
        "solution_code": "cat /var/log/auth.log | grep \"Failed\"",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "cat /var/log/auth.log | grep \"Failed\""}]
    },
    {
        "title": "Scenario Analysis: The Lazy Developer",
        "description": "A developer couldn't get their web application to upload images to the `uploads/` directory due to a permissions error. To 'fix' it quickly, they ran: `chmod 777 uploads/`\\n\\nTask: Thinking like an attacker who compromised the web server, what can you now do to that `uploads/` directory that you couldn't do before?",
        "difficulty": "Intermediate",
        "starter_code": "Analysis: ",
        "solution_code": "The attacker can now WRITE and EXECUTE files in that directory. They can upload a malicious script (like a reverse shell) and execute it, taking total control of the server.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "The attacker can now WRITE and EXECUTE files in that directory. They can upload a malicious script (like a reverse shell) and execute it, taking total control of the server."}]
    },
    {
        "title": "Debugging Task: Sudo Abuse",
        "description": "You are auditing a server. You look in the `/etc/sudoers` file and see the following line:\\n`alice ALL=(ALL:ALL) NOPASSWD: ALL`\\n\\nTask: What does this configuration allow the user 'alice' to do, and why is it a massive security risk?",
        "difficulty": "Advanced",
        "starter_code": "What it does: \\nRisk: ",
        "solution_code": "What it does: It allows Alice to run any command as Root without being prompted for a password.\\nRisk: If Alice's account is compromised, the attacker instantly has full Root privileges to destroy the server without needing to crack her password.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "What it does: It allows Alice to run any command as Root without being prompted for a password.\\nRisk: If Alice's account is compromised, the attacker instantly has full Root privileges to destroy the server without needing to crack her password."}]
    },
    {
        "title": "Challenge: Command History Theft",
        "description": "An attacker gains access as a standard user. They immediately type `cat ~/.bash_history`. \\n\\nTask: What is the attacker hoping to find in this file, and what mistake would a system administrator have made to allow this to be successful?",
        "difficulty": "Challenge",
        "starter_code": "Hoping to find: \\nAdmin mistake: ",
        "solution_code": "Hoping to find: Plain text passwords or sensitive API keys.\\nAdmin mistake: The admin typed a password or key directly into a command (like `mysql -u root -pPassword123`) instead of using a secure prompt, causing it to be saved in the command history log.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Hoping to find: Plain text passwords or sensitive API keys.\\nAdmin mistake: The admin typed a password or key directly into a command (like `mysql -u root -pPassword123`) instead of using a secure prompt, causing it to be saved in the command history log."}]
    }
]

m5_quizzes = [
    {
        "question_text": "In Linux, what is the 'Root' user?",
        "options": ["A user who only has access to the `/root` folder", "A guest account with no privileges", "The absolute super-administrator with unrestricted access to the entire operating system", "The user account used specifically for running web servers"],
        "correct_answer": "The absolute super-administrator with unrestricted access to the entire operating system",
        "explanation": "Root is the equivalent of the SYSTEM/Administrator account in Windows. Gaining Root is the ultimate goal of an attacker.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "You open a Linux terminal and want to know exactly which directory you are currently sitting in. Which command do you use?",
        "options": ["ls", "pwd", "cd", "whereami"],
        "correct_answer": "pwd",
        "explanation": "`pwd` stands for Print Working Directory.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "An attacker creates a malicious script but wants to hide it from a normal `ls` command. How do they name the file in Linux to make it hidden?",
        "options": ["hidden_malware.sh", "-malware.sh", ".malware.sh", "*malware.sh"],
        "correct_answer": ".malware.sh",
        "explanation": "In Linux, any file or directory name that begins with a period (.) is considered hidden by the OS.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "Which directory in the Linux file system hierarchy is primarily used to store variable data, such as system logs that security analysts need to review?",
        "options": ["/etc", "/bin", "/tmp", "/var"],
        "correct_answer": "/var",
        "explanation": "The `/var` directory holds variable data. Log files are specifically kept in `/var/log`.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "What does the pipe character (`|`) do in a Linux terminal?",
        "options": ["It stops a command from running", "It takes the output of the command on the left and feeds it as the input to the command on the right", "It creates a backup of a file", "It grants Root privileges"],
        "correct_answer": "It takes the output of the command on the left and feeds it as the input to the command on the right",
        "explanation": "Piping allows you to chain commands together, such as `cat file.txt | grep error`.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "A junior developer runs `chmod 777 sensitive_database_config.php`. Why is the security team extremely angry?",
        "options": ["It deleted the file", "It encrypted the file so the web server can't read it", "It granted Read, Write, and Execute permissions to every single user on the system", "It changed the owner of the file to Root"],
        "correct_answer": "It granted Read, Write, and Execute permissions to every single user on the system",
        "explanation": "777 means full permissions for the Owner, the Group, and 'Others' (everyone else). It is a massive security risk.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "If a security analyst wants to search through a massive log file to find any line containing the IP address '192.168.1.50', which command should they use?",
        "options": ["grep '192.168.1.50' access.log", "cat access.log > 192.168.1.50", "find access.log", "ls access.log"],
        "correct_answer": "grep '192.168.1.50' access.log",
        "explanation": "Grep is the standard tool for searching text using patterns or exact string matches.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "Why do security best practices recommend disabling direct Root login via SSH?",
        "options": ["Because Root passwords expire too quickly", "To force administrators to log in as themselves and use `sudo`, which leaves an audit trail of exactly who executed the privileged command", "Because Root login slows down the network", "Because Root is not allowed to use SSH by default"],
        "correct_answer": "To force administrators to log in as themselves and use `sudo`, which leaves an audit trail of exactly who executed the privileged command",
        "explanation": "Accountability is key. If multiple admins share the Root password, you don't know who broke the server. If they use `sudo`, it is logged under their personal username.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "Which configuration file in Linux contains the system's user accounts and is often checked by defenders to see if a hacker created a backdoor account?",
        "options": ["/var/log/auth.log", "/etc/passwd", "/bin/bash", "/tmp/users.txt"],
        "correct_answer": "/etc/passwd",
        "explanation": "`/etc/passwd` lists all user accounts on the system. (The actual hashed passwords are stored securely in `/etc/shadow`).",
        "difficulty": "Advanced"
    },
    {
        "question_text": "A hacker gains low-level access to a server and wants to compile a C program to exploit the kernel. They need a place where any user can write and execute files. Which directory do they typically target first?",
        "options": ["/etc", "/root", "/var", "/tmp"],
        "correct_answer": "/tmp",
        "explanation": "The `/tmp` directory is designed for temporary files and usually has 'write' permissions for all users, making it a favorite staging ground for malware.",
        "difficulty": "Advanced"
    }
]


m6_lesson = """# Windows Security Fundamentals

## 1. What Is It?

While Linux dominates the server and cloud world, Microsoft Windows absolutely dominates the corporate desktop and enterprise environment. When an employee opens a malicious email attachment, the machine being compromised is almost always running Windows.

Windows security fundamentals revolve around understanding how Windows manages users, permissions, processes, and a massive internal database called the **Windows Registry**. Because Windows was originally designed for user convenience rather than strict security (unlike Unix/Linux), Microsoft has spent decades retrofitting complex security boundaries into the OS.

## 2. Why Do We Need It?

If you want to be a penetration tester or a SOC (Security Operations Center) analyst, you will spend a vast amount of time attacking or defending Windows environments.

**Example 1: Ransomware**
When ransomware hits a corporate network, it abuses Windows specific features (like SMB file sharing and Active Directory) to spread from one accountant's laptop to every single computer in the building in minutes.

**Example 2: Endpoint Detection**
To detect a hacker on a laptop, a defender must know how to read Windows Event Logs, analyze Windows Services, and spot malicious modifications in the Windows Registry.

## 3. Where Is It Used?

- **Enterprise Endpoints**: The millions of laptops and desktops used by employees globally.
- **Active Directory (AD)**: The centralized identity management system used by 95% of Fortune 500 companies to manage all Windows computers in their network.
- **Malware Analysis**: The vast majority of malware in the wild is written specifically to target Windows architectures (PE files - `.exe`, `.dll`).

## 4. How Does It Work?

1. **NTFS (New Technology File System)**: The file system Windows uses. It supports complex permissions called ACLs (Access Control Lists), which dictate exactly who can read or write a file.
2. **The Windows Registry**: The central nervous system of Windows. It is a massive hierarchical database that stores configuration settings for the OS, the hardware, and every installed application.
3. **Processes and Services**: Like Linux, Windows runs programs in RAM as processes. However, Windows relies heavily on **Services**—background programs that run silently (often as the `SYSTEM` user) to handle things like networking or printing.
4. **UAC (User Account Control)**: The prompt that pops up asking "Do you want to allow this app to make changes to your device?" It acts as a barrier, forcing a user to explicitly grant Administrator privileges to a process.

## 5. Important Terminology

| Term | Meaning |
|------|---------|
| **SYSTEM** | The highest-privileged built-in account in Windows (higher than Administrator). |
| **Active Directory (AD)** | A centralized database used to manage users and computers across a corporate network. |
| **Windows Registry** | The central configuration database for the OS and applications. |
| **UAC** | User Account Control. A security boundary preventing unauthorized privilege elevation. |
| **Event Viewer** | The built-in Windows tool used to view system, security, and application logs. |
| **SMB** | Server Message Block. The protocol Windows uses to share files over a network. |

## 6. Architecture / Diagram

```text
The Windows Security Boundary

[ Standard User Account ]
          |
    (Runs application)
          |
    +-----------+
    |  Browser  | (Runs with Standard privileges)
    +-----------+
          |
 (Malware tries to modify C:\\Windows)
          |
    [ UAC Prompt ] ---- (Blocks action unless Admin approves)
          |
    [ OS Kernel ]  ---- (Enforces NTFS Permissions)
          |
[ Protected System Files ]
```

## 7. Syntax / Commands / Configuration

In modern Windows, administrators and security professionals use **PowerShell**, a highly advanced command-line shell and scripting language.

```powershell
# View running processes
Get-Process

# View local user accounts
Get-LocalUser

# View recent Security Event Logs (e.g., failed logins)
Get-EventLog -LogName Security -Newest 10

# Check network connections
netstat -ano
```

## 8. Beginner Example

Think of the **Windows Registry** like the control panel of an airplane. 
Every switch and dial (startup programs, wallpaper settings, firewall rules) is stored here. 
If an attacker wants to ensure their malware runs every time the computer turns on (called "Persistence"), they don't need to put the malware in a special startup folder. They just add a new "switch" to the Registry telling Windows to execute `malware.exe` on boot. 

Defenders constantly monitor the Registry for unauthorized changes.

## 9. Real-World Example

**Situation**: An attacker compromises an HR employee's laptop via a phishing email.
**Weakness**: The employee uses the same password for their local laptop account and their Domain Admin account.
**Risk**: The attacker dumps the passwords from the laptop's memory and uses them to log into the central Domain Controller (Active Directory).
**Detection**: The Windows Event Logs on the Domain Controller register a `Logon Type 3` (Network Logon) from the HR laptop using Admin credentials at 3:00 AM.
**Mitigation**: The organization enforces "Tiered Administration" in Active Directory, strictly preventing high-privilege IT accounts from ever logging into standard employee laptops, meaning their passwords can never be stolen from those laptops.

## 10. What Happens Internally? (Windows Authentication)

When you log into a corporate Windows machine, you aren't just checking a local file (like `/etc/passwd` in Linux). 

Windows heavily uses protocols like **Kerberos** or **NTLM** for authentication across the network. 
1. The laptop takes your password, encrypts it (creates a hash), and sends an authentication request to the central server (Domain Controller).
2. The server verifies the hash and issues a "Ticket".
3. Your laptop uses this Ticket to prove to other servers (like the file server or email server) that you are authorized, so you don't have to type your password 50 times a day (Single Sign-On).

*Security Note: Attackers love stealing these Tickets from RAM (using tools like Mimikatz) to perform "Pass-the-Ticket" attacks, allowing them to impersonate you without ever needing your actual password.*

## 11. Common Mistakes

1. **Disabling UAC**: Users get annoyed by the pop-ups and turn UAC off. This completely removes the barrier between a standard application and administrative control, allowing malware to silently take over.
2. **Leaving SMB exposed**: Exposing Port 445 (SMB File Sharing) to the internet. This is exactly how the devastating WannaCry ransomware spread globally.
3. **Ignoring Event Logs**: Windows logs everything, but if nobody is collecting and reading those logs, a hacker can live on the network for months undetected.
4. **Local Admin Rights**: Giving every employee "Local Administrator" rights on their company laptop so they can install their own software. This guarantees that any malware they click on runs with Admin rights.

## 12. Defensive Best Practices

1. **Remove Local Admin Rights**: Standard users should never operate as Local Administrators.
2. **Enable LAPS (Local Administrator Password Solution)**: If IT needs a local admin account on every laptop for emergencies, LAPS ensures every single laptop has a unique, randomly generated, rotating password, preventing lateral movement.
3. **Forward Event Logs**: Don't leave the security logs on the laptop. If it gets hacked, the attacker will just clear the logs. Forward them immediately to a central, secure SIEM (Security Information and Event Management) server.
4. **Harden the Registry**: Use Group Policy Objects (GPOs) to push strict Registry configurations to all machines, disabling dangerous legacy protocols (like NTLMv1 or SMBv1).

## 13. Security Mindset

When analyzing a compromised Windows machine, ask:
- *What processes are running as `SYSTEM`?*
- *What programs are set to run automatically at startup via the Registry?*
- *Did the attacker clear the Security Event Logs? (Event ID 1102 - The audit log was cleared is a massive red flag).*
- *Are there any hidden accounts added to the 'Administrators' group?*

## 14. Try It Yourself

If you are on a Windows machine:
1. Press `Win + R`, type `eventvwr.msc` and press Enter to open the Event Viewer.
2. Expand "Windows Logs" and click on "Security".
3. Look at the sheer volume of logs generated just by turning the computer on and logging in. 
4. Imagine trying to find a single hacker's login among 50,000 legitimate logs. This is why defenders write automated rules and use SIEMs!
"""

m6_exercises = [
    {
        "title": "Concept Check: Windows Registry",
        "description": "Task: What is the name of the central hierarchical database in Windows that stores configuration settings for the OS and applications, often used by malware for persistence?",
        "difficulty": "Beginner",
        "starter_code": "Database Name: ",
        "solution_code": "Windows Registry",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Windows Registry"}]
    },
    {
        "title": "Guided Lab: Highest Privilege",
        "description": "In Linux, the highest privilege account is `root`.\\n\\nTask: In Windows, what is the built-in account that has even higher privileges than the 'Administrator' account, and is often used by core OS services?",
        "difficulty": "Beginner",
        "starter_code": "Account: ",
        "solution_code": "SYSTEM (or NT AUTHORITY\\SYSTEM)",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "SYSTEM (or NT AUTHORITY\\SYSTEM)"}]
    },
    {
        "title": "Hands-on Task: UAC Analysis",
        "description": "A user downloads a fake Flash Player update. They double-click it. The screen dims, and a prompt asks: 'Do you want to allow this app to make changes to your device?'\\n\\nTask: What is the acronym for this specific security feature, and what happens if the user clicks 'No'?",
        "difficulty": "Intermediate",
        "starter_code": "Acronym: \\nIf 'No': ",
        "solution_code": "Acronym: UAC (User Account Control)\\nIf 'No': The application is denied administrative privileges and fails to execute the system-level changes (stopping the malware installation).",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Acronym: UAC (User Account Control)\\nIf 'No': The application is denied administrative privileges and fails to execute the system-level changes (stopping the malware installation)."}]
    },
    {
        "title": "Scenario Analysis: Active Directory Risk",
        "description": "A company uses Active Directory. The IT Administrator logs into an infected receptionist's laptop using their Domain Admin account to fix a printer issue. \\n\\nTask: Explain why this is a massive security failure, and what the malware on the laptop can now do.",
        "difficulty": "Intermediate",
        "starter_code": "Analysis: ",
        "solution_code": "Failure: High-privilege accounts should never log into untrusted/low-tier machines. \\nResult: The malware can scrape the Domain Admin's password hash or Kerberos ticket directly from the laptop's RAM and use it to take over the entire corporate network.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Failure: High-privilege accounts should never log into untrusted/low-tier machines. \\nResult: The malware can scrape the Domain Admin's password hash or Kerberos ticket directly from the laptop's RAM and use it to take over the entire corporate network."}]
    },
    {
        "title": "Debugging Task: Event Log Clearing",
        "description": "You are a SOC analyst. You receive an alert for 'Windows Event ID 1102: The audit log was cleared' from a production database server at 2:00 AM.\\n\\nTask: Why is this specific event considered one of the highest severity alerts a defender can receive?",
        "difficulty": "Advanced",
        "starter_code": "Reason: ",
        "solution_code": "Reason: Legitimate administrators rarely, if ever, manually clear the security logs. This event almost always indicates an attacker is currently on the machine attempting to destroy the forensic evidence of their intrusion.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Reason: Legitimate administrators rarely, if ever, manually clear the security logs. This event almost always indicates an attacker is currently on the machine attempting to destroy the forensic evidence of their intrusion."}]
    },
    {
        "title": "Challenge: Pass-the-Ticket",
        "description": "An attacker uses a tool like Mimikatz to extract a Kerberos Ticket-Granting Ticket (TGT) from the memory of a compromised Windows machine.\\n\\nTask: How does this allow the attacker to impersonate the user without ever running a password-cracking program?",
        "difficulty": "Challenge",
        "starter_code": "Explanation: ",
        "solution_code": "Explanation: Windows uses the Ticket itself to grant access to network resources. The attacker simply injects the stolen ticket into their own session, effectively bypassing the need to ever know or type the actual password (Single Sign-On abuse).",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Explanation: Windows uses the Ticket itself to grant access to network resources. The attacker simply injects the stolen ticket into their own session, effectively bypassing the need to ever know or type the actual password (Single Sign-On abuse)."}]
    }
]

m6_quizzes = [
    {
        "question_text": "What is the primary function of Active Directory (AD) in a corporate Windows environment?",
        "options": ["To act as the local firewall on a laptop", "To provide a centralized database for managing users, computers, and security policies across the entire network", "To scan for viruses", "To manage the physical memory (RAM)"],
        "correct_answer": "To provide a centralized database for managing users, computers, and security policies across the entire network",
        "explanation": "Active Directory allows IT to manage thousands of computers from a single central server (Domain Controller).",
        "difficulty": "Beginner"
    },
    {
        "question_text": "Which built-in Windows tool is used by defenders to review system, security, and application logs (such as failed login attempts)?",
        "options": ["Task Manager", "Windows Registry", "Event Viewer", "Command Prompt"],
        "correct_answer": "Event Viewer",
        "explanation": "Event Viewer reads the `.evtx` log files that Windows constantly generates to track system activity.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "An attacker wants their malware to run automatically every time the infected Windows computer reboots. Where is the most common place they will add a configuration setting to achieve this?",
        "options": ["The C:\\ drive root", "The Windows Registry", "The Recycle Bin", "The Event Viewer"],
        "correct_answer": "The Windows Registry",
        "explanation": "The Registry contains 'Run' keys that tell Windows which programs to start on boot. Attackers abuse this for persistence.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "What is the purpose of User Account Control (UAC) in modern Windows?",
        "options": ["To encrypt user files", "To prevent a standard application or script from silently elevating its privileges to Administrator without explicit human approval", "To manage network bandwidth", "To block spam emails"],
        "correct_answer": "To prevent a standard application or script from silently elevating its privileges to Administrator without explicit human approval",
        "explanation": "UAC acts as a physical barrier. Even if you are logged in as an Admin, applications run as Standard users until you click 'Yes' on the UAC prompt.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "Which Windows protocol operates on Port 445 and is used for network file sharing, but is also highly targeted by ransomware (like WannaCry) to spread across a network?",
        "options": ["HTTP", "SSH", "SMB (Server Message Block)", "FTP"],
        "correct_answer": "SMB (Server Message Block)",
        "explanation": "SMB is essential for Windows file sharing, but vulnerabilities in SMB have been responsible for the worst ransomware worms in history.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "Which of the following describes a 'Pass-the-Ticket' attack?",
        "options": ["Guessing a user's password repeatedly until it works", "Stealing a Kerberos authentication ticket directly from the computer's RAM and using it to impersonate the user without knowing their password", "Emailing a fake concert ticket to an employee", "Bypassing a physical security turnstile"],
        "correct_answer": "Stealing a Kerberos authentication ticket directly from the computer's RAM and using it to impersonate the user without knowing their password",
        "explanation": "Pass-the-Ticket (PtT) abuses how Windows handles Single Sign-On (SSO) by stealing the cryptographic tickets from memory.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "In Windows, what is the `SYSTEM` account (NT AUTHORITY\\SYSTEM)?",
        "options": ["A guest account", "A standard user account", "The highest-privileged built-in service account, possessing more power over the local machine than the Administrator account", "An account used only for updating Windows"],
        "correct_answer": "The highest-privileged built-in service account, possessing more power over the local machine than the Administrator account",
        "explanation": "The SYSTEM account runs core OS services. If an attacker gains SYSTEM privileges, they own the machine completely.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "Why is giving all employees 'Local Administrator' rights on their company laptops considered a terrible security practice?",
        "options": ["It makes the laptops run slower", "It costs more in licensing fees", "If the employee accidentally clicks on a malicious link, the malware executes with those same Administrator rights and can permanently compromise the machine", "It prevents them from accessing the internet"],
        "correct_answer": "If the employee accidentally clicks on a malicious link, the malware executes with those same Administrator rights and can permanently compromise the machine",
        "explanation": "Operating at Least Privilege (Standard User) prevents malware from installing itself deeply into the OS.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "A SOC analyst notices that a user's machine generated 'Event ID 1102: The audit log was cleared'. What should the analyst assume?",
        "options": ["Windows is performing routine maintenance", "The hard drive is full", "An attacker has likely compromised the machine and is deleting the logs to hide their tracks", "The user forgot their password"],
        "correct_answer": "An attacker has likely compromised the machine and is deleting the logs to hide their tracks",
        "explanation": "Clearing the security logs is highly anomalous behavior and a classic anti-forensics technique used by hackers.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "What is the purpose of LAPS (Local Administrator Password Solution) in a corporate Windows environment?",
        "options": ["To force users to have passwords with at least 8 characters", "To randomly generate and rotate a unique local Administrator password for every single computer, preventing attackers from using one stolen password to access every machine", "To encrypt the hard drive", "To store passwords in the cloud"],
        "correct_answer": "To randomly generate and rotate a unique local Administrator password for every single computer, preventing attackers from using one stolen password to access every machine",
        "explanation": "LAPS prevents lateral movement. If an attacker steals the local admin password from Laptop A, they cannot use it to log into Laptop B.",
        "difficulty": "Advanced"
    }
]


m7_lesson = """# CIA Triad, Threats, Vulnerabilities & Risk

## 1. What Is It?

In Phase 1, you learned the technical foundations of computers, networks, and operating systems. Now, in Phase 2, we apply core security theory to those foundations.

The absolute core of all security theory is the **CIA Triad**: Confidentiality, Integrity, and Availability. Every piece of hardware, every line of code, and every security policy exists to protect one or more of these three pillars.

To understand *what* threatens the CIA Triad, we use a specific formula:
**Risk = Threat × Vulnerability × Impact**

A **Vulnerability** is a weakness (a missing patch, a bad password, an unlocked door).
A **Threat** is a malicious actor or event that exploits that weakness (a hacker, ransomware, a flood).
**Risk** is the overall danger to the business if the Threat succeeds.

## 2. Why Do We Need It?

Security professionals cannot protect everything perfectly; they have limited time and budget. The CIA Triad and the Risk equation allow defenders to prioritize their efforts.

**Example 1: Prioritizing Vulnerabilities**
If a vulnerability scan finds 10,000 missing patches on a network, which one do you fix first? You use Risk analysis. You fix the vulnerability that allows a highly likely Threat to cause a massive Impact to Confidentiality.

**Example 2: The CIA Trade-off**
You cannot have maximum Confidentiality and maximum Availability simultaneously. If you unplug a server and bury it in concrete, Confidentiality is perfect, but Availability is zero. Security is about balancing the triad.

## 3. Where Is It Used?

- **Risk Assessments**: Security consultants evaluate corporate networks to determine their overall Risk score.
- **Threat Modeling**: Software engineers analyze their applications *before* writing code to identify potential vulnerabilities.
- **Incident Response**: When a breach happens, analysts immediately assess which pillar of the CIA Triad was compromised to determine the legal and technical response.

## 4. How Does It Work?

**1. Confidentiality (Secrecy)**
Ensuring data is accessible only to authorized people.
*How it's enforced*: Encryption, Passwords, Access Control Lists (ACLs), Biometrics.

**2. Integrity (Accuracy)**
Ensuring data has not been altered, tampered with, or corrupted.
*How it's enforced*: Hash functions, Digital Signatures, Read-only permissions, Backups.

**3. Availability (Uptime)**
Ensuring systems and data are available when needed.
*How it's enforced*: Redundant servers, Load balancers, Uninterruptible Power Supplies (UPS), DDoS protection.

## 5. Important Terminology

| Term | Meaning |
|------|---------|
| **Confidentiality** | Protecting data from unauthorized viewing. |
| **Integrity** | Protecting data from unauthorized modification. |
| **Availability** | Ensuring authorized users have access to data when needed. |
| **Threat Actor** | The person or entity carrying out the attack (e.g., Script Kiddie, APT, Insider Threat). |
| **APT** | Advanced Persistent Threat. Usually a highly funded, state-sponsored hacking group. |
| **Zero-Day** | A vulnerability that is unknown to the software vendor (the vendor has had "zero days" to fix it). |

## 6. Architecture / Diagram

```text
The Risk Matrix

                 |  High Risk    |  CRITICAL RISK |
    High Impact  | (Requires     | (Immediate     |
                 |  Attention)   |  Action)       |
                 +--------------------------------+
                 |  Low Risk     |  Medium Risk   |
    Low Impact   | (Acceptable)  | (Requires      |
                 |               |  Monitoring)   |
                 +--------------------------------+
                   Low Likelihood   High Likelihood
```

## 7. Syntax / Commands / Configuration

Risk is often calculated mathematically in enterprise environments using CVSS (Common Vulnerability Scoring System). When a new vulnerability is discovered, it is given a score from 0.0 to 10.0.

```text
# Example CVSS Score for the "Log4Shell" Vulnerability
CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H -> Score: 10.0 (CRITICAL)

Translation:
AV:N (Attack Vector: Network) - Attacker can exploit this from anywhere on the internet.
PR:N (Privileges Required: None) - Attacker doesn't need a password.
C:H, I:H, A:H (Confidentiality, Integrity, Availability Impact: HIGH) - Complete system takeover.
```

## 8. Beginner Example

Imagine a library.
- **Confidentiality**: The library keeps the list of "who checked out what book" private. Only the librarian can see it.
- **Integrity**: Nobody can sneak behind the desk and change the records to say someone else checked out a book.
- **Availability**: The library is open during its posted hours, and the catalog computer is turned on and working.

## 9. Real-World Example

**Situation**: A nation-state hacker (APT) wants to disrupt an enemy country's power grid.
**Weakness (Vulnerability)**: The power plant's industrial control systems use outdated software with no passwords.
**Threat**: The APT group, armed with custom malware.
**Risk**: CRITICAL. The likelihood is high, and the impact is a national blackout.
**CIA Violation**: The attackers deploy malware that shuts down the power generators. This is a massive attack on **Availability**.
**Mitigation**: The power plant is "air-gapped" (physically disconnected from the internet), completely eliminating the network vulnerability.

## 10. What Happens Internally? (Threat Modeling)

Internally, security teams use a process called **Threat Modeling** (like the STRIDE framework) to systematically identify risks in software.

- **S**poofing (Pretending to be someone else) -> Violates Authentication
- **T**ampering (Modifying data) -> Violates Integrity
- **R**epudiation (Claiming you didn't do something) -> Violates Non-repudiation
- **I**nformation Disclosure (Stealing data) -> Violates Confidentiality
- **D**enial of Service (Crashing the system) -> Violates Availability
- **E**levation of Privilege (Gaining admin rights) -> Violates Authorization

By mapping threats to the CIA triad, defenders know exactly which technical controls to build into the software.

## 11. Common Mistakes

1. **Focusing only on Confidentiality**: Encrypting a database (Confidentiality) is useless if an attacker can just delete the entire encrypted database (Availability).
2. **Ignoring Insider Threats**: Assuming all threats come from the outside internet. A disgruntled employee with valid credentials is often the most dangerous threat actor.
3. **Miscalculating Risk**: Spending $50,000 to implement a security control that protects a system only worth $10,000. Risk management dictates that the cost of the control must not exceed the value of the asset.
4. **Treating Vulnerability Scanning as Penetration Testing**: Running an automated tool that spits out a list of missing patches is not hacking. A true penetration test involves actually exploiting the vulnerabilities to demonstrate the real business risk.

## 12. Defensive Best Practices

1. **Risk Acceptance**: Sometimes, the correct security decision is to do nothing. If a vulnerability requires an attacker to have physical access to a highly guarded nuclear facility to exploit it, the likelihood is so low that the risk is "Accepted."
2. **Defense in Depth**: Always use multiple controls.
3. **Patch Management**: The absolute best way to reduce Risk is to reduce Vulnerabilities by keeping all software strictly updated.
4. **Data Classification**: You cannot protect what you don't know you have. Classify data (e.g., Public, Internal, Top Secret) and apply CIA controls accordingly.

## 13. Security Mindset

When analyzing a system's risk, ask:
- *What is the absolute worst thing that could happen if this system goes offline (Availability)?*
- *What happens if the data in this database is quietly changed by 1% (Integrity)?*
- *Who is the most likely Threat Actor targeting this system (Script Kiddie vs. Nation State), and what resources do they have?*

## 14. Try It Yourself

Perform a CVSS analysis mentally. You find a vulnerability in your personal blog. 
- To exploit it, the attacker must have physical access to your keyboard (Attack Vector = Physical). 
- If they exploit it, they can read your unpublished drafts (Confidentiality = Low).
Is this a High, Medium, or Low risk vulnerability? (Answer: Low Risk. Physical access is hard to achieve for a remote hacker, and the impact of reading a draft is negligible).
"""

m7_exercises = [
    {
        "title": "Concept Check: Identify the CIA Pillar",
        "description": "Read the scenario and identify which pillar of the CIA triad is primarily being protected.\\n\\nScenario: A hospital implements a strict policy that all patient medical records must be strongly encrypted before being transmitted over the internet to an insurance company.\\n\\nTask: Which pillar (Confidentiality, Integrity, or Availability) does encryption primarily protect?",
        "difficulty": "Beginner",
        "starter_code": "Pillar: ",
        "solution_code": "Confidentiality",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Confidentiality"}]
    },
    {
        "title": "Guided Lab: Threat Actors",
        "description": "Different Threat Actors have different motivations and skill levels.\\n\\nScenario: A bored teenager downloads a pre-made hacking tool from the internet and runs it against a random website just to see if it works, without really understanding the underlying code.\\n\\nTask: What is the standard industry term for this specific type of low-skill threat actor?",
        "difficulty": "Beginner",
        "starter_code": "Actor: ",
        "solution_code": "Script Kiddie",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Script Kiddie"}]
    },
    {
        "title": "Hands-on Task: The Risk Equation",
        "description": "Risk = Threat x Vulnerability x Impact.\\n\\nYou manage a server containing the secret recipe for Coca-Cola. The Impact of a breach is catastrophic (100). The server is vulnerable to the 'Heartbleed' bug (Vulnerability = High). However, the server is completely turned off, unplugged, and locked in a bank vault with no network connection.\\n\\nTask: Based on the risk equation, is the overall logical Risk High or Low? Explain why in one sentence.",
        "difficulty": "Intermediate",
        "starter_code": "Risk (High/Low): \\nReason: ",
        "solution_code": "Risk (High/Low): Low\\nReason: Because the server is physically unplugged and locked away, the Threat likelihood is near zero, which zeroes out the overall Risk equation.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Risk (High/Low): Low\\nReason: Because the server is physically unplugged and locked away, the Threat likelihood is near zero, which zeroes out the overall Risk equation."}]
    },
    {
        "title": "Scenario Analysis: Integrity Violation",
        "description": "A hacker breaches a university's database. Instead of stealing data or crashing the server, the hacker simply changes the grades of five students from 'F' to 'A'.\\n\\nTask: Explain why this is specifically an attack on Integrity rather than Confidentiality or Availability.",
        "difficulty": "Intermediate",
        "starter_code": "Analysis: ",
        "solution_code": "The attacker did not steal data (Confidentiality) or take the system offline (Availability). They unauthorizedly modified the data, destroying the accuracy and trustworthiness of the academic records, which is the definition of an Integrity violation.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "The attacker did not steal data (Confidentiality) or take the system offline (Availability). They unauthorizedly modified the data, destroying the accuracy and trustworthiness of the academic records, which is the definition of an Integrity violation."}]
    },
    {
        "title": "Debugging Task: Zero-Day Logic",
        "description": "The CEO asks you, 'We just spent $10 million on the best firewall and antivirus software. We are 100% safe from hackers now, right?'\\n\\nTask: Using the concept of a 'Zero-Day Vulnerability', write a 1-2 sentence response explaining why the CEO is factually incorrect.",
        "difficulty": "Advanced",
        "starter_code": "Response: ",
        "solution_code": "No, we are not 100% safe because attackers can use 'Zero-Day vulnerabilities'—flaws that are completely unknown to the software vendors and our antivirus signatures. Since no patch exists for a Zero-Day, even the best defenses can be bypassed, meaning we must maintain an 'Assume Breach' mindset.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "No, we are not 100% safe because attackers can use 'Zero-Day vulnerabilities'—flaws that are completely unknown to the software vendors and our antivirus signatures. Since no patch exists for a Zero-Day, even the best defenses can be bypassed, meaning we must maintain an 'Assume Breach' mindset."}]
    },
    {
        "title": "Challenge: Threat Modeling (STRIDE)",
        "description": "A developer writes a banking application. The application uses HTTP (unencrypted) to send passwords from the user's browser to the server.\\n\\nTask: Using the STRIDE threat model (Spoofing, Tampering, Repudiation, Information Disclosure, DoS, Elevation of Privilege), which specific threat does this unencrypted connection expose the users to, and which CIA pillar does it violate?",
        "difficulty": "Challenge",
        "starter_code": "STRIDE Threat: \\nCIA Pillar Violated: ",
        "solution_code": "STRIDE Threat: Information Disclosure (because anyone on the network can read the plain-text password).\\nCIA Pillar Violated: Confidentiality.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "STRIDE Threat: Information Disclosure (because anyone on the network can read the plain-text password).\\nCIA Pillar Violated: Confidentiality."}]
    }
]

m7_quizzes = [
    {
        "question_text": "What does the 'I' in the CIA Triad stand for?",
        "options": ["Intelligence", "Information", "Integrity", "Isolation"],
        "correct_answer": "Integrity",
        "explanation": "Integrity ensures data is accurate, trustworthy, and has not been modified by unauthorized parties.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "A massive Distributed Denial of Service (DDoS) attack takes an e-commerce website offline on Black Friday. Which pillar of the CIA Triad was successfully attacked?",
        "options": ["Confidentiality", "Integrity", "Availability", "Authentication"],
        "correct_answer": "Availability",
        "explanation": "Availability ensures systems are up and running when legitimate users need them. A DDoS attack destroys availability.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "Which of the following best defines a 'Vulnerability'?",
        "options": ["A highly skilled hacker", "A weakness or flaw in a system that can be exploited", "The financial cost of a data breach", "A piece of protective software like a firewall"],
        "correct_answer": "A weakness or flaw in a system that can be exploited",
        "explanation": "A vulnerability is the hole in the armor; a threat is the arrow that passes through it.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "In the risk equation (Risk = Threat × Vulnerability × Impact), if the Threat is zero (e.g., an entirely isolated offline system locked in a vault), what happens to the overall Risk?",
        "options": ["It increases", "It remains the same", "It drops to zero", "It doubles"],
        "correct_answer": "It drops to zero",
        "explanation": "If any multiplier in the equation is zero, the overall risk becomes negligible.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "What is an Advanced Persistent Threat (APT)?",
        "options": ["A teenager running an automated hacking script", "A computer virus that spreads via USB drives", "A highly organized, well-funded hacking group, typically state-sponsored, that maintains long-term covert access to a target", "A firewall misconfiguration"],
        "correct_answer": "A highly organized, well-funded hacking group, typically state-sponsored, that maintains long-term covert access to a target",
        "explanation": "APTs (like Cozy Bear or Lazarus Group) are the most dangerous threat actors, possessing immense resources and patience.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "A security analyst discovers a vulnerability in a popular web server. The software vendor is completely unaware of the flaw, meaning no security patch currently exists. What is this type of vulnerability called?",
        "options": ["A One-Day", "A Buffer Overflow", "A Zero-Day", "A Script Kiddie"],
        "correct_answer": "A Zero-Day",
        "explanation": "It is called a Zero-Day because the vendor has had zero days of notice to fix it before it could be exploited in the wild.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "In the STRIDE threat model, what does 'Tampering' refer to, and which CIA pillar does it violate?",
        "options": ["Stealing data; violates Confidentiality", "Modifying data; violates Integrity", "Crashing a server; violates Availability", "Guessing a password; violates Authorization"],
        "correct_answer": "Modifying data; violates Integrity",
        "explanation": "Tampering involves maliciously changing data on a disk, in memory, or in transit, directly destroying Integrity.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "A company realizes it would cost $100,000 to implement a security system to protect a server that is only worth $5,000 and contains no customer data. The company decides not to buy the security system. What is this risk management strategy called?",
        "options": ["Risk Mitigation", "Risk Transference", "Risk Acceptance", "Risk Ignorance"],
        "correct_answer": "Risk Acceptance",
        "explanation": "When the cost of the control exceeds the cost of the impact, organizations formally 'Accept' the risk.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "What is the primary difference between a Vulnerability Scan and a Penetration Test?",
        "options": ["A vulnerability scan is done manually; a pen test is automated", "A vulnerability scan is illegal; a pen test is legal", "A vulnerability scan automatedly identifies potential flaws; a pen test involves a human actively exploiting those flaws to prove the business risk", "They are exactly the same thing"],
        "correct_answer": "A vulnerability scan automatedly identifies potential flaws; a pen test involves a human actively exploiting those flaws to prove the business risk",
        "explanation": "Scanners just point out unlocked doors. Pen testers actually walk through the doors and see what they can steal.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "A disgruntled employee who already has legitimate administrative access to a company's database decides to steal the customer list and sell it to a competitor. What type of threat actor is this?",
        "options": ["Hacktivist", "Nation-State APT", "Insider Threat", "Script Kiddie"],
        "correct_answer": "Insider Threat",
        "explanation": "Insider threats are exceptionally dangerous because they already possess valid credentials and bypass the outer firewall defenses.",
        "difficulty": "Intermediate"
    }
]


m8_lesson = """# Authentication, Authorization & Cryptography

## 1. What Is It?

This module covers the core mechanisms we use to enforce the CIA Triad in computer systems.

**Authentication** is the process of verifying *who* you are.
**Authorization** is the process of determining *what you are allowed to do* after you have been authenticated.
**Cryptography** is the mathematical science of keeping data secure, ensuring that even if authentication and authorization fail, the data remains unreadable.

You cannot have a secure system without all three of these components working perfectly together.

## 2. Why Do We Need It?

Without these mechanisms, the internet would be a free-for-all where anyone could read anyone else's bank statements or send emails pretending to be the President.

**Example 1: The Email Login**
When you log into Gmail, you provide a password (Authentication). Google then uses internal rules (Authorization) to ensure you can only read *your* emails, not your neighbor's.

**Example 2: E-Commerce**
When you buy something on Amazon, you send your credit card number over the internet. Because the internet is fundamentally insecure (anyone can intercept packets), we use Cryptography (specifically TLS/SSL) to scramble the credit card number in transit so attackers cannot steal it.

## 3. Where Is It Used?

- **Websites (HTTPS)**: Uses cryptography to encrypt traffic between your browser and the web server.
- **Operating Systems**: Uses authentication (login screens) and authorization (file permissions).
- **Mobile Phones**: Uses biometrics (FaceID/Fingerprint) for authentication, and cryptography to encrypt the storage drive so thieves cannot read your data.
- **VPNs**: Uses cryptography to create a secure, private tunnel over public Wi-Fi.

## 4. How Does It Work?

**Authentication Factors**
Authentication requires you to present "factors". The three main types are:
1. *Something you know* (Password, PIN)
2. *Something you have* (Smartcard, Authenticator App on your phone)
3. *Something you are* (Fingerprint, Iris scan)
Using more than one type is called **Multi-Factor Authentication (MFA)**.

**Cryptography Basics**
Cryptography uses mathematics to scramble data. 
- **Plaintext**: The original, readable message ("Hello").
- **Ciphertext**: The scrambled, unreadable message ("XyZ123").
- **Encryption**: Turning Plaintext into Ciphertext using a secret **Key**.
- **Decryption**: Turning Ciphertext back into Plaintext using a Key.

## 5. Important Terminology

| Term | Meaning |
|------|---------|
| **Authentication** | Proving identity (Are you who you say you are?). |
| **Authorization** | Checking permissions (Are you allowed to do this?). |
| **MFA** | Multi-Factor Authentication. Requiring two or more different *types* of authentication factors. |
| **Plaintext / Ciphertext** | Readable text vs. Encrypted, unreadable text. |
| **Symmetric Encryption** | Uses the *same* key to encrypt and decrypt data (Fast, used for large data). |
| **Asymmetric Encryption** | Uses *two different keys* (Public Key and Private Key) to encrypt and decrypt. |

## 6. Architecture / Diagram

```text
The Authentication & Authorization Flow

[ User ] --- (1. Sends Username + Password) ---> [ Server ]
                                                     |
                                            (2. Verifies Password) -> AUTHENTICATION
                                                     |
                                           (3. Checks Role = User) -> AUTHORIZATION
                                                     |
                                (4. Grants access to /profile, denies /admin)
```

## 7. Syntax / Commands / Configuration

In modern systems, authentication is often handled by identity protocols like OAuth or SAML, while authorization is handled by RBAC (Role-Based Access Control).

```text
# Example RBAC Configuration (Authorization)

Role: User
Permissions: READ /own_profile, WRITE /own_profile

Role: Admin
Permissions: READ /all_profiles, WRITE /all_profiles, DELETE /users
```

## 8. Beginner Example

Think of going to a nightclub.
- **Authentication**: You hand your ID to the bouncer. The bouncer checks the picture and the birthdate to prove you are who you say you are, and you are over 21. 
- **Authorization**: Once inside, you try to walk into the VIP lounge. The VIP bouncer checks your wristband. You don't have the VIP wristband, so you are denied access. You were authenticated (allowed in the club), but not authorized (allowed in the VIP area).

## 9. Real-World Example

**Situation**: A hospital stores patient records in a database.
**Weakness**: The database uses single-factor authentication (just a password) and lacks RBAC (all logged-in users have full admin rights).
**Threat**: A phisher steals a receptionist's password.
**Risk**: The attacker logs in, and because the authorization is broken, the receptionist's account allows the attacker to download and delete the entire hospital database.
**Mitigation**: The hospital implements MFA (requiring an app on the user's phone). They also implement strict RBAC, so a receptionist's account only has the authorization to READ the schedule, but absolutely zero authorization to DELETE records.

## 10. What Happens Internally? (Asymmetric Cryptography)

Symmetric encryption is fast, but it has a huge problem: If Alice and Bob want to talk securely, they have to share the secret Key. If a hacker intercepts the Key while they share it, the encryption is useless.

**Asymmetric Cryptography** (Public Key Cryptography) solves this. It uses a mathematical pair of keys: a **Public Key** and a **Private Key**. 
- You can give your Public Key to the entire world.
- You keep your Private Key absolutely secret.
- **The Magic Rule**: Anything encrypted with the Public Key can *only* be decrypted by the matching Private Key.

If Bob wants to send Alice a secret message:
1. Bob gets Alice's Public Key.
2. Bob encrypts the message using Alice's Public Key.
3. Bob sends the Ciphertext over the internet.
4. Alice receives it and decrypts it using her Private Key. (Even if Bob intercepted his own ciphertext, he couldn't decrypt it!).

## 11. Common Mistakes

1. **Confusing Authentication and Authorization**: Believing that just because a user is logged in, they are safe to trust.
2. **"Rolling your own crypto"**: Developers trying to write their own encryption algorithms instead of using proven industry standards (like AES-256). Amateur cryptography is always broken easily.
3. **MFA Bypass**: Using SMS text messages for MFA. Attackers can perform "SIM Swapping" to steal a user's phone number and intercept the SMS codes. Authenticator apps (like Authy or Google Authenticator) are much safer.
4. **Hardcoding Keys**: Developers leaving the secret encryption keys directly in the application's source code, which attackers can easily extract.

## 12. Defensive Best Practices

1. **Enforce MFA Everywhere**: Passwords are dead. Any system accessible from the internet must require MFA.
2. **Implement RBAC (Role-Based Access Control)**: Assign permissions to Roles (e.g., 'Manager', 'Cashier'), and assign users to those roles. Do not assign permissions directly to users.
3. **Use Industry Standard Cryptography**: Use AES for symmetric encryption, RSA or ECC for asymmetric encryption, and TLS 1.3 for network traffic.
4. **Zero Trust Architecture**: Never trust a user or device just because they are inside the corporate network. Continuously authenticate and authorize every single request.

## 13. Security Mindset

When evaluating a login portal, ask:
- *Is the traffic encrypted (HTTPS)? If not, I can just sniff the password off the Wi-Fi.*
- *Does it require MFA? If not, a stolen password is all I need.*
- *Once I log in as a normal user, what happens if I manually change the URL from `/user/profile` to `/admin/dashboard`? Does the server actually verify my Authorization on the backend, or did it just hide the button?*

## 14. Try It Yourself

Look at your smartphone lock screen. 
1. If you use a PIN, you are using "Something you know".
2. If you use FaceID or a fingerprint, you are using "Something you are".
3. Consider: If a police officer or a thief forces you to look at your phone, FaceID will unlock it. If you use a PIN, they cannot force your mind to reveal the numbers. This is an example of the complex legal and security trade-offs of authentication factors.
"""

m8_exercises = [
    {
        "title": "Concept Check: Authentication Factors",
        "description": "Multi-Factor Authentication (MFA) requires using two or more *different types* of factors (Something you know, Something you have, Something you are).\\n\\nScenario: A bank requires you to enter a password, and then asks you to enter a 4-digit PIN.\\n\\nTask: Is this true Multi-Factor Authentication? Output exactly one word: Yes or No.",
        "difficulty": "Beginner",
        "starter_code": "True MFA? ",
        "solution_code": "No",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "No"}]
    },
    {
        "title": "Guided Lab: Auth vs Auth",
        "description": "Determine if the failure is an Authentication failure or an Authorization failure.\\n\\nScenario: Alice logs into her company payroll system successfully using her username, password, and MFA token. However, when she clicks the 'View CEO Salary' button, she receives an 'Access Denied' error.\\n\\nTask: Is this an Authentication block or an Authorization block?",
        "difficulty": "Beginner",
        "starter_code": "Block Type: ",
        "solution_code": "Authorization",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Authorization"}]
    },
    {
        "title": "Hands-on Task: Asymmetric Cryptography Logic",
        "description": "Bob wants to send a highly confidential file to Alice over the internet using Asymmetric Cryptography. They have generated their respective Public and Private keys.\\n\\nTask: Exactly which key must Bob use to *encrypt* the file so that only Alice can read it?",
        "difficulty": "Intermediate",
        "starter_code": "Key to use: ",
        "solution_code": "Alice's Public Key",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Alice's Public Key"}]
    },
    {
        "title": "Scenario Analysis: IDOR (Insecure Direct Object Reference)",
        "description": "A developer builds a website. When Bob logs in, his browser goes to `bank.com/account?id=101`. Bob realizes he can manually change the URL to `bank.com/account?id=102` and suddenly he is viewing Alice's bank account.\\n\\nTask: The developer implemented Authentication (Bob had to log in). What specific security mechanism completely failed here?",
        "difficulty": "Intermediate",
        "starter_code": "Failure: ",
        "solution_code": "Authorization (Specifically, backend authorization checks). The server failed to verify if Bob was authorized to view account ID 102.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Authorization (Specifically, backend authorization checks). The server failed to verify if Bob was authorized to view account ID 102."}]
    },
    {
        "title": "Debugging Task: The Custom Cipher",
        "description": "Your company's lead developer announces: 'I don't trust standard AES encryption because hackers have the source code for it. I wrote my own custom encryption algorithm. It shifts every letter by 3 places. It is perfectly secure because nobody knows the algorithm!'\\n\\nTask: Based on cryptographic best practices, explain why 'Rolling your own crypto' and relying on a secret algorithm is a catastrophic security failure.",
        "difficulty": "Advanced",
        "starter_code": "Reason: ",
        "solution_code": "Reason: Security by Obscurity is not real security. Industry standard algorithms (like AES) are secure *because* they have been mathematically vetted by the world's best cryptographers for decades. Custom algorithms are easily reverse-engineered and almost always contain mathematical flaws.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Reason: Security by Obscurity is not real security. Industry standard algorithms (like AES) are secure *because* they have been mathematically vetted by the world's best cryptographers for decades. Custom algorithms are easily reverse-engineered and almost always contain mathematical flaws."}]
    },
    {
        "title": "Challenge: Digital Signatures",
        "description": "Asymmetric cryptography isn't just for secrecy; it's also for proving identity (Integrity/Non-repudiation). \\n\\nScenario: Alice wants to prove to Bob that a message truly came from her, and was not altered by a hacker. She encrypts the message (or a hash of it) using her *Private Key*. Bob receives it and decrypts it using Alice's *Public Key*. \\n\\nTask: Why does this mathematically prove the message must have come from Alice?",
        "difficulty": "Challenge",
        "starter_code": "Explanation: ",
        "solution_code": "Because Alice's Private Key is the only key in the universe capable of creating a ciphertext that successfully decrypts with Alice's Public Key. Since it decrypted successfully, only Alice could have encrypted it.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Because Alice's Private Key is the only key in the universe capable of creating a ciphertext that successfully decrypts with Alice's Public Key. Since it decrypted successfully, only Alice could have encrypted it."}]
    }
]

m8_quizzes = [
    {
        "question_text": "What is the definition of Authentication in cybersecurity?",
        "options": ["Determining what permissions a user has", "Encrypting data so it cannot be read", "Verifying the identity of a user or system", "Blocking malicious network traffic"],
        "correct_answer": "Verifying the identity of a user or system",
        "explanation": "Authentication answers the question: 'Are you who you claim to be?'",
        "difficulty": "Beginner"
    },
    {
        "question_text": "Which of the following is an example of 'Something you have' in the context of Authentication Factors?",
        "options": ["A complex password", "A fingerprint", "A physical smartcard or a YubiKey", "A mother's maiden name"],
        "correct_answer": "A physical smartcard or a YubiKey",
        "explanation": "Factors you possess physically (like a hardware token, smartcard, or a mobile phone app) fall under 'Something you have'.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "Why is it mathematically flawed to rely on a system where you enter a Password, and then enter a PIN, and call it 'Multi-Factor Authentication' (MFA)?",
        "options": ["Because PINs are too short", "Because both a Password and a PIN belong to the same category ('Something you know'), meaning it is just Single-Factor Authentication twice", "Because passwords expire", "Because it takes too long for the user"],
        "correct_answer": "Because both a Password and a PIN belong to the same category ('Something you know'), meaning it is just Single-Factor Authentication twice",
        "explanation": "True MFA requires factors from at least two different categories (e.g., Something you know + Something you have).",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "What is the primary difference between Symmetric and Asymmetric cryptography?",
        "options": ["Symmetric is used for hardware; Asymmetric is used for software", "Symmetric uses the same key for encryption and decryption; Asymmetric uses a pair of keys (Public and Private)", "Symmetric is uncrackable; Asymmetric is easily cracked", "There is no difference"],
        "correct_answer": "Symmetric uses the same key for encryption and decryption; Asymmetric uses a pair of keys (Public and Private)",
        "explanation": "Symmetric (like AES) uses one shared key. Asymmetric (like RSA) uses a mathematically linked key pair.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "If Bob wants to send a highly secret encrypted email to Alice using Asymmetric cryptography, which key should Bob use to encrypt the message?",
        "options": ["Bob's Private Key", "Bob's Public Key", "Alice's Private Key", "Alice's Public Key"],
        "correct_answer": "Alice's Public Key",
        "explanation": "Bob encrypts it with Alice's Public Key. Because of the math, only Alice's Private Key (which only she possesses) can decrypt it.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "A user logs into a web application perfectly, but when they try to access a specific file, the server returns an 'HTTP 403 Forbidden' error. What process just occurred?",
        "options": ["Authentication failure", "Authorization enforcement", "Encryption failure", "A firewall block"],
        "correct_answer": "Authorization enforcement",
        "explanation": "The user was authenticated (they logged in), but the server's Authorization rules determined they did not have the permissions to view that file.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "What does RBAC stand for, and what problem does it solve?",
        "options": ["Random Bytes And Cryptography; it generates encryption keys", "Role-Based Access Control; it simplifies authorization by assigning permissions to roles rather than individual users", "Redundant Backup And Control; it ensures availability", "Remote Botnet Attack Command; it is a hacking tool"],
        "correct_answer": "Role-Based Access Control; it simplifies authorization by assigning permissions to roles rather than individual users",
        "explanation": "In large companies, assigning permissions to thousands of individual users is impossible. RBAC groups permissions into roles (e.g., 'HR_Manager').",
        "difficulty": "Advanced"
    },
    {
        "question_text": "Why is 'SIM Swapping' a major threat to modern authentication?",
        "options": ["It steals the user's password from their brain", "It allows attackers to intercept SMS text messages, completely bypassing SMS-based Two-Factor Authentication", "It breaks AES encryption", "It causes physical damage to the mobile phone"],
        "correct_answer": "It allows attackers to intercept SMS text messages, completely bypassing SMS-based Two-Factor Authentication",
        "explanation": "Hackers trick the telecom company into transferring the victim's phone number to the hacker's SIM card, stealing the MFA codes.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "In a Digital Signature, a person encrypts a hash of their message using their own Private Key. Why is this useful?",
        "options": ["It makes the message impossible to read", "It mathematically proves non-repudiation (proof of origin), because only their specific Public Key can successfully decrypt it, verifying they are the true sender", "It makes the message transmit faster over the internet", "It hides their IP address"],
        "correct_answer": "It mathematically proves non-repudiation (proof of origin), because only their specific Public Key can successfully decrypt it, verifying they are the true sender",
        "explanation": "Digital signatures provide Integrity and Non-repudiation (you cannot deny sending it).",
        "difficulty": "Advanced"
    },
    {
        "question_text": "A developer writes a custom encryption algorithm and keeps the code highly secret. Security professionals strongly condemn this practice. What is the fundamental rule the developer is ignoring?",
        "options": ["Kerckhoffs's Principle", "The CIA Triad", "The OSI Model", "Moore's Law"],
        "correct_answer": "Kerckhoffs's Principle",
        "explanation": "Kerckhoffs's Principle states that a cryptosystem should be secure even if everything about the system, except the key, is public knowledge. Relying on a secret algorithm is 'Security by Obscurity'.",
        "difficulty": "Advanced"
    }
]


m9_lesson = """# Hashing, Encryption, Encoding & Certificates

## 1. What Is It?

In cybersecurity, data is constantly being transformed from readable text into unreadable gibberish. However, *how* and *why* it is transformed matters immensely. Beginners often confuse three distinct processes: Hashing, Encryption, and Encoding.

- **Encryption** is a two-way function used for *secrecy*. You lock it with a key, and later, you (or someone else) unlocks it with a key to read the original data.
- **Hashing** is a one-way mathematical function used for *integrity*. You turn data into a fixed-length string of characters (a hash). You can *never* turn the hash back into the original data.
- **Encoding** is a two-way function used for *data compatibility*, not security. There are no keys. It just changes the format of data so a computer can transmit it easily (e.g., Base64).

Finally, **Digital Certificates** are the digital passports of the internet. They combine hashing and encryption to prove that a website (like `google.com`) is actually owned by Google.

## 2. Why Do We Need It?

**Example 1: Passwords (Hashing)**
If a website stores your password using *encryption*, they must also store the decryption key. If a hacker steals the database and the key, all passwords are stolen.
If a website stores your password using *hashing*, they only store the hash. When you log in, they hash what you typed and compare the two hashes. If a hacker steals the database, they only get useless hashes, not your password.

**Example 2: Data Transfer (Encoding)**
If you try to attach a binary image file (.jpg) to an old email server designed only for text, the email server will crash. Your email client *encodes* the image into raw text (Base64), sends it, and the receiver's client decodes it back into an image. No security is provided; anyone who intercepts it can decode it instantly.

## 3. Where Is It Used?

- **Hashing (SHA-256)**: Used to securely store passwords, and to verify that downloaded files (like an OS installer) haven't been tampered with by malware.
- **Encryption (AES/RSA)**: Used to protect data at rest (Full Disk Encryption) and data in transit (VPNs, HTTPS).
- **Encoding (Base64, URL Encoding)**: Used by web developers and API engineers to safely transmit special characters over HTTP.
- **Certificates (X.509)**: Used by every secure website on the internet (the little padlock in your browser).

## 4. How Does It Work?

**The Hashing Process (Integrity)**
Let's use the SHA-256 algorithm.
- Input: `apple` -> Hash: `3a7bd...`
- Input: `apples` -> Hash: `f9b2d...` (Even a 1-letter change completely changes the entire hash, an effect called the Avalanche Effect).
- Important: You cannot mathematically reverse `3a7bd...` back into `apple`.

**The Certificate Process (Authentication & Encryption)**
1. Google generates a Public/Private key pair.
2. Google sends their Public Key to a trusted Certificate Authority (CA), like DigiCert.
3. DigiCert verifies Google's legal identity.
4. DigiCert creates a Certificate containing Google's Public Key and digitally signs it with DigiCert's own Private Key.
5. When you visit Google, your browser checks DigiCert's signature on the certificate. If it matches, your browser trusts the Public Key and uses it to establish a secure encrypted connection.

## 5. Important Terminology

| Term | Meaning |
|------|---------|
| **Hashing** | One-way transformation of data to ensure Integrity. (Cannot be reversed). |
| **Encryption** | Two-way transformation of data to ensure Confidentiality. (Requires a Key). |
| **Encoding** | Two-way transformation of data to ensure Compatibility. (No Key, not secure). |
| **Salt** | Random data added to a password before hashing it, to prevent attackers from using pre-computed tables (Rainbow Tables) to crack it. |
| **Certificate Authority (CA)** | A trusted third-party organization that issues Digital Certificates. |

## 6. Architecture / Diagram

```text
Comparing the Three E's

ENCODING (Format change only)
[ "Hello" ] --(Base64 algorithm)--> [ "SGVsbG8=" ]
[ "SGVsbG8=" ] --(Base64 decode)--> [ "Hello" ]  <-- Anyone can do this

ENCRYPTION (Requires a Key)
[ "Hello" ] + [ Secret Key 'X' ] ----> [ "8f9a2b" ]
[ "8f9a2b" ] + [ Secret Key 'X' ] ---> [ "Hello" ] <-- Only Key holder can do this

HASHING (One-Way Trip)
[ "Hello" ] --(SHA256 algorithm)--> [ "185f8db32271fe25f561a6fc938b2e26" ]
[ "185f8db32271fe25f561..." ] --(Cannot be reversed)--> X
```

## 7. Syntax / Commands / Configuration

You can perform hashing and encoding directly in a Linux or Mac terminal.

```bash
# Hashing a string (Notice how long the output is)
echo -n "Password123" | sha256sum
# Output: 008c70392e3abfbd0fa47bbc2ed96aa99bd49e159727fcba0f2e6abeb3a9d601

# Encoding a string in Base64
echo -n "Hello World" | base64
# Output: SGVsbG8gV29ybGQ=

# Decoding a Base64 string back to text
echo -n "SGVsbG8gV29ybGQ=" | base64 --decode
# Output: Hello World
```

## 8. Beginner Example

- **Encoding** is like translating English into Morse Code. Anyone with a Morse Code chart can translate it back.
- **Encryption** is like putting a letter in a locked safe. Only the person with the physical key can open the safe to read the letter.
- **Hashing** is like putting a letter through a paper shredder. You can weigh the shredded paper to prove it's the exact same letter you shredded yesterday, but you can never put the words back together.

## 9. Real-World Example

**Situation**: You download a Linux Operating System installer (a massive 3GB `.iso` file) from a mirror website.
**Weakness**: The mirror website might have been hacked, and the hacker might have inserted a backdoor virus into the 3GB file.
**Risk**: If you install the backdoored OS, your computer is instantly compromised.
**Mitigation**: The official Linux creators post the SHA-256 Hash of the legitimate file on their secure website. You download the file from the mirror, run `sha256sum` on it locally, and compare your result to the official hash. If they match perfectly, you have cryptographic proof (Integrity) that not a single byte of the 3GB file has been altered.

## 10. What Happens Internally? (Salting Passwords)

If you hash the password `password123`, it always results in hash `ABC`.
Hackers know this. They create massive databases (Rainbow Tables) pre-calculating the hashes for every common password in existence. If they steal a database and see hash `ABC`, they look it up in their table and instantly know the password is `password123`.

To defeat this, defenders use a **Salt**.
Before hashing, the system generates a random string (e.g., `Xq9!`) and adds it to the password.
Input: `password123` + `Xq9!` -> Hash: `ZXY77`.
Now, the attacker's pre-computed table is useless because it doesn't contain the random salt. The attacker must waste immense computing power trying to crack every single password individually.

## 11. Common Mistakes

1. **Using Base64 for Security**: Developers often "encode" API keys or passwords in Base64 in their source code, thinking it is encrypted. Any hacker can decode it in 1 second.
2. **Using outdated Hash Algorithms**: Using MD5 or SHA-1 for passwords. These algorithms are mathematically broken; modern graphics cards can crack billions of MD5 hashes per second.
3. **Not Salting Passwords**: Storing passwords using modern SHA-256, but failing to add a random salt to each user's password.
4. **Ignoring Certificate Errors**: When a browser says "Your connection is not private," users click "Proceed anyway." This usually means a hacker (or a corporate firewall) is actively intercepting the connection and presenting a fake certificate.

## 12. Defensive Best Practices

1. **Password Storage**: Always use strong, salted, and computationally slow hashing algorithms (like Argon2 or bcrypt) to store user passwords.
2. **File Integrity Monitoring (FIM)**: Use tools that constantly hash critical operating system files. If the hash changes unexpectedly, it means malware modified the file, and an alert is triggered.
3. **Certificate Management**: Never let digital certificates expire. An expired certificate on an e-commerce site will cause browsers to block customers, resulting in massive revenue loss.
4. **Assume Encoding is Public**: Never use encoding to hide sensitive data. Only use encryption.

## 13. Security Mindset

When analyzing an application's data flow, ask:
- *I see a weird string like `YWRtaW46cGFzc3dvcmQ=`. It ends in an `=` sign, which is a classic sign of Base64. What happens if I just decode it?*
- *Is this website storing my password securely? (If I click 'Forgot Password' and they email me my exact original password in plain text, I know they aren't hashing it!)*
- *Who issued the certificate for this website? Is it a trusted CA, or is it self-signed?*

## 14. Try It Yourself

Identify this string: `c2VjdXJpdHkgaXMgZnVu`.
It looks like encrypted gibberish, right?
Open a terminal (or use an online Base64 decoder). 
In a terminal, type: `echo -n "c2VjdXJpdHkgaXMgZnVu" | base64 --decode`
You will see that it is merely encoded, and it simply says "security is fun".
"""

m9_exercises = [
    {
        "title": "Concept Check: Hashing vs Encryption",
        "description": "Read the scenario and decide if the process requires Hashing or Encryption.\\n\\nScenario: You are designing a database to store user passwords. If the database is stolen, you want to ensure the attacker cannot reverse the stored data back into the original passwords.\\n\\nTask: Should you use Hashing or Encryption?",
        "difficulty": "Beginner",
        "starter_code": "Process: ",
        "solution_code": "Hashing",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Hashing"}]
    },
    {
        "title": "Guided Lab: The Purpose of Salting",
        "description": "Attackers use pre-calculated 'Rainbow Tables' to quickly crack large lists of stolen password hashes.\\n\\nTask: What is the specific term for the random data added to a password *before* it is hashed, which renders these pre-calculated Rainbow Tables completely useless?",
        "difficulty": "Beginner",
        "starter_code": "Term: ",
        "solution_code": "Salt",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Salt"}]
    },
    {
        "title": "Hands-on Task: Recognizing Base64",
        "description": "As a security analyst, you intercept an HTTP request. You see the header: `Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==`\\n\\nYou recognize the trailing `==` as a dead giveaway for a specific type of Encoding (not encryption). \\n\\nTask: What is the name of this encoding standard, and can you easily read the original data?",
        "difficulty": "Intermediate",
        "starter_code": "Standard: \\nIs it easily readable?: ",
        "solution_code": "Standard: Base64\\nIs it easily readable?: Yes (Anyone can run a Base64 decode command to read it in plain text).",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Standard: Base64\\nIs it easily readable?: Yes (Anyone can run a Base64 decode command to read it in plain text)."}]
    },
    {
        "title": "Scenario Analysis: The Hashed File",
        "description": "A developer sends you an important software update. They also send you the SHA-256 hash of the update file. You download the file, run it through your own SHA-256 tool, and the resulting hash is completely different from the one the developer sent.\\n\\nTask: What does this mathematically prove about the file you downloaded?",
        "difficulty": "Intermediate",
        "starter_code": "Proof: ",
        "solution_code": "It proves the file lacks Integrity. The file has been altered or corrupted in transit (potentially infected with malware) and is not the exact same file the developer created.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "It proves the file lacks Integrity. The file has been altered or corrupted in transit (potentially infected with malware) and is not the exact same file the developer created."}]
    },
    {
        "title": "Debugging Task: The Forgot Password Flaw",
        "description": "You are auditing a new web application. You create an account with the password `MySuperSecret!`. The next day, you click the 'Forgot Password' link. The website immediately sends you an email containing the text: 'Your password is: MySuperSecret!'.\\n\\nTask: Explain why this is a massive, critical security vulnerability regarding how they are storing data.",
        "difficulty": "Advanced",
        "starter_code": "Vulnerability: ",
        "solution_code": "Vulnerability: It proves they are NOT hashing passwords. Hashing is a one-way function. If they can email you your exact original password, it means they are either storing it in plain text or using reversible encryption, both of which are catastrophic failures for password storage.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Vulnerability: It proves they are NOT hashing passwords. Hashing is a one-way function. If they can email you your exact original password, it means they are either storing it in plain text or using reversible encryption, both of which are catastrophic failures for password storage."}]
    },
    {
        "title": "Challenge: Digital Certificates",
        "description": "When you visit `bank.com`, your browser receives a Digital Certificate. The certificate contains `bank.com`'s Public Key, but it also contains a Digital Signature created by a Certificate Authority (like DigiCert).\\n\\nTask: Based on the rules of asymmetric cryptography, what specific key does your browser use to verify DigiCert's signature, proving the certificate is authentic?",
        "difficulty": "Challenge",
        "starter_code": "Key used to verify: ",
        "solution_code": "DigiCert's Public Key. (Because DigiCert signed it with their Private Key, the browser uses the CA's globally trusted Public Key to verify the math).",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "DigiCert's Public Key. (Because DigiCert signed it with their Private Key, the browser uses the CA's globally trusted Public Key to verify the math)."}]
    }
]

m9_quizzes = [
    {
        "question_text": "Which of the following processes is a ONE-WAY mathematical function that cannot be reversed?",
        "options": ["Symmetric Encryption", "Base64 Encoding", "Hashing", "Asymmetric Encryption"],
        "correct_answer": "Hashing",
        "explanation": "Hashing destroys the original data format to create a fixed-length signature. It cannot be decrypted.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "A developer wants to safely transmit binary data (like an image) over a text-based HTTP protocol. They don't care about secrecy, they just want the data format to be compatible. Which process should they use?",
        "options": ["AES Encryption", "Encoding (like Base64)", "SHA-256 Hashing", "A Digital Certificate"],
        "correct_answer": "Encoding (like Base64)",
        "explanation": "Encoding is purely for data formatting and compatibility. It provides zero security.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "What is the primary purpose of a Digital Certificate (like X.509) on a website?",
        "options": ["To compress the website's images so they load faster", "To prove the legal identity of the website and provide the Public Key necessary to establish an encrypted HTTPS connection", "To run antivirus scans on the user's browser", "To hash the user's password"],
        "correct_answer": "To prove the legal identity of the website and provide the Public Key necessary to establish an encrypted HTTPS connection",
        "explanation": "Certificates act as a digital passport, verified by a trusted Certificate Authority, ensuring you are talking to the real website.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "If you change a single comma in a 1,000-page text document and run it through a hashing algorithm (like SHA-256), what happens to the resulting hash?",
        "options": ["Only the last character of the hash changes", "The hash remains exactly the same", "The entire hash changes completely and unrecognizably", "The hashing algorithm crashes"],
        "correct_answer": "The entire hash changes completely and unrecognizably",
        "explanation": "This is called the Avalanche Effect. It ensures that even microscopic tampering is instantly obvious.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "Why do security professionals mandate that a random 'Salt' must be added to user passwords before hashing them in a database?",
        "options": ["To make the password look cooler", "To defeat pre-calculated 'Rainbow Tables' by ensuring that two users with the exact same password have completely different hashes", "To encrypt the database faster", "To compress the database size"],
        "correct_answer": "To defeat pre-calculated 'Rainbow Tables' by ensuring that two users with the exact same password have completely different hashes",
        "explanation": "Salting makes mass-cracking of stolen password hashes computationally unfeasible.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "A junior developer stores an API key in a configuration file as `YXBpa2V5MTIz`. They tell you it is secure because they 'encrypted' it with Base64. What is the correct response?",
        "options": ["Great job, Base64 is military-grade encryption.", "Base64 is encoding, not encryption. It has no key, and any attacker can decode it instantly in their terminal.", "Base64 is hashing, so it can't be reversed.", "Base64 is too slow for modern computers."],
        "correct_answer": "Base64 is encoding, not encryption. It has no key, and any attacker can decode it instantly in their terminal.",
        "explanation": "Base64 is just a different alphabet. It is not encryption.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "You click 'Forgot Password' on a website. They email you a link to reset your password. What does this indicate about their security practices?",
        "options": ["They are storing your password in plain text, which is terrible.", "They are using industry-standard hashing, which is good. Because they can't reverse the hash, they must ask you to create a new password.", "They are using a Certificate Authority.", "They are using a Rainbow Table."],
        "correct_answer": "They are using industry-standard hashing, which is good. Because they can't reverse the hash, they must ask you to create a new password.",
        "explanation": "A secure site literally does not know your password. Therefore, they cannot email it to you; they can only let you reset it.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "In the context of Digital Certificates, what is a CA (Certificate Authority)?",
        "options": ["A local firewall", "A trusted third-party organization (like DigiCert or Let's Encrypt) that vouches for the identity of a website by digitally signing its certificate", "The IT manager at a company", "A type of hashing algorithm"],
        "correct_answer": "A trusted third-party organization (like DigiCert or Let's Encrypt) that vouches for the identity of a website by digitally signing its certificate",
        "explanation": "Browsers inherently trust root CAs. If a CA signs a website's certificate, the browser trusts the website.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "Which of the following algorithms is widely considered mathematically broken and should NEVER be used for hashing passwords or verifying file integrity today?",
        "options": ["SHA-256", "bcrypt", "MD5", "Argon2"],
        "correct_answer": "MD5",
        "explanation": "MD5 (and SHA-1) suffer from collision vulnerabilities and can be cracked in seconds by modern GPUs.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "A hacker intercepts a file being transmitted over a network. The file is protected by AES-256 encryption. The hacker does not have the encryption key. What is the hacker's most likely method of reading the file?",
        "options": ["Running a Base64 decode command", "Using a Rainbow Table", "The hacker cannot read it. Without the key, AES-256 is computationally impossible to break with modern technology.", "Hashing the ciphertext again"],
        "correct_answer": "The hacker cannot read it. Without the key, AES-256 is computationally impossible to break with modern technology.",
        "explanation": "Strong encryption works. Unless the hacker steals the key or exploits a flaw in how the encryption was implemented, the math holds.",
        "difficulty": "Advanced"
    }
]


m10_lesson = """# Web Security Fundamentals

## 1. What Is It?

In the modern world, the "Web Browser" is the primary way humans interact with computers. Therefore, the "Web Application" (the website) is the primary target for attackers. 

Web Security Fundamentals involves understanding how browsers communicate with servers via HTTP/HTTPS, how the server processes that data, and how databases store it. When these components interact improperly, massive vulnerabilities are born. 

Unlike network attacks (which focus on ports and packets), web attacks focus on manipulating the actual data and logic of the application itself.

## 2. Why Do We Need It?

Every bank, hospital, store, and government agency relies on web applications.

**Example 1: The Form Submission**
When you type your username and password into a login form, you are sending data to the server. If the server implicitly trusts that data without checking it, a hacker can type malicious code into the username field to trick the server into deleting the database.

**Example 2: Session Hijacking**
When you log in, the server gives your browser a temporary ID badge (a Session Cookie) so you don't have to log in on every single page click. If a hacker steals this cookie, they can present it to the server and instantly become you.

## 3. Where Is It Used?

- **Frontend Development**: Writing secure JavaScript and HTML that runs in the user's browser.
- **Backend Development**: Writing secure PHP, Python, or Node.js code that processes user input on the server.
- **Bug Bounties**: Ethical hackers get paid millions of dollars a year to find web vulnerabilities in major companies before the bad guys do.

## 4. How Does It Work?

The web operates on a Client-Server model using the **HTTP Protocol** (HyperText Transfer Protocol).

1. **The Request**: The Client (your browser) sends an HTTP Request.
   - It uses a Method (e.g., `GET` to read a page, `POST` to send form data).
   - It includes Headers (metadata like cookies and browser type).
2. **The Processing**: The Web Server receives the request. It often talks to a backend Database (like MySQL) to fetch data.
3. **The Response**: The Web Server sends an HTTP Response.
   - It includes a Status Code (e.g., `200 OK` for success, `404 Not Found`, `500 Server Error`).
   - It includes the HTML/CSS/JavaScript that your browser renders into a visual webpage.

## 5. Important Terminology

| Term | Meaning |
|------|---------|
| **HTTP / HTTPS** | The protocols used for transmitting web pages. (HTTPS is encrypted). |
| **GET Request** | Used to retrieve data from the server. (Data is in the URL). |
| **POST Request** | Used to submit data to the server. (Data is hidden in the body). |
| **Cookie** | A small piece of data the server tells your browser to store. Used to remember you (Session ID). |
| **Input Validation** | The defensive practice of strictly checking all data submitted by a user before processing it. |

## 6. Architecture / Diagram

```text
The Web Application Architecture

[ Hacker's Browser ]
       |
  (HTTP POST Request)
  Username: admin
  Password: ' OR 1=1 --
       |
       v
[ Web Server (Python/PHP) ]
       |
  (Translates input directly into a database query)
  SELECT * FROM users WHERE username='admin' AND password='' OR 1=1 --'
       |
       v
[ Database (MySQL) ]
  (Database sees '1=1', which is always True. It ignores the password check.)
  (Returns Admin data)
       |
[ Web Server ] -> (Logs hacker in as Admin)
```

## 7. Syntax / Commands / Configuration

Security professionals don't just use a normal web browser. They use tools called **Web Proxies** (like Burp Suite or OWASP ZAP). 
A proxy sits between your browser and the internet. It catches the HTTP Request before it leaves your computer, allowing you to manually rewrite the hidden data before sending it to the server.

```http
# A Raw HTTP GET Request (Intercepted by a Proxy)
GET /profile?user_id=105 HTTP/1.1
Host: www.bank.com
Cookie: session_id=abc123xyz
User-Agent: Mozilla/5.0

# A hacker might intercept this and manually change "user_id=105" to "user_id=106" 
# to see if the server allows them to read another person's profile.
```

## 8. Beginner Example

Think of a web server as a restaurant kitchen, and the browser as the customer.
- The **HTTP Request** is the waiter taking your order ("I want a hamburger").
- The **HTTP Response** is the waiter bringing the hamburger back.
- **Input Validation Failure**: What if the customer orders "I want you to set the kitchen on fire"? A secure waiter (input validation) says "That's not on the menu, request denied." An insecure waiter blindly hands that ticket to the chef, and the chef follows the instructions. 

## 9. Real-World Example

**Situation**: An online store has a shopping cart feature.
**Weakness**: The price of the item is sent from the browser to the server in a hidden HTML field. The server trusts the browser and never checks the actual database price.
**Threat**: A hacker intercepts the HTTP POST request using a proxy.
**Risk**: The hacker changes the `price=$500` field to `price=$1`.
**Impact**: The server processes the checkout and charges the hacker's credit card exactly $1 for a $500 television.
**Mitigation**: NEVER trust the client (browser). The server must only use the browser to determine the Item ID. The server must then look up the price in its own secure database.

## 10. What Happens Internally? (The Golden Rule)

The absolute golden rule of Web Security is: **Never Trust User Input.**

Any data that originates from the client side (the browser) is completely under the control of the user. This includes URLs, form fields, cookies, and HTTP headers. 

Internally, when a web framework takes user input and concatenates (glues) it directly into a Database Query (SQL), an OS Command, or HTML output without sanitizing it first, a vulnerability is created. An attacker can use special characters (like quotes `'`, semicolons `;`, or brackets `< >`) to "break out" of the expected data format and inject their own executable code.

## 11. Common Mistakes

1. **Client-Side Validation Only**: Writing JavaScript that prevents a user from typing letters into an "Age" box. This is good for user experience, but a hacker can bypass the JavaScript entirely by sending a raw HTTP request. You must ALWAYS validate on the server side.
2. **Verbose Error Messages**: When a server crashes, it spits out a detailed stack trace showing the exact database version and lines of code that failed. Hackers use these errors as a treasure map to build exploits.
3. **Unencrypted Logins**: Sending login credentials over standard HTTP. Anyone on the same Wi-Fi network can read the plain text packets and steal the password.
4. **Predictable Session IDs**: Generating session cookies like `session=1`, `session=2`. A hacker can just guess that `session=3` is the next logged-in user and hijack their account.

## 12. Defensive Best Practices

1. **Strict Server-Side Validation**: Validate all input against a strict "allow-list" (e.g., this field must be exactly 5 numbers) before processing it.
2. **Parameterization**: Never glue user input directly into database queries. Use Parameterized Queries (Prepared Statements), which treat user input strictly as data, never as executable code.
3. **Secure Cookies**: When the server issues a session cookie, it must flag it as `Secure` (only transmit over HTTPS) and `HttpOnly` (prevent malicious JavaScript from reading the cookie).
4. **Use HTTPS Everywhere**: Force all traffic to use TLS/SSL encryption.

## 13. Security Mindset

When looking at a webpage, an attacker doesn't look at the pretty pictures. They look at the URL and the inputs:
- *If the URL is `site.com/view?file=report.pdf`, what happens if I change it to `site.com/view?file=../../../../../etc/passwd`? Will the server blindly read a core OS configuration file and show it to me?*
- *If this site has a search bar, what happens if I search for `<script>alert('Hacked')</script>`? Will the server reflect that code back and execute it in my browser?*

## 14. Try It Yourself

Open any webpage (like Google or Wikipedia).
Press `F12` (or Right Click -> Inspect) to open the Developer Tools.
Click on the "Network" tab.
Refresh the page.
You are now seeing exactly what an attacker sees—every single HTTP Request and Response flying between your browser and the server. Click on one of the requests and look at the "Headers". This is the hidden metadata that powers the web.
"""

m10_exercises = [
    {
        "title": "Concept Check: GET vs POST",
        "description": "Read the scenario and decide which HTTP Method is appropriate.\\n\\nScenario: A user is filling out a secure login form with a username and a highly sensitive password.\\n\\nTask: Should the browser send this data using a GET request (where data is visible in the URL) or a POST request (where data is hidden in the body)?",
        "difficulty": "Beginner",
        "starter_code": "Method: ",
        "solution_code": "POST",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "POST"}]
    },
    {
        "title": "Guided Lab: The Golden Rule",
        "description": "A developer writes JavaScript on the webpage to ensure a user's password is at least 8 characters long. The developer assumes they don't need to check the length again on the backend server.\\n\\nTask: What is the fundamental web security rule this developer is violating regarding where input comes from?",
        "difficulty": "Beginner",
        "starter_code": "Rule violated: ",
        "solution_code": "Never trust user input (or Never rely solely on client-side validation).",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Never trust user input (or Never rely solely on client-side validation)."}]
    },
    {
        "title": "Hands-on Task: Session Cookies",
        "description": "You log into a banking app. The server gives your browser a cookie: `Cookie: session_id=999abc`.\\n\\nTask: If a hacker intercepts this cookie over public Wi-Fi, what can they do with it, and what is this attack called?",
        "difficulty": "Intermediate",
        "starter_code": "What they can do: \\nAttack Name: ",
        "solution_code": "What they can do: They can put the cookie in their own browser and instantly access your bank account without needing your username or password.\\nAttack Name: Session Hijacking.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "What they can do: They can put the cookie in their own browser and instantly access your bank account without needing your username or password.\\nAttack Name: Session Hijacking."}]
    },
    {
        "title": "Scenario Analysis: Trusting the Client",
        "description": "A mobile game app sends an HTTP POST request to the server when you finish a level: `POST /submit_score` with body `score=50`. The server reads the score and adds it to the global leaderboard.\\n\\nTask: Thinking like an attacker equipped with an interception proxy (like Burp Suite), how do you get the #1 spot on the leaderboard in 5 seconds?",
        "difficulty": "Intermediate",
        "starter_code": "Attacker Action: ",
        "solution_code": "Use the proxy to intercept the HTTP request leaving the phone, manually change the body to `score=9999999`, and forward it to the server. Because the server blindly trusts the client's data, it accepts the fake score.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Use the proxy to intercept the HTTP request leaving the phone, manually change the body to `score=9999999`, and forward it to the server. Because the server blindly trusts the client's data, it accepts the fake score."}]
    },
    {
        "title": "Debugging Task: Parameter Tampering",
        "description": "An online store checkout page URL looks like this: `store.com/checkout?item_id=4&price=20.00`.\\n\\nTask: Explain the severe architectural flaw in how this application handles pricing data.",
        "difficulty": "Advanced",
        "starter_code": "Flaw: ",
        "solution_code": "Flaw: The application relies on the client (the URL parameter) to dictate the price. An attacker can simply change the URL to `price=0.01` before hitting enter. The server should only receive the `item_id` and look up the price securely in its own backend database.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Flaw: The application relies on the client (the URL parameter) to dictate the price. An attacker can simply change the URL to `price=0.01` before hitting enter. The server should only receive the `item_id` and look up the price securely in its own backend database."}]
    },
    {
        "title": "Challenge: Directory Traversal",
        "description": "You notice a website loads images using this URL format: `site.com/image_loader.php?file=logo.png`.\\nYou know that in Linux, `../` means 'go up one directory level', and `/etc/passwd` contains user account names.\\n\\nTask: What exact URL would an attacker try to type in the browser to attempt to steal the `/etc/passwd` file from the server?",
        "difficulty": "Challenge",
        "starter_code": "Malicious URL: ",
        "solution_code": "site.com/image_loader.php?file=../../../../../etc/passwd",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "site.com/image_loader.php?file=../../../../../etc/passwd"}]
    }
]

m10_quizzes = [
    {
        "question_text": "What is the absolute 'Golden Rule' of web application security?",
        "options": ["Always use green fonts", "Never trust user input", "Always use a Windows server", "Never use cookies"],
        "correct_answer": "Never trust user input",
        "explanation": "Any data coming from the browser can be manipulated by an attacker. It must be strictly validated on the server.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "Which HTTP method is designed to submit data to the server (like a login form) and hides the data in the body of the request rather than putting it in the URL?",
        "options": ["GET", "POST", "HTTP", "HTML"],
        "correct_answer": "POST",
        "explanation": "POST requests are used for sending sensitive or large amounts of data. GET requests put parameters directly in the URL.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "What is a 'Web Proxy' (like Burp Suite or OWASP ZAP) primarily used for by security professionals?",
        "options": ["To speed up their internet connection", "To intercept and manually modify HTTP requests before they are sent from the browser to the web server", "To block viruses from being downloaded", "To write HTML code"],
        "correct_answer": "To intercept and manually modify HTTP requests before they are sent from the browser to the web server",
        "explanation": "Proxies allow hackers and defenders to see and manipulate the hidden metadata and parameters sent by the browser.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "When you log into a website, the server gives your browser a small piece of data called a 'Cookie'. What is the primary purpose of a Session Cookie?",
        "options": ["To track your physical location", "To act as a temporary ID badge so the server remembers you are logged in as you click from page to page", "To encrypt your hard drive", "To play sound effects"],
        "correct_answer": "To act as a temporary ID badge so the server remembers you are logged in as you click from page to page",
        "explanation": "HTTP is a stateless protocol. Cookies provide state (memory) so you don't have to re-enter your password on every page.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "A developer adds a JavaScript rule to a webpage that prevents users from typing special characters into a form. Is the application secure from malicious input now?",
        "options": ["Yes, JavaScript cannot be bypassed", "No, an attacker can use a proxy to intercept the request and inject special characters after the JavaScript has run, meaning the server must also validate the input", "Yes, as long as it's a Chrome browser", "No, because JavaScript is illegal"],
        "correct_answer": "No, an attacker can use a proxy to intercept the request and inject special characters after the JavaScript has run, meaning the server must also validate the input",
        "explanation": "Client-side validation is for user convenience. Server-side validation is for security.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "If an attacker successfully steals your active Session Cookie over an unencrypted Wi-Fi network, what can they do?",
        "options": ["Nothing, cookies are useless", "They can use the cookie to bypass the login screen and hijack your active session", "They can find out your physical home address", "They can fry your motherboard"],
        "correct_answer": "They can use the cookie to bypass the login screen and hijack your active session",
        "explanation": "Session hijacking (or sidejacking) allows an attacker to impersonate you completely until the session expires or you log out.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "What does setting the `HttpOnly` flag on a Session Cookie do?",
        "options": ["It forces the cookie to only travel over HTTPS", "It prevents client-side scripts (like malicious JavaScript) from reading the cookie, mitigating Cross-Site Scripting (XSS) attacks", "It makes the cookie expire faster", "It turns the cookie into a password"],
        "correct_answer": "It prevents client-side scripts (like malicious JavaScript) from reading the cookie, mitigating Cross-Site Scripting (XSS) attacks",
        "explanation": "If a hacker injects JavaScript into a page to steal cookies, the `HttpOnly` flag tells the browser, 'Do not let JavaScript touch this.'",
        "difficulty": "Advanced"
    },
    {
        "question_text": "An e-commerce site calculates the total cart price by taking the item price sent from the user's browser. What is the fundamental architectural flaw?",
        "options": ["The price is too high", "The server is trusting the client to provide critical business data, which an attacker can easily tamper with using a proxy", "The database is too slow", "The browser is not using cookies"],
        "correct_answer": "The server is trusting the client to provide critical business data, which an attacker can easily tamper with using a proxy",
        "explanation": "Prices, access levels, and critical logic must always be determined on the backend, never trusted from the frontend.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "A web application has a URL like `site.com/download.php?file=report.pdf`. An attacker changes the URL to `site.com/download.php?file=../../../../etc/passwd` and successfully downloads the server's password file. What is this attack called?",
        "options": ["SQL Injection", "Cross-Site Scripting (XSS)", "Directory Traversal (or Path Traversal)", "DDoS"],
        "correct_answer": "Directory Traversal (or Path Traversal)",
        "explanation": "The attacker traversed out of the intended web directory and into the core operating system files.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "Why do security experts strongly recommend turning OFF verbose error messages (e.g., stack traces showing database syntax errors) in production web environments?",
        "options": ["Because they take up too much hard drive space", "Because attackers use these detailed error messages as a map to understand the backend infrastructure and craft specific exploits", "Because they confuse legitimate users", "Because it makes the server run faster"],
        "correct_answer": "Because attackers use these detailed error messages as a map to understand the backend infrastructure and craft specific exploits",
        "explanation": "If an app crashes, the user should just see 'Oops, something went wrong.' Only the backend logs should record the exact technical failure.",
        "difficulty": "Intermediate"
    }
]


m11_lesson = """# OWASP Top 10

## 1. What Is It?

The **OWASP Top 10** is a standard awareness document for developers and web application security. It represents a broad consensus about the most critical security risks to web applications. 

Created by the Open Worldwide Application Security Project (OWASP), it is updated every few years to reflect the changing threat landscape. It is not just a list of vulnerabilities; it is the fundamental curriculum for ethical hackers testing web apps, and the baseline checklist for developers building them.

If a company is breached via a web application, it is almost guaranteed that the vulnerability used was listed on the OWASP Top 10.

## 2. Why Do We Need It?

Security is vast, and developers cannot be experts in everything. The OWASP Top 10 provides a focused, prioritized list. 

**Example 1: Compliance**
Many major security standards (like PCI-DSS for credit card processing) legally mandate that a company's web applications are tested specifically against the OWASP Top 10.

**Example 2: Common Language**
When a penetration tester finds a flaw, they don't just say "I broke your site." They categorize it: "You have an A03:2021 Injection vulnerability." This allows developers to instantly understand the nature and severity of the risk.

## 3. Where Is It Used?

- **Software Development Lifecycle (SDLC)**: Training developers *before* they write code to avoid these specific pitfalls.
- **Dynamic Application Security Testing (DAST)**: Automated scanners look specifically for OWASP Top 10 signatures.
- **Penetration Testing**: Human hackers manually test applications against every category on the list.

## 4. How Does It Work?

The list groups thousands of individual vulnerabilities into 10 broad categories. While the exact rankings change, the core concepts remain consistent. 

Here are the most critical categories historically and currently:

1. **Broken Access Control**: Users acting outside of their intended permissions (e.g., User A viewing User B's bank account).
2. **Cryptographic Failures**: Protecting sensitive data poorly (e.g., storing passwords in plain text, using old encryption).
3. **Injection**: Sending malicious data to trick an interpreter (e.g., SQL Injection, where a hacker types database commands into a login box).
4. **Insecure Design**: Flaws in the architecture itself, before code is even written.
5. **Security Misconfiguration**: Failing to securely configure servers (e.g., leaving default passwords, leaving cloud buckets public).
6. **Vulnerable and Outdated Components**: Using old open-source libraries that have known public exploits.

## 5. Important Terminology

| Term | Meaning |
|------|---------|
| **OWASP** | Open Worldwide Application Security Project. |
| **SQL Injection (SQLi)** | Injecting malicious SQL commands into a database query via user input. |
| **Cross-Site Scripting (XSS)** | Injecting malicious JavaScript into a webpage, which then executes in the browsers of other users. |
| **Broken Access Control** | Failure to enforce what authenticated users are allowed to do. |
| **CVE** | Common Vulnerabilities and Exposures. A dictionary of publicly known security vulnerabilities. |

## 6. Architecture / Diagram

```text
The Injection Concept

[ Intended Application Logic ]
"SELECT account_balance FROM users WHERE username = ' [USER INPUT] ' "

[ Normal User Input: 'Bob' ]
"SELECT account_balance FROM users WHERE username = 'Bob' "
(Result: Shows Bob's balance)

[ Malicious User Input: 'Bob' OR 1=1 -- ]
"SELECT account_balance FROM users WHERE username = 'Bob' OR 1=1 -- ' "
(Result: 1=1 is always true. The database ignores the username check and dumps ALL account balances).
```

## 7. Syntax / Commands / Configuration

Security professionals use tools to identify OWASP vulnerabilities. A common tool for finding outdated components (A06) is `npm audit` for Node.js developers, or `pip-audit` for Python.

```bash
# Example: Scanning a Python project for known vulnerabilities in its libraries
pip-audit

# Output might look like:
# Found 1 known vulnerability in 1 package
# Name: Django
# Version: 2.1.1
# ID: CVE-2019-14234
# Fix Versions: 2.1.10
# Description: SQL injection vulnerability...
```

## 8. Beginner Example

Imagine a hotel.
- **Broken Access Control**: Your room key (Room 101) accidentally opens Room 102 as well. 
- **Security Misconfiguration**: The hotel buys a new high-tech safe for the lobby, but forgets to change the default passcode from `1234`.
- **Injection**: You fill out a comment card and drop it in the suggestion box. Instead of writing a comment, you write "Fire the manager." The boss reads it aloud, and blindly follows the instruction.

## 9. Real-World Example

**Situation**: Equifax, one of the largest credit reporting agencies, suffered a massive breach in 2017.
**OWASP Category**: A06 - Vulnerable and Outdated Components.
**Weakness**: Equifax's web portal relied on an open-source framework called Apache Struts. A critical vulnerability in Struts was publicly announced in March. A patch was released immediately.
**Threat**: Hackers scanning the internet for unpatched Struts servers.
**Risk**: Equifax failed to apply the patch for months.
**Impact**: Attackers found the server, exploited the known vulnerability, and stole the personal data (including Social Security Numbers) of 147 million Americans.
**Mitigation**: Maintain a strict software inventory and automate patch management for all third-party libraries.

## 10. What Happens Internally? (Cross-Site Scripting - XSS)

Injection isn't just for databases (SQLi). It also targets other users' browsers (XSS).

1. A hacker goes to a forum and posts a comment. But instead of text, they post malicious JavaScript: `<script>steal_cookie()</script>`.
2. The web server (lacking input validation) saves this exact text to the database.
3. You visit the forum to read the comments.
4. The web server sends the hacker's text to your browser.
5. Your browser sees the `<script>` tag. It assumes the server wanted this code to run. It executes the hacker's JavaScript, stealing your session cookie and sending it to the hacker.

This is a classic OWASP Injection/XSS flaw. The server trusted the input, and the victim's browser trusted the server.

## 11. Common Mistakes

1. **Assuming firewalls stop web attacks**: A network firewall allows Port 443 (HTTPS) traffic through. An SQL Injection attack is just data traveling over Port 443. The firewall will blindly allow it. You need a WAF (Web Application Firewall).
2. **Security by Obscurity**: Trying to fix Broken Access Control by simply hiding the "Admin" button from normal users using CSS (`display: none`). The hacker will just look at the source code, find the URL for the admin page, and navigate to it directly.
3. **Trusting open-source code blindly**: Assuming that because a library is on GitHub, it is secure. You are responsible for every line of code you import.

## 12. Defensive Best Practices

1. **Parameterize Queries**: To stop SQL Injection, never concatenate user input into database queries. Use Prepared Statements.
2. **Encode Output**: To stop XSS, if you must display user input on a webpage, encode it first (turn `<script>` into `&lt;script&gt;`). The browser will display it as text, not execute it as code.
3. **Implement Strict Access Control**: Enforce Authorization checks on the backend for *every single request*. Never trust the client to enforce rules.
4. **Automate Dependency Scanning**: Use tools in your CI/CD pipeline that automatically block code from being deployed if it contains outdated, vulnerable libraries.

## 13. Security Mindset

When analyzing a web application against the OWASP Top 10, ask:
- *(A01 Access Control)*: If I change `user_id=5` to `user_id=6` in the URL, what happens?
- *(A02 Crypto Failures)*: Does this site force HTTPS on all pages, or just the login page?
- *(A03 Injection)*: If I put a single quote `'` in the search bar, does the database crash and show me a syntax error?
- *(A05 Misconfiguration)*: If I go to `site.com/non_existent_page`, does the 404 error page reveal the exact version of the web server (e.g., Apache/2.4.41)?

## 14. Try It Yourself

Explore the concept of Broken Access Control on your own computer.
If you have multiple user accounts on your PC, log in as a standard user.
Open the file explorer and try to navigate into the other user's Documents folder (`C:\\Users\\OtherUser\\Documents`). 
Windows will block you. This is an example of proper Access Control. The OS verified your identity (Authentication) and determined you do not have permission to view that folder (Authorization).
"""

m11_exercises = [
    {
        "title": "Concept Check: Identify the OWASP Category",
        "description": "Read the scenario and identify which broad OWASP concept it violates.\\n\\nScenario: An attacker types SQL commands into a website's search bar. The web server blindly passes the input to the database, which executes the commands and deletes all tables.\\n\\nTask: What is the specific OWASP term for this type of attack?",
        "difficulty": "Beginner",
        "starter_code": "Category: ",
        "solution_code": "Injection (or SQL Injection)",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Injection"}]
    },
    {
        "title": "Guided Lab: Vulnerable Components",
        "description": "Equifax was breached because they failed to update the Apache Struts library.\\n\\nTask: Which OWASP Top 10 category directly addresses the danger of using unpatched, third-party open-source code?",
        "difficulty": "Beginner",
        "starter_code": "Category: ",
        "solution_code": "Vulnerable and Outdated Components",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Vulnerable and Outdated Components"}]
    },
    {
        "title": "Hands-on Task: XSS Mitigation",
        "description": "Cross-Site Scripting (XSS) occurs when an application takes untrusted user input and sends it to a web browser without proper validation or escaping.\\n\\nTask: To stop XSS, when a server takes a user's comment (like `<script>`) and displays it on the screen, what specific defensive action must the server perform to ensure the browser treats it as text, not executable code?",
        "difficulty": "Intermediate",
        "starter_code": "Defensive Action: ",
        "solution_code": "Output Encoding (or Escaping/Sanitization)",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Output Encoding (or Escaping/Sanitization)"}]
    },
    {
        "title": "Scenario Analysis: Broken Access Control",
        "description": "A developer wants to prevent normal users from deleting files. They write JavaScript that hides the 'Delete' button if the user is not an Admin.\\n\\nTask: Why does this fail to prevent Broken Access Control when an attacker uses an interception proxy like Burp Suite?",
        "difficulty": "Intermediate",
        "starter_code": "Reason: ",
        "solution_code": "Reason: The attacker doesn't need to click the button. They can use the proxy to manually craft and send the 'DELETE' HTTP request directly to the backend server. If the backend server does not explicitly verify authorization, it will delete the file.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Reason: The attacker doesn't need to click the button. They can use the proxy to manually craft and send the 'DELETE' HTTP request directly to the backend server. If the backend server does not explicitly verify authorization, it will delete the file."}]
    },
    {
        "title": "Debugging Task: The Misconfiguration",
        "description": "You scan a corporate web server and find a directory called `admin/backups/`. Inside is a file named `database_dump.sql` containing all user passwords. There is no login required to access this directory.\\n\\nTask: Which OWASP category does this represent, and what is the technical fix?",
        "difficulty": "Advanced",
        "starter_code": "Category: \\nFix: ",
        "solution_code": "Category: Security Misconfiguration (or Broken Access Control).\\nFix: Configure the web server (e.g., in Apache/Nginx config) to deny public access to the backups directory, or move the backups outside of the public web root entirely.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Category: Security Misconfiguration (or Broken Access Control).\\nFix: Configure the web server (e.g., in Apache/Nginx config) to deny public access to the backups directory, or move the backups outside of the public web root entirely."}]
    },
    {
        "title": "Challenge: SQL Injection Logic",
        "description": "An attacker types the following into a username field: `' OR 1=1 -- `\\n\\nThe backend query becomes:\\n`SELECT * FROM users WHERE username = '' OR 1=1 -- ' AND password = 'xxx'`\\n\\nTask: In SQL syntax, what does the `--` do, and why does this attack successfully bypass the password check?",
        "difficulty": "Challenge",
        "starter_code": "What '--' does: \\nWhy it works: ",
        "solution_code": "What '--' does: It comments out the rest of the SQL line.\\nWhy it works: The database evaluates '1=1', which is always True. Because of the '--', the database completely ignores the password check at the end of the query. It returns the first record (usually the Admin).",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "What '--' does: It comments out the rest of the SQL line.\\nWhy it works: The database evaluates '1=1', which is always True. Because of the '--', the database completely ignores the password check at the end of the query. It returns the first record (usually the Admin)."}]
    }
]

m11_quizzes = [
    {
        "question_text": "What is the OWASP Top 10?",
        "options": ["A list of the top 10 most wanted hackers", "A standard awareness document representing a broad consensus about the most critical security risks to web applications", "A list of the 10 best antivirus programs", "A programming language used for security"],
        "correct_answer": "A standard awareness document representing a broad consensus about the most critical security risks to web applications",
        "explanation": "It is the foundational document for web application security training and testing globally.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "Which OWASP category involves an attacker sending malicious data (like database commands) to a system, tricking the system into executing those commands?",
        "options": ["Broken Access Control", "Cryptographic Failures", "Injection", "Security Misconfiguration"],
        "correct_answer": "Injection",
        "explanation": "Injection (like SQLi or Command Injection) occurs when untrusted data is processed as code.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "A user logs into their banking app. They change the URL from `bank.com/account=1` to `bank.com/account=2` and are able to view another customer's balance. What OWASP vulnerability is this?",
        "options": ["Cross-Site Scripting (XSS)", "Broken Access Control", "Vulnerable and Outdated Components", "Server-Side Request Forgery"],
        "correct_answer": "Broken Access Control",
        "explanation": "The server failed to enforce authorization checks on the backend to ensure the user had access to account 2. (Historically known as IDOR).",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "A developer leaves default passwords (admin/admin) on a production database and leaves directory listing enabled on the web server. Which OWASP category does this fall under?",
        "options": ["Security Misconfiguration", "Cryptographic Failures", "Injection", "Insecure Design"],
        "correct_answer": "Security Misconfiguration",
        "explanation": "Failing to harden the server, leaving default settings, or leaving unnecessary features enabled are misconfigurations.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "What is the most effective way to prevent SQL Injection?",
        "options": ["Installing a better antivirus", "Using Parameterized Queries (Prepared Statements) so the database treats user input strictly as data, never as executable code", "Hiding the database IP address", "Using Base64 encoding on all input"],
        "correct_answer": "Using Parameterized Queries (Prepared Statements) so the database treats user input strictly as data, never as executable code",
        "explanation": "Prepared statements pre-compile the SQL logic. When the user input is added later, the database knows not to execute it.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "In a Cross-Site Scripting (XSS) attack, whose machine is actually executing the malicious code?",
        "options": ["The Web Server", "The Database Server", "The Victim's Web Browser", "The Firewall"],
        "correct_answer": "The Victim's Web Browser",
        "explanation": "XSS targets the client. The server merely acts as a delivery mechanism to bounce the malicious JavaScript into the victim's browser.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "How did the 2017 Equifax breach, which compromised 147 million people, primarily happen?",
        "options": ["An employee stole a hard drive", "They used an unpatched, outdated version of the Apache Struts open-source library that had a known vulnerability", "An attacker guessed the CEO's password", "They forgot to use HTTPS"],
        "correct_answer": "They used an unpatched, outdated version of the Apache Struts open-source library that had a known vulnerability",
        "explanation": "This highlights the catastrophic risk of OWASP A06: Vulnerable and Outdated Components. Patch management is critical.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "What does 'Output Encoding' (or Escaping) do to prevent XSS attacks?",
        "options": ["It encrypts the entire webpage", "It converts special characters (like `<` and `>`) into HTML entities (like `&lt;` and `&gt;`), forcing the browser to display them as text rather than execute them as code", "It blocks IP addresses from known hackers", "It deletes all JavaScript from the server"],
        "correct_answer": "It converts special characters (like `<` and `>`) into HTML entities (like `&lt;` and `&gt;`), forcing the browser to display them as text rather than execute them as code",
        "explanation": "Encoding neutralizes the attack payload before the browser ever sees it.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "A company designs a password reset feature. It works by emailing a randomly generated 4-digit PIN to the user. An attacker realizes they can simply guess all 10,000 possible PINs on the website in a few minutes. Which OWASP category best describes this architectural flaw?",
        "options": ["Vulnerable Components", "Insecure Design", "Injection", "Security Misconfiguration"],
        "correct_answer": "Insecure Design",
        "explanation": "The code works exactly as intended, but the design itself is fundamentally flawed (no rate-limiting, PIN space is too small).",
        "difficulty": "Advanced"
    },
    {
        "question_text": "Will a standard Network Firewall (which allows Port 80 and 443) protect a web application from an SQL Injection attack?",
        "options": ["Yes, firewalls block all malicious traffic", "No, because the SQL Injection payload is hidden inside legitimate HTTP traffic on Port 80/443, which the network firewall blindly allows through", "Yes, as long as it's a hardware firewall", "No, because SQL injection uses Port 22"],
        "correct_answer": "No, because the SQL Injection payload is hidden inside legitimate HTTP traffic on Port 80/443, which the network firewall blindly allows through",
        "explanation": "Network firewalls only look at IPs and Ports. To block SQLi, you need a Web Application Firewall (WAF) that actually reads the HTTP payload.",
        "difficulty": "Advanced"
    }
]


m12_lesson = """# Secure Coding & Input Validation

## 1. What Is It?

Web Security Fundamentals taught us *how* applications are attacked (OWASP Top 10). **Secure Coding** is the proactive discipline of writing software that is inherently resistant to those attacks. 

The most critical principle of secure coding is **Input Validation**. Input Validation is the process of testing any data supplied by a user or external system against a strict set of rules before the application processes it. If the data doesn't match the rules, it is rejected entirely.

## 2. Why Do We Need It?

Attackers are incredibly creative. They will submit data in formats, lengths, and encodings that a developer never anticipated. If the code blindly assumes all input is benign, the application will break, crash, or be compromised.

**Example 1: The Buffer Overflow**
A developer expects the user to input a 5-letter zip code. The code reserves 5 bytes of memory. An attacker inputs a 50,000-letter string. If there is no input validation checking the length, the memory overflows, crashing the system or allowing the attacker to execute code.

**Example 2: Logic Flaws**
An e-commerce site expects a user to enter the quantity of items they want to buy. A user enters `-10`. Without validation checking for negative numbers, the system calculates `Price = -10 * $50 = -$500`, and accidentally refunds the attacker $500.

## 3. Where Is It Used?

- **Everywhere**: Input validation must happen at every trust boundary.
- **Form Fields**: Checking emails, phone numbers, and ages.
- **APIs**: Validating JSON data payloads sent from other servers.
- **File Uploads**: Ensuring an uploaded file is actually a `.jpg` and not a malicious `.php` script.

## 4. How Does It Work?

There are two primary ways to validate input:
1. **Deny-listing (Blacklisting)**: Trying to block known "bad" characters (like blocking `<script>` or `SELECT`). 
   *This is a terrible approach.* Attackers will find ways around it (e.g., using `<sCrIpT>` or URL encoding).
2. **Allow-listing (Whitelisting)**: Strictly defining what "good" data looks like, and blocking *everything else*.
   *This is the gold standard.* If you expect a US Zip Code, the allow-list rule is: "Exactly 5 characters, and all characters must be numbers from 0-9." If the input is "Hello", it's rejected. If it's "123456", it's rejected. If it's "1234a", it's rejected.

## 5. Important Terminology

| Term | Meaning |
|------|---------|
| **Input Validation** | Verifying data against strict rules before processing. |
| **Allow-listing (Whitelisting)** | Defining exactly what is allowed and rejecting all else. (Highly secure). |
| **Deny-listing (Blacklisting)** | Defining what is forbidden. (Easily bypassed, insecure). |
| **Sanitization** | Modifying input to make it safe (e.g., stripping out HTML tags). |
| **Regular Expressions (Regex)** | A sequence of characters specifying a search pattern, often used to enforce allow-lists (e.g., `^[0-9]{5}$`). |

## 6. Architecture / Diagram

```text
The Secure Coding Pipeline

[ User Browser ]
       | (Submits 'Age: 25')
       v
[ Web Server ]
       |
  1. Receive Input: "25"
  2. Input Validation (Allow-list): 
     - Is it a number? (Yes)
     - Is it greater than 0? (Yes)
     - Is it less than 130? (Yes)
       |
  3. Processing: (Data is safe, proceed)
       |
  4. Database Query (Parameterized):
     "UPDATE users SET age = ? WHERE id = ?"
       |
[ Database ]
```

## 7. Syntax / Commands / Configuration

Developers use **Regular Expressions (Regex)** to implement strict allow-lists. 

```python
import re

def is_valid_zip_code(zip_code_string):
    # Regex rule: Exactly 5 digits (0-9). Nothing else.
    # ^ means start of string, $ means end of string.
    rule = re.compile(r'^[0-9]{5}$')
    
    if rule.match(zip_code_string):
        return True
    else:
        return False

print(is_valid_zip_code("90210")) # True
print(is_valid_zip_code("90210 DROP TABLE")) # False (Rejected instantly)
```

## 8. Beginner Example

Think of a nightclub bouncer using a VIP list.
- **Deny-listing**: The bouncer has a list of 5 known troublemakers to keep out. If a new troublemaker shows up not on the list, they get in. (Insecure).
- **Allow-listing**: The bouncer has a list of 10 VIPs. If your name is not exactly on the list, you are rejected, no matter who you are. (Highly secure).

## 9. Real-World Example

**Situation**: A website allows users to upload a profile picture.
**Weakness**: The developer uses a Deny-list: `if filename.endswith(".php"): block_upload()`
**Threat**: A hacker wants to upload a malicious PHP script.
**Risk**: The hacker names their file `malware.php5` or `malware.PHP` or `malware.php.jpg`. The deny-list fails to catch these variations, the file is uploaded, and the server is compromised.
**Mitigation**: The developer uses an Allow-list. They check the actual file header (magic bytes) to ensure it is a valid image, and force the system to rename the file upon saving it so it ends strictly in `.jpg` or `.png`.

## 10. What Happens Internally? (Defense in Depth in Code)

Secure coding isn't just one check; it's Defense in Depth applied to software architecture.

If a user submits an email address:
1. **Client-Side**: The browser uses HTML5 (`type="email"`) to check if it has an `@` symbol. (For user convenience).
2. **Server-Side Validation**: The backend Python code receives it and runs a strict Regex allow-list to ensure it only contains valid email characters. (For security).
3. **Parameterization**: When saving to the database, the backend uses a prepared statement so even if validation failed, SQL injection is impossible. (Failsafe).
4. **Output Encoding**: When displaying the email on the profile page, the server HTML-encodes it to prevent XSS. (Failsafe).

## 11. Common Mistakes

1. **Trusting Client-Side Validation**: Believing that because the web form restricts input to 10 characters, the server will never receive 11 characters. Attackers use proxies to bypass the browser entirely.
2. **Deny-listing characters**: Trying to block `'` and `<` and `>`. You will always miss one, or an attacker will use URL encoding (like `%3C`) to bypass your filter.
3. **Validating Too Late**: Waiting until the data is already inside the database logic before checking if it's safe. Validate at the very edge of your application.
4. **Crashing Poorly**: When validation fails, the app throws a massive unhandled exception showing database credentials. Apps should fail securely and gracefully.

## 12. Defensive Best Practices

1. **Type Checking**: Before doing any complex validation, just check the data type. If you expect an Age, ensure it is an Integer, not a String.
2. **Length Checking**: Set strict minimum and maximum lengths for all text inputs to prevent buffer overflows and DoS attacks.
3. **Range Checking**: If you expect a month, ensure the number is between 1 and 12.
4. **Use Built-in Framework Features**: Modern frameworks (like Django, Spring, or Laravel) have built-in, highly tested validation and parameterization libraries. Use them instead of writing your own from scratch.

## 13. Security Mindset

When writing or reviewing code, ask:
- *What is the most ridiculous, unexpected data a user could submit to this variable?*
- *What happens if they submit a negative number? A billion? Null? Emoji?*
- *Is this input being validated against an allow-list, or are we just hoping they don't submit bad characters?*

## 14. Try It Yourself

Think about a standard login form (Username and Password).
Design a mental allow-list for a Username. 
- Type: String
- Length: Minimum 3 characters, Maximum 20 characters.
- Characters allowed: Letters (A-Z, a-z), Numbers (0-9), and Underscores (_). No spaces, no special characters.
If a developer enforces this allow-list strictly on the server side, it is virtually impossible for a hacker to execute SQL Injection or XSS through the username field, because the required malicious characters (`'` `<`) will be instantly rejected!
"""

m12_exercises = [
    {
        "title": "Concept Check: Allow-listing vs Deny-listing",
        "description": "Read the scenario and identify the validation strategy.\\n\\nScenario: A firewall is configured with a rule: 'Block traffic from IP 1.2.3.4 and IP 5.6.7.8. Allow all other traffic.'\\n\\nTask: Is this an example of Allow-listing or Deny-listing?",
        "difficulty": "Beginner",
        "starter_code": "Strategy: ",
        "solution_code": "Deny-listing (Blacklisting)",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Deny-listing"}]
    },
    {
        "title": "Guided Lab: Client vs Server Validation",
        "description": "A developer writes a JavaScript function that prevents a user from submitting a form if the 'Age' field is negative. \\n\\nTask: Is this sufficient for security, or must the validation also happen somewhere else?",
        "difficulty": "Beginner",
        "starter_code": "Where else?: ",
        "solution_code": "It must also happen on the backend server (Server-side validation).",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "It must also happen on the backend server (Server-side validation)."}]
    },
    {
        "title": "Hands-on Task: Logic Flaws",
        "description": "You are reviewing code for a banking transfer function:\\n`def transfer(amount, recipient):`\\n`  if user_balance >= amount:`\\n`    user_balance -= amount`\\n`    recipient_balance += amount`\\n\\nTask: What critical input validation check is missing that would allow an attacker to actually *steal* money from the recipient?",
        "difficulty": "Intermediate",
        "starter_code": "Missing check: ",
        "solution_code": "The code fails to check if the `amount` is greater than zero (Range checking). An attacker could submit a negative transfer amount (e.g., -500), which would add money to their balance and subtract it from the recipient.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "The code fails to check if the `amount` is greater than zero (Range checking). An attacker could submit a negative transfer amount (e.g., -500), which would add money to their balance and subtract it from the recipient."}]
    },
    {
        "title": "Scenario Analysis: File Upload Defense",
        "description": "A website allows users to upload avatars. The developer uses an allow-list checking the file extension: `if filename.endswith('.jpg') or filename.endswith('.png'): allow()`\\n\\nTask: While better than a deny-list, why is relying *only* on the file extension still dangerous?",
        "difficulty": "Intermediate",
        "starter_code": "Danger: ",
        "solution_code": "An attacker can simply rename a malicious PHP script to `malware.php.jpg`. The code checks the extension, sees '.jpg', and allows it. The developer must also validate the file's internal content (MIME type/Magic bytes) and ensure the server doesn't execute it.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "An attacker can simply rename a malicious PHP script to `malware.php.jpg`. The code checks the extension, sees '.jpg', and allows it. The developer must also validate the file's internal content (MIME type/Magic bytes) and ensure the server doesn't execute it."}]
    },
    {
        "title": "Debugging Task: Regex Allow-list",
        "description": "You need to write an allow-list rule for a US Zip Code (exactly 5 digits).\\nYou use this Regular Expression: `^[0-9]{5}$`\\n\\nTask: Explain exactly what the `^`, the `[0-9]`, the `{5}`, and the `$` mean in this pattern to guarantee security.",
        "difficulty": "Advanced",
        "starter_code": "Explanation: ",
        "solution_code": "Explanation: `^` means the match must start at the very beginning of the string. `[0-9]` means only numbers are allowed. `{5}` means exactly five occurrences. `$` means the match must end at the very end of the string. Together, they ensure the string is exactly 5 numbers and nothing else (preventing '12345malware').",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Explanation: `^` means the match must start at the very beginning of the string. `[0-9]` means only numbers are allowed. `{5}` means exactly five occurrences. `$` means the match must end at the very end of the string. Together, they ensure the string is exactly 5 numbers and nothing else (preventing '12345malware')."}]
    },
    {
        "title": "Challenge: Fail Securely",
        "description": "When input validation fails, the application must throw an error. A developer configures the app to display a full Python stack trace and database query syntax to the user when validation fails.\\n\\nTask: What is this anti-pattern called, and what is the secure alternative?",
        "difficulty": "Challenge",
        "starter_code": "Anti-pattern: \\nAlternative: ",
        "solution_code": "Anti-pattern: Verbose Error Messages (or Information Leakage).\\nAlternative: Fail securely/gracefully. Display a generic, polite error to the user ('Invalid input'), and log the detailed technical stack trace securely on the backend server for the developers to review.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Anti-pattern: Verbose Error Messages (or Information Leakage).\\nAlternative: Fail securely/gracefully. Display a generic, polite error to the user ('Invalid input'), and log the detailed technical stack trace securely on the backend server for the developers to review."}]
    }
]

m12_quizzes = [
    {
        "question_text": "What is the primary goal of Input Validation?",
        "options": ["To make the website load faster", "To test any data supplied by a user against a strict set of rules before processing it", "To encrypt user passwords", "To format HTML correctly"],
        "correct_answer": "To test any data supplied by a user against a strict set of rules before processing it",
        "explanation": "Input validation ensures that only safe, expected data is allowed into the application logic.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "In secure coding, what is the difference between Allow-listing (Whitelisting) and Deny-listing (Blacklisting)?",
        "options": ["Allow-listing blocks known bad input; Deny-listing allows known good input", "Allow-listing defines exactly what is permitted and rejects all else (Secure); Deny-listing tries to block specific bad characters and allows all else (Insecure)", "They are the exact same thing", "Allow-listing is for networks; Deny-listing is for databases"],
        "correct_answer": "Allow-listing defines exactly what is permitted and rejects all else (Secure); Deny-listing tries to block specific bad characters and allows all else (Insecure)",
        "explanation": "Deny-lists always fail eventually because attackers find creative ways to bypass the blocked characters.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "A developer writes HTML5 code: `<input type=\"number\" min=\"1\" max=\"10\">`. Is the application fully protected against an attacker submitting the number 500?",
        "options": ["Yes, the browser will prevent it", "No, an attacker can bypass the browser using a proxy to submit the number 500 directly to the server. The server must also validate it.", "Yes, HTML5 is perfectly secure", "No, but the database will automatically fix it"],
        "correct_answer": "No, an attacker can bypass the browser using a proxy to submit the number 500 directly to the server. The server must also validate it.",
        "explanation": "Client-side validation is easily bypassed. Server-side validation is mandatory.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "What type of validation check would prevent a user from accidentally (or maliciously) entering an age of -25?",
        "options": ["Type Checking", "Length Checking", "Range Checking", "Encoding"],
        "correct_answer": "Range Checking",
        "explanation": "Range checking ensures a number falls between a sensible minimum and maximum value (e.g., 0 to 120).",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "What is a Regular Expression (Regex) commonly used for in secure coding?",
        "options": ["To encrypt the database", "To define strict pattern-matching rules for Allow-list input validation (e.g., ensuring an email looks exactly like an email)", "To generate random passwords", "To speed up server reboots"],
        "correct_answer": "To define strict pattern-matching rules for Allow-list input validation (e.g., ensuring an email looks exactly like an email)",
        "explanation": "Regex is a powerful tool for strictly defining the allowed shape and characters of text input.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "A developer wants to stop SQL Injection, so they write a function to delete any single quotes (`'`) from user input. What is this flawed defensive strategy called?",
        "options": ["Parameterization", "Deny-listing (Blacklisting)", "Allow-listing", "Output Encoding"],
        "correct_answer": "Deny-listing (Blacklisting)",
        "explanation": "Trying to filter out specific 'bad' characters is a deny-list approach and is highly prone to failure.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "When a web application encounters unexpected input and crashes, what is the most secure way to handle the error?",
        "options": ["Display a detailed stack trace to the user so they can help debug it", "Fail securely by showing a generic 'Error occurred' message to the user, and log the detailed technical data securely on the backend", "Ignore the error and continue processing", "Email the database password to the admin"],
        "correct_answer": "Fail securely by showing a generic 'Error occurred' message to the user, and log the detailed technical data securely on the backend",
        "explanation": "Verbose error messages give attackers a roadmap to your application's architecture.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "In Defense in Depth, if you strictly validate a user's input (Allow-list) when they submit it, do you still need to use Parameterized Queries when saving it to the database?",
        "options": ["No, validation is enough", "Yes, you should use multiple layers of defense. Validation ensures the data is the correct format, Parameterization ensures it cannot be executed as code.", "No, databases don't get hacked", "Yes, but only for Admin users"],
        "correct_answer": "Yes, you should use multiple layers of defense. Validation ensures the data is the correct format, Parameterization ensures it cannot be executed as code.",
        "explanation": "Defense in depth means assuming one layer might fail and relying on the next.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "Why is it dangerous to validate a file upload based solely on the filename extension (e.g., `.jpg`)?",
        "options": ["Because JPEGs are large files", "Because an attacker can rename a malicious executable script to end in `.jpg`, bypassing the check, and the server might still execute it", "Because file extensions don't work on Macs", "Because it uses too much CPU"],
        "correct_answer": "Because an attacker can rename a malicious executable script to end in `.jpg`, bypassing the check, and the server might still execute it",
        "explanation": "Names mean nothing. Secure file upload validation checks the file's internal 'magic bytes' to ensure it is truly an image.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "Which of the following describes 'Type Checking', the most basic form of input validation?",
        "options": ["Checking if the user typed their password fast enough", "Ensuring that if the application expects an Integer (like an Age), the input is actually an Integer and not a String of text", "Checking if the text is in English", "Checking the font type of the text"],
        "correct_answer": "Ensuring that if the application expects an Integer (like an Age), the input is actually an Integer and not a String of text",
        "explanation": "Type checking instantly defeats many injection attacks because you cannot inject SQL code into a pure Integer variable.",
        "difficulty": "Advanced"
    }
]


m13_lesson = """# Reconnaissance & OSINT

## 1. What Is It?

Welcome to Phase 3: Ethical Hacking. 

The very first step of any hacking methodology (whether performed by a criminal or an ethical penetration tester) is **Reconnaissance**. Reconnaissance is the act of gathering information about a target *before* launching an attack. 

A specific and powerful subset of reconnaissance is **OSINT (Open-Source Intelligence)**. OSINT is the collection and analysis of data gathered from publicly available sources (the "open" internet). 

A professional hacker rarely starts by firing exploits at a firewall. They start by reading. They map out the target's employees, technologies, physical locations, and business relationships without ever touching the target's actual servers.

## 2. Why Do We Need It?

**Example 1: The Phishing Campaign**
If an attacker wants to breach a bank, guessing passwords on the external firewall is loud and will trigger alarms. Instead, the attacker uses OSINT (LinkedIn, corporate blogs) to find the names, emails, and job titles of 50 employees in the HR department. The attacker then crafts a highly convincing, targeted phishing email tailored specifically to the HR manager. This is far more likely to succeed.

**Example 2: The Forgotten Subdomain**
A company spends $1,000,000 securing `www.company.com`. However, through reconnaissance, an attacker discovers a forgotten, unprotected testing server at `dev-test.company.com` that the IT team set up 5 years ago and abandoned. The attacker breaches the entire network through that forgotten server.

## 3. Where Is It Used?

- **Red Teaming / Penetration Testing**: Testers use OSINT to build a massive map of the target's attack surface before designing their attack plan.
- **Law Enforcement & Journalism**: Investigators use OSINT to track down criminals, trace cryptocurrency transactions, and uncover corporate fraud.
- **Social Engineering**: Attackers use OSINT to build psychological profiles of their victims to manipulate them effectively.

## 4. How Does It Work?

Reconnaissance is divided into two categories:

1. **Passive Reconnaissance (OSINT)**: You never interact directly with the target's systems. The target has no idea you are investigating them.
   - *Sources*: Google (Google Dorks), LinkedIn, WHOIS databases, Shodan, Wayback Machine, Public GitHub repositories, Social Media.
2. **Active Reconnaissance**: You interact directly with the target's systems. The target's firewalls and logs will record your IP address. (We will cover this deeply in the next module).
   - *Sources*: Ping sweeps, Port scanning (Nmap), Banner grabbing.

## 5. Important Terminology

| Term | Meaning |
|------|---------|
| **OSINT** | Open-Source Intelligence. Gathering data from publicly available sources. |
| **Attack Surface** | The total sum of all vulnerabilities and exposed systems a target has. |
| **Passive Recon** | Gathering info without touching the target's servers (Undetectable). |
| **Active Recon** | Gathering info by directly probing the target's servers (Detectable). |
| **Google Dorking** | Using advanced search operators in Google to find hidden or sensitive files. |

## 6. Architecture / Diagram

```text
The Reconnaissance Funnel

1. Broad OSINT (Passive)
   [ Google, LinkedIn, WHOIS, DNS Records ]
   -> Identifies 500 Employee Emails, 50 Subdomains, 3 Physical Offices.

2. Focused Probing (Active)
   [ Nmap Port Scanning against the 50 Subdomains ]
   -> Identifies 10 Open Ports (80, 443, 22, 3306).

3. Vulnerability Identification
   [ Scanning Port 80 for specific software versions ]
   -> Identifies Apache 2.4.49 (Known to be vulnerable).

4. Exploitation
   [ The actual attack ]
```

## 7. Syntax / Commands / Configuration

**Google Dorking**
Google indexes almost everything on the internet. Hackers use special operators to filter out the noise and find sensitive files that companies accidentally left public.

```text
# Find Excel spreadsheets containing the word "password" on a specific site
site:example.com filetype:xlsx intext:password

# Find exposed directory listings (Index of /)
intitle:"index of" "backup"

# Find exposed configuration files containing database credentials
filetype:env intext:DB_PASSWORD
```

**DNS Information Gathering**
You can use command-line tools to query public DNS (Domain Name System) records.
```bash
# Find the IP address of a website
nslookup google.com

# Find the email servers (MX records) for a domain
dig google.com MX
```

## 8. Beginner Example

Imagine you want to rob a museum (hypothetically!).
- **Passive Recon (OSINT)**: You sit at home, look at the museum's public website to find their hours, use Google Earth to see the layout of the roof, and look at LinkedIn to find the name of the Head of Security. The museum has no idea you are planning a robbery.
- **Active Recon**: You walk up to the museum at 2:00 AM, jiggle the back door handle to see if it's locked, and shine a flashlight into the security cameras. The museum's security guards will absolutely notice you doing this.

## 9. Real-World Example

**Situation**: A hacker wants to breach a tech startup.
**Weakness**: A junior developer at the startup asked a question on a public coding forum (like StackOverflow) three years ago.
**Threat (OSINT)**: The hacker searches Google for the startup's domain name combined with coding keywords.
**Risk**: The hacker finds the old forum post. In the post, the developer pasted a chunk of code to ask for help. Embedded in that code is the hardcoded AWS (Amazon Web Services) master password for the startup.
**Impact**: The hacker uses the password to log into the startup's cloud infrastructure and deletes all their servers. This required zero technical "hacking" of the startup's firewall; it was pure OSINT.

## 10. What Happens Internally? (The WHOIS Database)

When a company registers a domain name (like `learnx.com`), they must provide their contact information to the registrar (like GoDaddy). This information is often published in a global, public database called **WHOIS**.

Hackers query the WHOIS database to find:
- The physical address of the company.
- The name, phone number, and email address of the IT Administrator who registered the domain.
- The date the domain was created and when it expires.

*Security Note*: Attackers often use the IT Administrator's name and email found in WHOIS to craft highly believable phishing emails targeting other employees ("Hi, this is Dave from IT...").

## 11. Common Mistakes

1. **Leaking Metadata**: Companies publish PDF reports online. They don't realize the PDF file contains hidden metadata showing the exact software version used to create it, the internal username of the author, and the internal file path on the author's computer.
2. **Oversharing on Social Media**: Employees posting selfies at their desk. Attackers zoom in on the sticky notes on their monitors to steal passwords, or look at the ID badge hanging from their neck to forge a fake one.
3. **Public GitHub Repositories**: Developers accidentally uploading proprietary source code or API keys to public GitHub repositories instead of private ones. Bots scan GitHub 24/7 looking for these mistakes.

## 12. Defensive Best Practices

1. **Perform Self-OSINT**: Security teams must regularly Google their own company, search for their own domain on GitHub, and check Shodan to see what an attacker sees.
2. **Scrub Metadata**: Use tools to automatically remove metadata from all documents and images before publishing them to the corporate website.
3. **WHOIS Privacy**: Pay the domain registrar for "Domain Privacy" so your personal IT contact information is hidden from the public WHOIS database.
4. **Employee Training**: Train employees on the dangers of oversharing on social media, emphasizing that attackers use that information to build psychological profiles for social engineering.

## 13. Security Mindset

When performing OSINT on a target, ask:
- *What is the target trying to hide, but accidentally broadcasting?*
- *Who are the people behind this technology, and what are their weaknesses?*
- *If I look at this company's job postings on a career site, what does it tell me? (e.g., If they are hiring a "Windows Server 2012 Administrator", I now know exactly what outdated OS they are running internally).*

## 14. Try It Yourself

Perform a passive OSINT exercise on yourself.
1. Open Google in an Incognito/Private window.
2. Search for your exact name in quotes: `"Firstname Lastname"`.
3. Add a modifier like your city or school: `"Firstname Lastname" "New York"`.
4. Look at the images tab. 
5. What could a hacker learn about you in 5 minutes? Your hobbies? Your family members' names? Where you work? How could they use that information to trick you in an email?
"""

m13_exercises = [
    {
        "title": "Concept Check: Passive vs Active Recon",
        "description": "Read the scenario and decide if it is Passive or Active reconnaissance.\\n\\nScenario: A penetration tester uses a tool to send thousands of TCP SYN packets directly to a company's web server to see which ports are open.\\n\\nTask: Is this Passive or Active?",
        "difficulty": "Beginner",
        "starter_code": "Recon Type: ",
        "solution_code": "Active",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Active"}]
    },
    {
        "title": "Guided Lab: OSINT Sources",
        "description": "You need to find the names and job titles of the IT staff at a target company without touching their servers.\\n\\nTask: Name a popular, public professional social networking website that is widely used by hackers for this exact OSINT purpose.",
        "difficulty": "Beginner",
        "starter_code": "Website: ",
        "solution_code": "LinkedIn",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "LinkedIn"}]
    },
    {
        "title": "Hands-on Task: Google Dorking",
        "description": "You are a bug bounty hunter looking for exposed database backups on the domain `target.com`.\\n\\nTask: Write the exact Google Dork syntax to search only within `target.com` for files that have the extension `.sql`.",
        "difficulty": "Intermediate",
        "starter_code": "Google Dork: ",
        "solution_code": "site:target.com filetype:sql",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "site:target.com filetype:sql"}]
    },
    {
        "title": "Scenario Analysis: The Job Posting",
        "description": "A company posts a job listing for a 'Senior Database Administrator'. The listing says: 'Must have 5 years experience managing MySQL 5.5 and Apache Tomcat 7'.\\n\\nTask: Explain why this seemingly harmless HR job posting is highly valuable intelligence for a hacker.",
        "difficulty": "Intermediate",
        "starter_code": "Value to Hacker: ",
        "solution_code": "It reveals the exact internal technology stack and specific version numbers the company is running. The hacker can now skip guessing and immediately look up specific exploits for MySQL 5.5 and Tomcat 7.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "It reveals the exact internal technology stack and specific version numbers the company is running. The hacker can now skip guessing and immediately look up specific exploits for MySQL 5.5 and Tomcat 7."}]
    },
    {
        "title": "Debugging Task: The Wayback Machine",
        "description": "A company accidentally published a page containing user passwords at `site.com/passwords.txt`. They realize the mistake 5 minutes later and delete the file. The server now returns a 404 Not Found error.\\n\\nTask: Explain how an OSINT investigator might still be able to view that deleted file without hacking the server.",
        "difficulty": "Advanced",
        "starter_code": "Method: ",
        "solution_code": "By using the Internet Archive's 'Wayback Machine' (or Google Cache). If an automated web crawler took a snapshot of that URL during those 5 minutes, the file's contents are permanently archived on the internet.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "By using the Internet Archive's 'Wayback Machine' (or Google Cache). If an automated web crawler took a snapshot of that URL during those 5 minutes, the file's contents are permanently archived on the internet."}]
    },
    {
        "title": "Challenge: Shodan",
        "description": "Google indexes websites. 'Shodan' is a search engine that indexes devices connected to the internet (webcams, routers, industrial control systems) by scanning their IP addresses and grabbing their service banners.\\n\\nTask: If a hacker uses Shodan to find an exposed security camera, is the hacker performing Passive or Active reconnaissance against the camera? Explain why.",
        "difficulty": "Challenge",
        "starter_code": "Type: \\nWhy: ",
        "solution_code": "Type: Passive.\\nWhy: The hacker is not touching the camera directly. Shodan's servers already performed the active scanning months ago. The hacker is just reading Shodan's public database, so the camera's logs will show Shodan's IP, not the hacker's IP.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Type: Passive.\\nWhy: The hacker is not touching the camera directly. Shodan's servers already performed the active scanning months ago. The hacker is just reading Shodan's public database, so the camera's logs will show Shodan's IP, not the hacker's IP."}]
    }
]

m13_quizzes = [
    {
        "question_text": "What does OSINT stand for?",
        "options": ["Offensive Security Internal Network Testing", "Open-Source Intelligence", "Operating System Internal Networking Theory", "Online Security Incident Network Tracking"],
        "correct_answer": "Open-Source Intelligence",
        "explanation": "OSINT involves gathering actionable intelligence from publicly available, open-source data.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "What is the defining characteristic of 'Passive' reconnaissance?",
        "options": ["It requires the attacker to physically break into a building", "It involves directly interacting with the target's servers, triggering their firewalls", "The attacker gathers information without ever directly interacting with the target's systems, making it undetectable by the target", "It only works on Windows operating systems"],
        "correct_answer": "The attacker gathers information without ever directly interacting with the target's systems, making it undetectable by the target",
        "explanation": "Passive recon relies on third-party sources (like Google or WHOIS) to gather data about the target.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "A hacker searches Google using the query: `site:example.com filetype:pdf`. What is this technique called?",
        "options": ["SQL Injection", "Port Scanning", "Google Dorking", "Cross-Site Scripting"],
        "correct_answer": "Google Dorking",
        "explanation": "Google Dorking uses advanced search operators to filter results and uncover sensitive files indexed by Google.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "Why do hackers frequently search for a target company's job postings on sites like Indeed or LinkedIn?",
        "options": ["Because hackers are looking for legitimate employment", "To find out exactly what specific software, hardware, and versions the company's IT department is running internally", "To steal the company's credit card data", "To launch a DDoS attack against the HR department"],
        "correct_answer": "To find out exactly what specific software, hardware, and versions the company's IT department is running internally",
        "explanation": "Job requirements (e.g., 'Must know Cisco ASA Firewalls') map out the internal network architecture for the attacker.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "What information does the WHOIS database provide to an OSINT investigator?",
        "options": ["The passwords for a website", "The public registration details of a domain name, often including the name, email, and phone number of the IT administrator", "The list of all open ports on a server", "The source code of a web application"],
        "correct_answer": "The public registration details of a domain name, often including the name, email, and phone number of the IT administrator",
        "explanation": "WHOIS is the internet's phonebook for domain ownership.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "A developer takes a screenshot of their computer desktop to show a colleague a funny meme, and posts it on Twitter. An attacker zooms in on the background of the image and reads a sticky note containing a password. This is an example of:",
        "options": ["A highly sophisticated Zero-Day exploit", "An OSINT discovery resulting from employee oversharing", "A Cryptographic Failure", "A DNS poisoning attack"],
        "correct_answer": "An OSINT discovery resulting from employee oversharing",
        "explanation": "Humans are often the weakest link. OSINT heavily relies on analyzing human mistakes.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "What is the 'Wayback Machine' (Internet Archive) used for in reconnaissance?",
        "options": ["To travel back in time physically", "To view historical snapshots of a website, allowing an attacker to see sensitive pages or files that the company has since deleted", "To perform high-speed port scans", "To encrypt web traffic"],
        "correct_answer": "To view historical snapshots of a website, allowing an attacker to see sensitive pages or files that the company has since deleted",
        "explanation": "The internet never forgets. Once a file is indexed, it often remains accessible in archives even if the host deletes it.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "How does the search engine 'Shodan' differ from Google?",
        "options": ["Shodan only searches for images", "Google indexes web pages; Shodan indexes internet-connected devices (routers, webcams, servers) based on their IP addresses and open ports", "Shodan is a dark web search engine that requires Tor", "There is no difference"],
        "correct_answer": "Google indexes web pages; Shodan indexes internet-connected devices (routers, webcams, servers) based on their IP addresses and open ports",
        "explanation": "Shodan is the 'search engine for hackers'. It allows you to find devices running specific, vulnerable software globally.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "An attacker uses a command-line tool like `nslookup` or `dig` against a target domain. What are they trying to discover?",
        "options": ["The web server's password", "The physical address of the CEO", "The IP addresses and mail servers associated with the domain via DNS records", "The version of JavaScript the website is running"],
        "correct_answer": "The IP addresses and mail servers associated with the domain via DNS records",
        "explanation": "DNS reconnaissance translates the human-readable domain name into the actual target IP addresses for the next phase of the attack.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "Why do organizations scrub 'Metadata' from PDF files and images before publishing them online?",
        "options": ["To make the files download faster", "Because metadata can contain hidden intelligence, such as the exact software version used, GPS location coordinates, and internal usernames", "Because metadata causes web browsers to crash", "To comply with copyright laws"],
        "correct_answer": "Because metadata can contain hidden intelligence, such as the exact software version used, GPS location coordinates, and internal usernames",
        "explanation": "Metadata is 'data about data'. Hackers extract it using tools like ExifTool to gain internal network intelligence.",
        "difficulty": "Advanced"
    }
]


m14_lesson = """# Scanning & Enumeration

## 1. What Is It?

Once an attacker (or ethical hacker) has gathered OSINT (Passive Recon), they move to **Active Reconnaissance**, heavily relying on **Scanning and Enumeration**.

This is the phase where you actually touch the target's network.
- **Scanning** is the process of sending packets to a target to discover which IP addresses are 'alive' and which Ports are open.
- **Enumeration** is the deeper process of connecting to those open ports to extract detailed information (like software versions, usernames, and network shares).

If Recon is finding out where the building is, Scanning is walking up and checking every single door to see which ones are unlocked, and Enumeration is looking through the window of the unlocked doors to see what valuables are inside.

## 2. Why Do We Need It?

You cannot hack a system if you don't know what it is running.

**Example 1: The Penetration Tester**
A client gives a pen tester a list of 1,000 IP addresses. The tester cannot manually check them all. They use a scanner (like Nmap) to automatically find the 5 IP addresses that actually have web servers running on them, focusing their attack entirely on those 5.

**Example 2: Vulnerability Matching**
If you scan a port and enumerate that it is running "Apache Web Server version 2.2.8", you can now search a database of known vulnerabilities (like Exploit-DB) for that exact version to find a weaponized exploit.

## 3. Where Is It Used?

- **Network Mapping**: IT Administrators use scanning to keep track of all devices on their massive corporate networks.
- **Vulnerability Management**: Automated tools (like Nessus or Qualys) continuously scan corporate networks looking for unpatched software.
- **Ethical Hacking**: The absolute mandatory second step of any engagement.

## 4. How Does It Work?

**1. Host Discovery (Ping Sweep)**
Send a small ICMP packet to every IP address in a range (e.g., 192.168.1.1 to 192.168.1.255). If an IP replies, it is "alive".

**2. Port Scanning**
For every alive IP, send a packet to all 65,535 possible ports.
- If the port replies with SYN-ACK, it is **Open**.
- If it replies with RST (Reset), it is **Closed**.
- If it doesn't reply at all, it is **Filtered** (blocked by a firewall).

**3. Enumeration (Banner Grabbing)**
Connect to the Open ports and capture the text they send back (the "Banner"). The banner usually proudly announces exactly what software and version is running.

## 5. Important Terminology

| Term | Meaning |
|------|---------|
| **Nmap** | (Network Mapper). The industry-standard command-line tool for scanning and enumeration. |
| **Ping Sweep** | Scanning a range of IPs to see which ones are online. |
| **Port Scan** | Probing a specific IP to see which of its 65,535 ports are open. |
| **Banner Grabbing** | Connecting to an open port to read the software version it announces. |
| **Enumeration** | Actively extracting data (users, shares, versions) from a service. |

## 6. Architecture / Diagram

```text
The Scanning Process (Using Nmap)

[ Hacker ] ---> (Sends TCP SYN to Port 80) ---> [ Target Server ]
           <--- (Receives TCP SYN-ACK)     <--- (Port is OPEN)

[ Hacker ] ---> (Sends TCP SYN to Port 22) ---> [ Target Server ]
           <--- (Receives TCP RST)         <--- (Port is CLOSED)

[ Hacker ] ---> (Sends TCP SYN to Port 3389)--> [ Target Server ]
           <--- (No response at all)       <--- (Port is FILTERED by Firewall)

[ Hacker ] ---> (Banner Grabs Port 80)
           <--- ("Server: Apache/2.4.41 (Ubuntu)") -> ENUMERATION SUCCESS!
```

## 7. Syntax / Commands / Configuration

**Nmap (Network Mapper)** is arguably the most important tool in a hacker's toolkit.

```bash
# Basic Ping Sweep to find alive hosts on a local network
nmap -sn 192.168.1.0/24

# Scan a specific IP for the top 1000 common ports
nmap 192.168.1.10

# Scan ALL 65,535 ports (takes longer)
nmap -p- 192.168.1.10

# Aggressive Scan (Grabs Banners/Versions and detects the Operating System)
nmap -A 192.168.1.10
```

## 8. Beginner Example

Imagine you are a detective looking for a specific criminal in a hotel.
- **Host Discovery**: You walk down the hallway and knock on every door. If someone says "Who is it?", you write down that the room is occupied (Alive).
- **Port Scanning**: You go to an occupied room and check if the main door, the window, and the balcony are locked (Checking Ports).
- **Enumeration**: You find an unlocked window. You poke your head in and ask, "Who lives here?" They reply, "I am Bob, and I use Windows 10." (Banner Grabbing).

## 9. Real-World Example

**Situation**: A penetration tester is hired to test a company's external network.
**Action**: The tester runs an Nmap port scan against the company's public IP address.
**Discovery**: Nmap reports that Port 21 (FTP - File Transfer Protocol) is open.
**Enumeration**: The tester connects to Port 21. The server's banner responds: `220 ProFTPD 1.3.5 Server`.
**Exploitation**: The tester searches the internet for "ProFTPD 1.3.5 exploit" and discovers this specific version has a known vulnerability that allows anyone to copy files to the server without a password. The tester uses this to upload a virus.
**Mitigation**: The company should have used a vulnerability scanner to detect the outdated software and patched it to version 1.3.6.

## 10. What Happens Internally? (Stealth Scanning)

Firewalls are smart. If you establish a full TCP connection (SYN, SYN-ACK, ACK) to a port, the firewall will log your IP address.

To avoid detection, hackers use a **TCP SYN Scan** (also called a Stealth Scan or Half-Open scan).
1. Hacker sends SYN.
2. Server replies SYN-ACK (meaning the port is open).
3. Hacker immediately sends an RST (Reset) packet instead of the final ACK.

Because the TCP connection was never fully established, older firewalls and application logs do not record the interaction. The hacker learned the port was open without leaving a log in the application's history. (Modern Intrusion Detection Systems can catch this, however).

## 11. Common Mistakes

1. **Scanning without permission**: Running Nmap against a company without a written contract is a crime. It is the digital equivalent of walking onto someone's property and testing their door handles.
2. **Assuming 'No Ping' means 'Offline'**: Many firewalls are configured to block ICMP (Ping) packets. If you rely only on a ping sweep, you will miss perfectly alive servers that are just ignoring pings.
3. **Ignoring UDP**: Nmap scans TCP by default. Attackers often find vulnerabilities on forgotten UDP ports (like Port 161 for SNMP) because defenders forgot to scan them.

## 12. Defensive Best Practices

1. **Disable Unnecessary Banners**: Configure your web servers and SSH servers so they do not broadcast their exact version numbers. Make the attacker work for it.
2. **Monitor for Scans**: Configure your Intrusion Detection System (IDS) to trigger an alert if a single IP address hits 50 different ports on your server within 10 seconds.
3. **Scan Yourself Continuously**: You must scan your own network more frequently than the attackers do, so you can find and close open doors before they are exploited.

## 13. Security Mindset

When reviewing a scan report, ask:
- *Why is Port 3306 (MySQL) open to the internet? Databases should only be accessible internally.*
- *Nmap says Port 80 is filtered. Is there a firewall in the way, or is the router misconfigured?*
- *This server is running Microsoft IIS web server, but Nmap says the Operating System is Linux. That's impossible; IIS only runs on Windows. Is there a load balancer or proxy tricking the scan?*

## 14. Try It Yourself

If you have Nmap installed (or use a web-based scanner on a permitted target):
1. Open your terminal.
2. Type `nmap scanme.nmap.org`. (This is a server specifically set up by the Nmap creators, granting you legal permission to scan it).
3. Watch the output. It will list the open ports and the services running on them. You just performed Active Reconnaissance!
"""

m14_exercises = [
    {
        "title": "Concept Check: Scanning vs Enumeration",
        "description": "Read the scenario and identify the phase.\\n\\nScenario: An attacker connects to an open port they found and sends a specific command to force the server to reveal a list of all user accounts registered on the system.\\n\\nTask: Is this considered Port Scanning or Enumeration?",
        "difficulty": "Beginner",
        "starter_code": "Phase: ",
        "solution_code": "Enumeration",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Enumeration"}]
    },
    {
        "title": "Guided Lab: Nmap Basics",
        "description": "You need to perform a port scan against a target. You want the scanner to automatically probe the open ports and grab their banners to tell you the exact software versions running.\\n\\nTask: What is the specific 'Aggressive' flag used in Nmap to achieve this?",
        "difficulty": "Beginner",
        "starter_code": "Nmap Flag: ",
        "solution_code": "-A (or -sV for just version detection)",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "-A"}]
    },
    {
        "title": "Hands-on Task: Port States",
        "description": "You scan a target. Nmap reports:\\nPort 80: OPEN\\nPort 22: CLOSED\\nPort 3389: FILTERED\\n\\nTask: Based on TCP networking rules, what specific packet did the target send back to your scanner to indicate that Port 22 was CLOSED?",
        "difficulty": "Intermediate",
        "starter_code": "Packet type: ",
        "solution_code": "RST (Reset)",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "RST (Reset)"}]
    },
    {
        "title": "Scenario Analysis: Ping Sweep Failure",
        "description": "You are hired to test a corporate network. You run a basic ICMP Ping sweep across the IP range. Zero hosts reply. However, when you type one of the IP addresses into your web browser, a corporate website loads perfectly.\\n\\nTask: Explain why the host appeared 'dead' to the ping sweep but is actually alive.",
        "difficulty": "Intermediate",
        "starter_code": "Explanation: ",
        "solution_code": "Explanation: The corporate firewall is configured to block or drop ICMP (Ping) packets. The server is alive and accepting TCP traffic on Port 80/443, but it ignores pings.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Explanation: The corporate firewall is configured to block or drop ICMP (Ping) packets. The server is alive and accepting TCP traffic on Port 80/443, but it ignores pings."}]
    },
    {
        "title": "Debugging Task: The Stealth Scan",
        "description": "An attacker uses an Nmap TCP SYN scan (Stealth Scan) against your web server.\\n\\nTask: Explain the 3 steps of this network interaction, and why the attacker does NOT send the final 'ACK' packet of the TCP handshake.",
        "difficulty": "Advanced",
        "starter_code": "Step 1 (Attacker): \\nStep 2 (Server): \\nStep 3 (Attacker): \\nWhy no ACK?: ",
        "solution_code": "Step 1: Attacker sends SYN.\\nStep 2: Server replies SYN-ACK.\\nStep 3: Attacker sends RST.\\nWhy no ACK?: By tearing down the connection before it fully establishes, the attacker hopes the application layer (like the web server logs) will not record the interaction, helping them remain undetected.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Step 1: Attacker sends SYN.\\nStep 2: Server replies SYN-ACK.\\nStep 3: Attacker sends RST.\\nWhy no ACK?: By tearing down the connection before it fully establishes, the attacker hopes the application layer (like the web server logs) will not record the interaction, helping them remain undetected."}]
    },
    {
        "title": "Challenge: Banner Grabbing Mitigation",
        "description": "During enumeration, you grab a banner from a web server that reads: `Server: Apache/2.4.41 (Ubuntu) PHP/7.4.3`.\\n\\nTask: As a defender, what specific configuration change should you make to this server to follow the principle of 'Security by Obscurity' (even though it's not a primary defense, it slows attackers down)?",
        "difficulty": "Challenge",
        "starter_code": "Action: ",
        "solution_code": "Action: Modify the web server configuration (e.g., `ServerTokens Prod` in Apache) to suppress the version numbers, so the banner only returns a generic `Server: Apache`.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Action: Modify the web server configuration (e.g., `ServerTokens Prod` in Apache) to suppress the version numbers, so the banner only returns a generic `Server: Apache`."}]
    }
]

m14_quizzes = [
    {
        "question_text": "What is the primary difference between Passive Reconnaissance (OSINT) and Active Reconnaissance (Scanning)?",
        "options": ["Passive is illegal; Active is legal", "Passive relies on third-party public data; Active involves sending network packets directly to the target's systems", "Passive finds passwords; Active finds IP addresses", "There is no difference"],
        "correct_answer": "Passive relies on third-party public data; Active involves sending network packets directly to the target's systems",
        "explanation": "Active recon touches the target directly, meaning the target's firewalls can log your IP address.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "What is 'Nmap'?",
        "options": ["A type of computer virus", "The industry-standard command-line tool used by hackers and defenders for network scanning and port enumeration", "A Google search technique", "A type of firewall"],
        "correct_answer": "The industry-standard command-line tool used by hackers and defenders for network scanning and port enumeration",
        "explanation": "Nmap (Network Mapper) is the most famous and widely used scanning tool in cybersecurity.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "In port scanning, if an Nmap scan reports a port state as 'Filtered', what does this usually mean?",
        "options": ["The port is open and ready to accept data", "The server is turned off", "A firewall is blocking the scan packets, so Nmap cannot determine if the port is open or closed", "The port is infected with malware"],
        "correct_answer": "A firewall is blocking the scan packets, so Nmap cannot determine if the port is open or closed",
        "explanation": "When packets are dropped silently by a firewall without returning a Reset (RST) packet, Nmap calls it Filtered.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "What is the process of 'Banner Grabbing'?",
        "options": ["Stealing a website's logo", "Connecting to an open port to capture the text it sends back, which often reveals the exact software name and version number running on that port", "Sending millions of ping requests to crash a server", "Guessing passwords using a dictionary"],
        "correct_answer": "Connecting to an open port to capture the text it sends back, which often reveals the exact software name and version number running on that port",
        "explanation": "Banner grabbing is a key enumeration technique. Once you know the version, you can search for specific exploits.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "Why do attackers often prefer to use a TCP SYN Scan (Stealth Scan) instead of a full TCP Connect Scan?",
        "options": ["Because it encrypts the data", "Because it is completely invisible to all firewalls", "Because by not completing the final ACK of the 3-way handshake, the connection is never fully established, which often bypasses application-level logging", "Because it uses UDP packets which are faster"],
        "correct_answer": "Because by not completing the final ACK of the 3-way handshake, the connection is never fully established, which often bypasses application-level logging",
        "explanation": "A half-open connection tricks many basic systems into not recording the interaction.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "A penetration tester runs an ICMP Ping sweep on a corporate subnet, and no hosts respond. Is it safe to assume there are no computers turned on in that subnet?",
        "options": ["Yes, if ping fails, the computers are physically unplugged", "No, many modern operating systems and corporate firewalls are configured to block or drop ICMP ping requests by default for security reasons", "Yes, ping is 100% reliable", "No, because ping only works on Wi-Fi"],
        "correct_answer": "No, many modern operating systems and corporate firewalls are configured to block or drop ICMP ping requests by default for security reasons",
        "explanation": "Relying purely on Ping for host discovery will cause you to miss many alive, but stealthy, hosts.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "Which phase comes AFTER Port Scanning in the ethical hacking methodology?",
        "options": ["Passive Reconnaissance", "Physical Security Breach", "Enumeration (Extracting detailed info like users and banners from the open ports)", "Writing the final report"],
        "correct_answer": "Enumeration (Extracting detailed info like users and banners from the open ports)",
        "explanation": "You find the open doors (Scanning), then you look inside them (Enumeration), then you attack them (Exploitation).",
        "difficulty": "Advanced"
    },
    {
        "question_text": "A defender configures their web server to return the HTTP header `Server: Apache` instead of `Server: Apache/2.4.49 (Unix) OpenSSL/1.1.1`. What defensive concept is this?",
        "options": ["Cryptography", "Input Validation", "Suppressing banners to obscure the specific software version, making enumeration harder for the attacker", "Network Segmentation"],
        "correct_answer": "Suppressing banners to obscure the specific software version, making enumeration harder for the attacker",
        "explanation": "While 'Security by Obscurity' shouldn't be your only defense, removing version banners slows attackers down significantly.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "If Nmap sends a TCP packet to a closed port on a target server (and there is no firewall blocking it), what type of TCP packet does the server automatically send back?",
        "options": ["SYN-ACK", "ACK", "FIN", "RST (Reset)"],
        "correct_answer": "RST (Reset)",
        "explanation": "The OS network stack replies with a Reset packet, telling the scanner, 'I received your request, but there is no application listening on this port.'",
        "difficulty": "Advanced"
    },
    {
        "question_text": "Why is scanning a computer network without explicit written permission a terrible idea?",
        "options": ["Because it might crash your own computer", "Because Nmap costs money to use", "Because active scanning touches the target's network, leaves logs, and is considered illegal unauthorized access (a cybercrime) in most jurisdictions", "Because it violates the OSI model"],
        "correct_answer": "Because active scanning touches the target's network, leaves logs, and is considered illegal unauthorized access (a cybercrime) in most jurisdictions",
        "explanation": "Ethical hacking requires a 'Get Out of Jail Free' card—a signed contract called a Rules of Engagement document.",
        "difficulty": "Beginner"
    }
]


m15_lesson = """# Vulnerability Assessment

## 1. What Is It?

After enumeration tells you *what* is running on a network, **Vulnerability Assessment** is the process of figuring out if those specific software versions have known, exploitable flaws. 

A Vulnerability Assessment is highly systematic and usually automated. It involves using specialized software (like Nessus, Qualys, or OpenVAS) to scan every device on a network, compare the discovered software against a massive database of known vulnerabilities (the CVE database), and generate a giant report of everything that needs fixing.

It is important to note: A vulnerability assessment *identifies* the open doors. It does *not* walk through them. (Walking through the door is Penetration Testing).

## 2. Why Do We Need It?

Modern corporate networks contain thousands of servers, laptops, and routers. Software vendors release patches for newly discovered bugs every single Tuesday ("Patch Tuesday"). 

**Example 1: The Defender's Dilemma**
An IT team cannot manually check 5,000 laptops every day to see if they are missing the latest Adobe Reader security update. An automated Vulnerability Scanner does this in hours, prioritizing the most critical missing patches so the IT team knows what to fix first.

**Example 2: Compliance**
Almost all cybersecurity regulations (HIPAA, PCI-DSS, SOC 2) legally require companies to perform and document continuous vulnerability assessments. If you process credit cards and don't scan your network, you lose your license to process credit cards.

## 3. Where Is It Used?

- **Blue Teams (Defenders)**: Run continuous, authenticated scans to maintain network hygiene and enforce patch management.
- **Red Teams (Attackers)**: Run unauthenticated, stealthy scans to find the one missing patch they can exploit to breach the network.
- **Auditors**: Review scan reports to ensure the company is actually fixing high-risk vulnerabilities within a required timeframe (e.g., 30 days).

## 4. How Does It Work?

Vulnerability scanners work in two distinct modes:

1. **Unauthenticated Scans (Outside-In)**
   - The scanner acts like a hacker. It connects to the open ports (like Port 80) and grabs the banner.
   - It checks the database: "I see Apache 2.4.41. The database says Apache 2.4.41 has a Directory Traversal flaw (CVE-2021-41773). I will flag this."
   - *Limitation*: The scanner cannot see inside the server (e.g., it doesn't know if Adobe Reader is installed because Adobe Reader doesn't listen on a network port).

2. **Authenticated Scans (Inside-Out)**
   - The scanner is given a highly privileged username and password.
   - It logs directly into the target server via SSH or SMB.
   - It reads the internal registry, file system, and package manager, generating a 100% accurate list of every piece of missing software and every misconfiguration.
   - *Advantage*: This is how true enterprise network hygiene is maintained.

## 5. Important Terminology

| Term | Meaning |
|------|---------|
| **CVE** | Common Vulnerabilities and Exposures. The dictionary of known flaws (e.g., CVE-2017-0144). |
| **CVSS** | The scoring system (0.0 to 10.0) used to rank how dangerous a CVE is. |
| **False Positive** | The scanner reports a vulnerability exists, but it actually doesn't. |
| **False Negative** | The scanner reports the system is safe, but a vulnerability actually exists (Very dangerous). |
| **Patch Management** | The process of acquiring, testing, and installing software updates to fix vulnerabilities. |

## 6. Architecture / Diagram

```text
The Vulnerability Assessment Workflow

[ The Scanner ] (e.g., Nessus)
      |
      |-- 1. Logs into target Server A (Authenticated)
      |-- 2. Reads installed software list: "Java 8 Update 121"
      |
[ CVE Database ]
      |-- 3. Compares finding to database.
      |-- "Java 8 Update 121 is vulnerable to Remote Code Execution (CVSS 9.8)"
      |
[ The Report ]
      |-- 4. Generates PDF for the IT Team.
      |-- "CRITICAL: Update Java on Server A immediately."
```

## 7. Syntax / Commands / Configuration

While enterprise scanners have graphical interfaces, penetration testers often use command-line vulnerability scanning scripts built directly into Nmap (the Nmap Scripting Engine, or NSE).

```bash
# Run Nmap's standard vulnerability scanning scripts against a target
nmap --script vuln 192.168.1.10

# Example Output snippet:
# PORT    STATE SERVICE
# 445/tcp open  microsoft-ds
# | smb-vuln-ms17-010:
# |   VULNERABLE:
# |   Remote Code Execution vulnerability in Microsoft SMBv1 servers (ms17-010)
# |     State: VULNERABLE
# |     IDs:  CVE:CVE-2017-0143
```
*Note: MS17-010 is the famous "EternalBlue" vulnerability used by the WannaCry ransomware.*

## 8. Beginner Example

Imagine a Vulnerability Scanner as a Home Inspector.
You hire an inspector to look at a house before you buy it. 
- They walk around with a clipboard (the CVE Database). 
- They see a crack in the foundation and write it down (Identifying the vulnerability).
- They see exposed wiring and write it down.
- They hand you a report saying, "Fix the wiring immediately (Critical Risk), fix the crack eventually (Medium Risk)."
- **Crucial point**: The inspector does *not* pour gasoline on the exposed wiring to see if the house burns down. They just report the flaw.

## 9. Real-World Example

**Situation**: A hospital runs a monthly authenticated Nessus scan.
**Discovery**: The scanner flags a Windows server in the radiology department. The report states: "Vulnerability: MS17-010 (EternalBlue) - Critical - Patch missing."
**Complication**: The IT team realizes this server controls a million-dollar MRI machine. If they apply the Windows patch, the MRI software might crash.
**Risk**: If they don't patch it, ransomware could infect it. If they do patch it, the hospital might not be able to scan patients.
**Mitigation**: The hospital accepts the patching risk, but applies a "Compensating Control". They cannot patch the server, so they isolate it on a highly restricted VLAN, surrounded by firewalls, ensuring no other computer in the hospital can talk to it over the vulnerable SMB protocol.

## 10. What Happens Internally? (The False Positive)

A massive problem with automated scanners is the **False Positive**. 
Suppose a scanner sees a web server running `Apache 2.4.40`. The scanner knows that version is vulnerable, so it flags it as Critical.
However, the Linux administrators might have "backported" the security patch. They manually applied the code fix to the server, but intentionally did not change the version number in the banner (to avoid breaking legacy software). 

The scanner, doing an unauthenticated scan, just reads the banner, assumes it is unpatched, and screams "CRITICAL!" The security analyst must manually investigate, realize the patch *was* applied, and mark the alert as a False Positive so the IT team doesn't waste their time.

## 11. Common Mistakes

1. **Running Scans During Peak Hours**: Vulnerability scanners send massive amounts of packets. Running a full aggressive scan on a production database at 12:00 PM will likely cause the network to lag or the database to crash.
2. **Ignoring Medium/Low Vulnerabilities**: IT teams often fix the "Criticals" and ignore the rest. Hackers love this. A hacker will chain together three "Low" risk vulnerabilities (Information Disclosure + Directory Traversal + Weak Permissions) to achieve a full system compromise.
3. **The "Check-box" Mentality**: Running a scan once a year just to pass a compliance audit, then ignoring the report. Vulnerability management must be continuous.

## 12. Defensive Best Practices

1. **Scan Authenticated**: Unauthenticated scans are mostly useless for internal networks. Give the scanner credentials so it can see the truth.
2. **Prioritize by Business Context**: A Critical vulnerability on an offline test server is less urgent than a Medium vulnerability on the public-facing e-commerce web server. 
3. **Automate Patching**: Humans cannot keep up with the volume of vulnerabilities. Use tools (like SCCM or Ansible) to automatically push patches to workstations every week.
4. **Verify the Fix**: After the IT team says they applied the patch, run the vulnerability scan again to mathematically prove the vulnerability is actually gone.

## 13. Security Mindset

When analyzing a massive 500-page vulnerability report, ask:
- *Which of these vulnerabilities are "Remotely Exploitable" (Network access) vs "Locally Exploitable" (Requires physical keyboard access)? Fix the remote ones first.*
- *Is there a public exploit available for this CVE? (If a script exists on GitHub that any 12-year-old can download and run against your server, that patch goes to the front of the line).*
- *If we cannot patch this today, what Compensating Control can we put in place to block the attack path?*

## 14. Try It Yourself

Look up a CVE.
1. Open a web browser and go to `nvd.nist.gov` (National Vulnerability Database) or just search Google for `CVE-2021-44228`.
2. This is "Log4Shell", one of the worst vulnerabilities in history.
3. Look at the CVSS Score (it is a 10.0 CRITICAL).
4. Read the description. You will see it affects the Apache Log4j library and allows attackers to execute arbitrary code (Remote Code Execution). This is exactly what a scanner reads to generate its reports!
"""

m15_exercises = [
    {
        "title": "Concept Check: Scan vs Pen Test",
        "description": "Read the scenario and decide if it describes a Vulnerability Assessment or a Penetration Test.\\n\\nScenario: You run an automated tool against a network. The tool generates a 100-page PDF listing 50 missing Windows updates. You hand the PDF to the IT team.\\n\\nTask: Is this a Vulnerability Assessment or a Penetration Test?",
        "difficulty": "Beginner",
        "starter_code": "Process: ",
        "solution_code": "Vulnerability Assessment",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Vulnerability Assessment"}]
    },
    {
        "title": "Guided Lab: The Dictionary of Flaws",
        "description": "When a new vulnerability is discovered by researchers, it is assigned a unique tracking number so the entire industry can talk about it uniformly.\\n\\nTask: What is the 3-letter acronym for this dictionary of known vulnerabilities (e.g., ___-2023-12345)?",
        "difficulty": "Beginner",
        "starter_code": "Acronym: ",
        "solution_code": "CVE (Common Vulnerabilities and Exposures)",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "CVE"}]
    },
    {
        "title": "Hands-on Task: Scan Types",
        "description": "You are a defender. You want your vulnerability scanner (like Nessus) to provide a 100% accurate list of every outdated PDF reader and web browser installed on your employees' laptops.\\n\\nTask: Which scanning mode MUST you use to achieve this: Authenticated or Unauthenticated?",
        "difficulty": "Intermediate",
        "starter_code": "Mode: ",
        "solution_code": "Authenticated",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Authenticated"}]
    },
    {
        "title": "Scenario Analysis: False Positives",
        "description": "Your automated scanner flags a Linux web server as having a 'CRITICAL' vulnerability because it reads the banner: `Apache 2.2`. However, the Linux administrator insists the server is perfectly secure because they manually applied the security patch to the code last week.\\n\\nTask: What is the cybersecurity term for when a scanner incorrectly reports a vulnerability that isn't actually exploitable?",
        "difficulty": "Intermediate",
        "starter_code": "Term: ",
        "solution_code": "False Positive",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "False Positive"}]
    },
    {
        "title": "Debugging Task: Compensating Controls",
        "description": "A vulnerability scan finds a critical flaw in a legacy Windows XP machine running a factory assembly line. Microsoft no longer makes patches for Windows XP, so the vulnerability cannot be fixed. The factory cannot afford to replace the machine.\\n\\nTask: As a security engineer, describe a 'Compensating Control' (an alternative defense) you can implement to secure the machine without patching it.",
        "difficulty": "Advanced",
        "starter_code": "Control: ",
        "solution_code": "Isolate the machine from the network (Air-gap it). If it must be on the network, place it on a highly restricted VLAN behind a strict firewall that only allows it to talk to the specific internal server it needs, blocking all internet and local workstation access.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Isolate the machine from the network (Air-gap it). If it must be on the network, place it on a highly restricted VLAN behind a strict firewall that only allows it to talk to the specific internal server it needs, blocking all internet and local workstation access."}]
    },
    {
        "title": "Challenge: Vulnerability Chaining",
        "description": "A scanner finds three vulnerabilities on a web server: \\n1. Low Risk: The server reveals its internal folder structure (Information Disclosure).\\n2. Low Risk: A folder has weak permissions, allowing file uploads.\\n3. Low Risk: A script allows users to execute local files.\\n\\nTask: Explain why a human hacker might view this server as 'Critically' vulnerable, even though the automated scanner only reported 'Low' risks.",
        "difficulty": "Challenge",
        "starter_code": "Explanation: ",
        "solution_code": "Explanation: A human hacker can 'chain' these low-risk vulnerabilities together. They use the folder structure (1) to find the upload folder, upload a malicious script due to weak permissions (2), and then use the local execution script (3) to run their malware, resulting in a full system compromise. Scanners look at flaws in isolation; hackers chain them together.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Explanation: A human hacker can 'chain' these low-risk vulnerabilities together. They use the folder structure (1) to find the upload folder, upload a malicious script due to weak permissions (2), and then use the local execution script (3) to run their malware, resulting in a full system compromise. Scanners look at flaws in isolation; hackers chain them together."}]
    }
]

m15_quizzes = [
    {
        "question_text": "What is the primary difference between a Vulnerability Assessment and a Penetration Test?",
        "options": ["Vulnerability Assessments are done by hackers; Pen Tests are done by IT", "A Vulnerability Assessment automatically identifies and reports potential flaws; a Penetration Test involves a human actively attempting to exploit those flaws to prove the real-world risk", "They are exactly the same thing", "Vulnerability Assessments only scan Windows machines"],
        "correct_answer": "A Vulnerability Assessment automatically identifies and reports potential flaws; a Penetration Test involves a human actively attempting to exploit those flaws to prove the real-world risk",
        "explanation": "Scanners find the open windows. Pen testers climb through them.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "In the context of vulnerability management, what does the acronym CVE stand for?",
        "options": ["Computer Virus Elimination", "Common Vulnerabilities and Exposures", "Critical Vector Entry", "Cyber Vulnerability Engine"],
        "correct_answer": "Common Vulnerabilities and Exposures",
        "explanation": "The CVE database provides a standardized dictionary for publicly known cybersecurity vulnerabilities.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "Which type of vulnerability scan is the most accurate and produces the fewest False Positives?",
        "options": ["An Unauthenticated Scan", "A Ping Sweep", "An Authenticated Scan (where the scanner is given administrative credentials to log into the target)", "A Stealth Scan"],
        "correct_answer": "An Authenticated Scan (where the scanner is given administrative credentials to log into the target)",
        "explanation": "By logging in, the scanner can look directly at the file system and registry, rather than just guessing based on network banners.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "A scanner reports that a server is vulnerable to 'CVE-2017-0144' (EternalBlue). The IT team investigates and finds that the server was actually patched three years ago, but the scanner got confused by a custom banner. What is this scenario called?",
        "options": ["A True Positive", "A False Negative", "A False Positive", "A Zero-Day"],
        "correct_answer": "A False Positive",
        "explanation": "A False Positive is an alarm ringing when there is no fire. It wastes time, but it is better than a False Negative (a fire with no alarm).",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "What is the CVSS (Common Vulnerability Scoring System)?",
        "options": ["A tool used to scan databases", "A mathematical framework for rating the severity of a vulnerability from 0.0 to 10.0 based on its exploitability and impact", "A type of firewall configuration", "A certification for ethical hackers"],
        "correct_answer": "A mathematical framework for rating the severity of a vulnerability from 0.0 to 10.0 based on its exploitability and impact",
        "explanation": "CVSS helps IT teams prioritize which patches to apply first (e.g., fixing a 9.8 Critical before fixing a 3.2 Low).",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "Why do security professionals recommend running aggressive vulnerability scans on production systems during off-peak hours (e.g., 2:00 AM on a Sunday)?",
        "options": ["Because hackers only attack at night", "Because vulnerability scanners generate massive amounts of network traffic and aggressively test services, which can accidentally cause fragile production servers to crash or lag", "Because the CVE database is updated at night", "Because electricity is cheaper at night"],
        "correct_answer": "Because vulnerability scanners generate massive amounts of network traffic and aggressively test services, which can accidentally cause fragile production servers to crash or lag",
        "explanation": "Scanning is an inherently disruptive process. You do not want to accidentally DoS your own company during business hours.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "A critical vulnerability is found in a legacy medical device. The manufacturer says they will never release a patch for it. The hospital MUST keep using the device. What is the correct security action?",
        "options": ["Throw the device away", "Implement a Compensating Control, such as heavily restricting the device's network access using a firewall (Air-gapping or Micro-segmentation)", "Ignore the vulnerability because it's a medical device", "Change the hospital's Wi-Fi password"],
        "correct_answer": "Implement a Compensating Control, such as heavily restricting the device's network access using a firewall (Air-gapping or Micro-segmentation)",
        "explanation": "If you cannot fix the vulnerability, you must reduce the threat's ability to reach the vulnerability.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "What is the primary danger of a 'False Negative' in vulnerability scanning?",
        "options": ["It causes the IT team to waste time investigating a ghost", "It provides a false sense of security; the scanner says the system is safe, but a critical vulnerability actually exists, leaving the door wide open for attackers", "It causes the scanner to crash", "It breaks the network connection"],
        "correct_answer": "It provides a false sense of security; the scanner says the system is safe, but a critical vulnerability actually exists, leaving the door wide open for attackers",
        "explanation": "False Negatives are the worst outcome. You believe you are safe, so you stop defending.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "An automated scanner finds 5 'Low Risk' vulnerabilities on a server. An ethical hacker reads the report, smiles, and completely takes over the server in 10 minutes. How did the hacker likely do this?",
        "options": ["By using a Zero-Day", "By brute-forcing the password", "By 'chaining' the Low Risk vulnerabilities together to create an exploit path that the automated scanner lacked the logic to understand", "By rebooting the server"],
        "correct_answer": "By 'chaining' the Low Risk vulnerabilities together to create an exploit path that the automated scanner lacked the logic to understand",
        "explanation": "Automated tools lack human creativity. Chaining flaws is the hallmark of manual penetration testing.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "What is 'Patch Management'?",
        "options": ["Fixing physical holes in ethernet cables", "The systematic process of identifying, acquiring, testing, and installing software updates to fix vulnerabilities discovered by scanners", "Updating the antivirus signature database", "Managing user passwords"],
        "correct_answer": "The systematic process of identifying, acquiring, testing, and installing software updates to fix vulnerabilities discovered by scanners",
        "explanation": "Scanning is useless if you don't actually apply the patches. Patch management is the operational process of fixing the holes.",
        "difficulty": "Advanced"
    }
]


m16_lesson = """# Web Penetration Testing Concepts

## 1. What Is It?

After Reconnaissance (Module 13), Scanning (Module 14), and Vulnerability Assessment (Module 15), we reach the pinnacle of Phase 3: **Penetration Testing** (Exploitation).

Specifically, we are focusing on Web Penetration Testing. This is the manual, creative process of attempting to hack a web application exactly as a malicious attacker would, using the vulnerabilities we learned about in the OWASP Top 10 (Module 11).

The goal is not to break the application, but to *prove* that the vulnerability exists, demonstrate the business impact (e.g., "I can steal the customer database"), and provide actionable remediation advice to the developers.

## 2. Why Do We Need It?

Automated scanners (like Nessus) are dumb. They can only find known flaws with simple signatures. 

**Example 1: Business Logic Flaws**
A scanner cannot find a "Business Logic" flaw. For example, if an e-commerce site allows you to apply a $10 discount code infinitely until your cart total is negative, a scanner will never find that. Only a human penetration tester, thinking creatively, will discover it.

**Example 2: Proving the Risk**
If you tell a CEO "We have an A03: Injection flaw," they might ignore you. If a penetration tester legally exploits that flaw, extracts the CEO's personal password from the database, and puts it in a report, the CEO will immediately authorize the budget to fix it.

## 3. Where Is It Used?

- **Compliance Audits**: Banks and healthcare companies must hire external, independent penetration testers annually.
- **Bug Bounty Programs**: Companies like Google and Apple pay independent hackers to constantly try and penetrate their web apps.
- **Red Teaming**: Simulating a full-scale, stealthy cyber attack against an organization's people, processes, and technology.

## 4. How Does It Work?

A web penetration test follows a strict methodology:
1. **Planning & Scope**: The most critical step. Defining *exactly* what URLs the tester is legally allowed to attack, and what is off-limits.
2. **Recon & Enumeration**: Mapping the application, finding all input fields, URLs, and APIs (spidering/crawling).
3. **Vulnerability Analysis**: Using proxies (like Burp Suite) to intercept traffic and test for OWASP vulnerabilities (SQLi, XSS, IDOR).
4. **Exploitation**: Manually crafting malicious payloads to breach the application and extract data.
5. **Reporting**: Writing a detailed, professional document explaining the findings and how to fix them.

## 5. Important Terminology

| Term | Meaning |
|------|---------|
| **Rules of Engagement (RoE)** | The legal contract defining the scope and rules of the penetration test. |
| **Scope** | The specific IP addresses or URLs the tester is allowed to attack. |
| **Payload** | The specific piece of malicious code or data sent to exploit a vulnerability. |
| **Burp Suite** | The industry-standard web interception proxy used by penetration testers. |
| **Web Shell** | A malicious script uploaded by a hacker that allows them to run OS commands on the web server via the browser. |

## 6. Architecture / Diagram

```text
The Web Pen Testing Setup

[ Pen Tester's Browser ]
       |
       | (Configured to send all traffic through local Proxy)
       v
[ Interception Proxy (Burp Suite) ]
       |-- 1. Tester pauses the HTTP POST request.
       |-- 2. Tester manually injects an SQL payload: ' OR 1=1 --
       |-- 3. Tester clicks "Forward".
       v
[ Target Web Application ]
       |
[ Target Database ]
```

## 7. Syntax / Commands / Configuration

Penetration testers use specific **Payloads** to test for vulnerabilities.

**Testing for SQL Injection (SQLi):**
```text
# A tester will enter these characters into a login box or URL to see if the database crashes or returns an error.
'
' OR 1=1 --
" OR "a"="a
```

**Testing for Cross-Site Scripting (XSS):**
```html
<!-- A tester will enter this into a comment box. If a popup alert appears, XSS is confirmed. -->
<script>alert(1)</script>
<img src=x onerror=alert('Hacked')>
```

**Testing for Directory Traversal (LFI):**
```text
# A tester will manipulate a file-loading URL to see if they can read the Linux password file.
../../../../etc/passwd
```

## 8. Beginner Example

Imagine you are hired as a physical security tester for a bank.
- **Scanner**: You walk around and write down that the back door has a standard lock (Vulnerability Assessment).
- **Penetration Tester**: You pick the lock, walk into the bank, take a picture of the vault, and walk out, leaving a note on the manager's desk (Exploitation and Reporting). You proved the lock was not only vulnerable, but actually bypassable in the real world.

## 9. Real-World Example

**Situation**: A tester is attacking a web application that generates PDF invoices. The URL is `app.com/invoice?user_id=405`.
**Recon**: The tester intercepts the request in Burp Suite and notices the `user_id` parameter.
**Analysis**: The tester realizes this might be an Insecure Direct Object Reference (IDOR) / Broken Access Control flaw.
**Exploitation**: The tester manually changes the request in Burp Suite to `user_id=406` and forwards it to the server. The server responds with a PDF invoice belonging to a completely different customer, containing their credit card details.
**Reporting**: The tester takes a screenshot, marks it as a High severity Business Logic flaw, and advises the developers to implement backend authorization checks.

## 10. What Happens Internally? (The Web Shell)

The ultimate goal of a web penetration tester is often to achieve **RCE (Remote Code Execution)**. 
If an application allows file uploads (like a profile picture) and has weak input validation (Module 12), the tester will upload a **Web Shell**.

A Web Shell is a small piece of code (often written in scripting languages) that accepts commands via URL parameters and passes them to the operating system shell.

1. The tester saves this as `avatar.script` and uploads it.
2. The tester navigates to `app.com/uploads/avatar.script?cmd=whoami`.
3. The web server executes the code. The code takes the `cmd` variable from the URL (`whoami`) and passes it directly to the underlying OS.
4. The web page displays `www-data` (the Linux web user).
5. The tester now has complete command-line control of the web server through their browser.

## 11. Common Mistakes

1. **Attacking Out of Scope**: If the contract says you can only attack `app.target.com`, and you accidentally attack `marketing.target.com`, you have committed a cybercrime and can be sued or arrested. Scope is absolute law.
2. **Causing Denial of Service (DoS)**: Running aggressive automated exploitation tools (like SQLmap) during business hours, crashing the client's production database. Ethical hackers must operate carefully.
3. **Failing to Clean Up**: A tester uploads a web shell to prove RCE, but forgets to delete it after the test. A real hacker finds the tester's web shell a month later and uses it to breach the company.
4. **Poor Reporting**: Writing a report that only contains technical jargon. The report must explain the business risk clearly so executives understand why it matters.

## 12. Defensive Best Practices

1. **Fix the Root Cause**: When a pen tester finds XSS in a specific comment box, developers often just filter that one box. The correct defense is to implement a global Output Encoding library across the entire application.
2. **Web Application Firewall (WAF)**: Deploy a WAF (like Cloudflare or AWS WAF) in front of the application. It looks for common penetration testing payloads (like `' OR 1=1`) and blocks the IP address automatically.
3. **Least Privilege**: If a tester uploads a Web Shell, limit the damage. The web server process (`www-data`) should absolutely not have permission to read `/etc/shadow` or execute root-level commands.
4. **Regular Testing**: Web applications change daily. A penetration test from 2 years ago is meaningless today.

## 13. Security Mindset

When conducting a penetration test, the mindset is "Abuse of Functionality":
- *The developer built this 'Forgot Password' feature to help users.*
- *How can I abuse it?*
- *Can I request a password reset for the Admin user, intercept the email using a proxy, or brute-force the 4-digit reset token because it doesn't expire?*
- *The application is working exactly as coded, but I am forcing the code down a path the developer didn't anticipate.*

## 14. Try It Yourself

(This is a safe, mental exercise)
Look at the URL of this webpage, or any page you visit today.
Does it end in a number? (e.g., `article?id=15`)
Imagine you are an ethical hacker. The very first thing you should think is: "What happens if I change `15` to `16`? What happens if I change `15` to `-1`? What happens if I change `15` to `15 OR 1=1`?"
This constant curiosity and manipulation of inputs is the core of web penetration testing.
"""

m16_exercises = [
    {
        "title": "Concept Check: Scope",
        "description": "Read the scenario and identify the critical error.\\n\\nScenario: An ethical hacker is hired to test `api.company.com`. While scanning, they discover that `database.company.com` is wide open and highly vulnerable. They decide to hack into the database to show the client how dangerous it is.\\n\\nTask: What absolute rule of penetration testing did the hacker just violate, potentially committing a crime?",
        "difficulty": "Beginner",
        "starter_code": "Violated rule: ",
        "solution_code": "They attacked out of Scope (or violated the Rules of Engagement).",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "They attacked out of Scope (or violated the Rules of Engagement)."}]
    },
    {
        "title": "Guided Lab: The Interception Proxy",
        "description": "To test web applications, hackers do not use a standard browser alone. They use a tool that sits between the browser and the internet to pause and modify HTTP requests.\\n\\nTask: Name the industry-standard software tool most commonly used for this purpose (mentioned in the lesson).",
        "difficulty": "Beginner",
        "starter_code": "Tool Name: ",
        "solution_code": "Burp Suite",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Burp Suite"}]
    },
    {
        "title": "Hands-on Task: XSS Payload Identification",
        "description": "You are reviewing web logs and see the following input submitted to a search bar: `<script>alert('Test')</script>`\\n\\nTask: What specific type of vulnerability is the penetration tester attempting to find using this payload?",
        "difficulty": "Intermediate",
        "starter_code": "Vulnerability: ",
        "solution_code": "Cross-Site Scripting (XSS)",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Cross-Site Scripting (XSS)"}]
    },
    {
        "title": "Scenario Analysis: The Logic Flaw",
        "description": "A penetration tester is testing an airline ticketing system. They discover they can purchase a $500 ticket, intercept the request in Burp Suite, change the 'price' parameter to '$5', and the server issues a valid ticket.\\n\\nTask: Why would an automated Vulnerability Scanner (like Nessus) NEVER find this specific vulnerability?",
        "difficulty": "Intermediate",
        "starter_code": "Reason: ",
        "solution_code": "Because this is a Business Logic flaw, not a missing security patch. Scanners only look for known CVE signatures (like outdated software). They do not understand the human logic of how an application is supposed to function.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Because this is a Business Logic flaw, not a missing security patch. Scanners only look for known CVE signatures (like outdated software). They do not understand the human logic of how an application is supposed to function."}]
    },
    {
        "title": "Debugging Task: The Web Shell",
        "description": "A penetration tester successfully uploads a script to the web server's images folder. They navigate to `site.com/images/shell.script?cmd=cat /etc/passwd`.\\n\\nTask: Explain exactly how this achieves Remote Code Execution (RCE) by connecting the HTTP request to the Operating System.",
        "difficulty": "Advanced",
        "starter_code": "Explanation: ",
        "solution_code": "The web server processes the uploaded code. The code takes the value of the 'cmd' parameter from the URL (`cat /etc/passwd`), passes it directly to the underlying Linux OS system function, executes the Linux command, and returns the output to the web browser.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "The web server processes the uploaded code. The code takes the value of the 'cmd' parameter from the URL (`cat /etc/passwd`), passes it directly to the underlying Linux OS system function, executes the Linux command, and returns the output to the web browser."}]
    },
    {
        "title": "Challenge: Blind SQL Injection",
        "description": "A tester enters `' OR 1=1 -- ` into a login box. The database does NOT crash, and it does NOT return a database error message. It just says 'Invalid Login'. However, the tester notices the webpage took exactly 10 seconds to load after they injected the payload, whereas it usually takes 0.1 seconds.\\n\\nTask: Based on the time delay, what specific type of SQL Injection has the tester likely discovered?",
        "difficulty": "Challenge",
        "starter_code": "Type of SQLi: ",
        "solution_code": "Blind SQL Injection (specifically, Time-Based Blind SQLi). The database executes the payload (e.g., `SLEEP(10)`) even though it doesn't display the results on the screen, proving it is vulnerable.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Blind SQL Injection (specifically, Time-Based Blind SQLi). The database executes the payload (e.g., `SLEEP(10)`) even though it doesn't display the results on the screen, proving it is vulnerable."}]
    }
]

m16_quizzes = [
    {
        "question_text": "What is the primary purpose of a Penetration Test?",
        "options": ["To install antivirus software on the client's computers", "To manually simulate a real-world cyber attack to prove whether vulnerabilities can actually be exploited and to demonstrate the business impact", "To automatically scan for missing Windows updates", "To steal money from the client"],
        "correct_answer": "To manually simulate a real-world cyber attack to prove whether vulnerabilities can actually be exploited and to demonstrate the business impact",
        "explanation": "Pen testing proves the risk is real, moving it from a theoretical scanner warning to a demonstrable breach.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "In penetration testing, what is the 'Scope'?",
        "options": ["The tool used to view network traffic", "The strict, legally defined list of IP addresses, URLs, and systems the tester is allowed to attack", "The amount of money the tester is paid", "The type of malware used"],
        "correct_answer": "The strict, legally defined list of IP addresses, URLs, and systems the tester is allowed to attack",
        "explanation": "Attacking anything outside the agreed-upon Scope is unauthorized access, which is a cybercrime.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "Which software tool is considered the industry standard for intercepting and modifying HTTP traffic during a web penetration test?",
        "options": ["Microsoft Word", "Burp Suite", "Nmap", "Wireshark"],
        "correct_answer": "Burp Suite",
        "explanation": "Burp Suite (and OWASP ZAP) acts as a local proxy, allowing the tester to manipulate the raw HTTP requests before they reach the server.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "Why must a penetration tester carefully clean up their environment (e.g., delete test accounts, remove uploaded files) at the end of an engagement?",
        "options": ["To save hard drive space on their own computer", "Because leaving a Web Shell or a backdoor on the client's server creates a massive vulnerability that real attackers could find and use later", "To ensure the client doesn't know they were there", "Because it is required by HTML standards"],
        "correct_answer": "Because leaving a Web Shell or a backdoor on the client's server creates a massive vulnerability that real attackers could find and use later",
        "explanation": "Ethical hackers must leave the system in the exact state (or better) than they found it.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "A penetration tester intercepts an e-commerce checkout request and changes the `item_price` parameter from `100.00` to `1.00`. The server accepts it. What type of vulnerability is this?",
        "options": ["SQL Injection", "A Business Logic Flaw", "Cross-Site Scripting (XSS)", "A Zero-Day"],
        "correct_answer": "A Business Logic Flaw",
        "explanation": "The code executed perfectly without crashing. The flaw is in the logical design (trusting the client to dictate the price).",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "What is a 'Payload' in the context of web exploitation?",
        "options": ["The cost of the penetration test", "The amount of data a server can hold", "The specific string of malicious data or code (like `<script>alert(1)</script>`) sent to the target to exploit a vulnerability", "The encrypted password"],
        "correct_answer": "The specific string of malicious data or code (like `<script>alert(1)</script>`) sent to the target to exploit a vulnerability",
        "explanation": "Testers inject payloads to see how the application reacts.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "A tester uploads a script file called `shell.script` to a web server. When they navigate to it, it allows them to type Linux commands (like `ls` or `whoami`) directly into the browser, and the server executes them. What is this called?",
        "options": ["A Web Shell (resulting in Remote Code Execution)", "A SQL Injection", "A Denial of Service", "A Firewall"],
        "correct_answer": "A Web Shell (resulting in Remote Code Execution)",
        "explanation": "A web shell bridges the gap between the web application and the underlying operating system, providing full control.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "Why is the 'Reporting' phase often considered the most important part of a penetration test?",
        "options": ["Because it is the only part the tester gets paid for", "Because if the client (executives and developers) cannot understand the business risk and the technical remediation steps, the vulnerabilities will never get fixed", "Because it generates a CVSS score", "Because it encrypts the network"],
        "correct_answer": "Because if the client (executives and developers) cannot understand the business risk and the technical remediation steps, the vulnerabilities will never get fixed",
        "explanation": "A pen test is useless if it doesn't result in improved security posture. The report drives the change.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "A tester submits `' OR 1=1 -- ` into a search bar. Instead of logging them in, the webpage crashes and displays a detailed stack trace showing a MySQL syntax error. What has the tester proven?",
        "options": ["That the website is secure", "That the application is vulnerable to SQL Injection, and it suffers from Verbose Error Messages (Information Leakage)", "That the database is turned off", "That the server is using HTTPS"],
        "correct_answer": "That the application is vulnerable to SQL Injection, and it suffers from Verbose Error Messages (Information Leakage)",
        "explanation": "The database crash proves the input was evaluated as code, not data. The error message gives the tester a map of the backend.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "If a penetration tester discovers a vulnerability on a live production database during business hours, what should they generally avoid doing?",
        "options": ["Writing it down in the report", "Using an automated exploitation tool (like SQLmap) to dump the entire database, because aggressive automated tools can easily crash the fragile production server and cause a Denial of Service", "Telling the client about it", "Checking the CVSS score"],
        "correct_answer": "Using an automated exploitation tool (like SQLmap) to dump the entire database, because aggressive automated tools can easily crash the fragile production server and cause a Denial of Service",
        "explanation": "Ethical hackers must prioritize Availability (the 'A' in the CIA triad). Proving the flaw exists is enough; you don't need to destroy the server to prove it.",
        "difficulty": "Advanced"
    }
]


m17_lesson = """# Network Security & Packet Analysis

## 1. What Is It?

While Web Security focuses on the application layer (HTTP/Browsers), **Network Security** focuses on the infrastructure that carries the data: the cables, routers, switches, and firewalls. 

**Packet Analysis** is the core skill of network security. A network packet is a tiny envelope of data traveling across a wire. Packet Analysis (or Packet Sniffing) involves capturing these envelopes as they fly by, opening them, and reading both the headers (To/From addresses) and the payload (the actual data).

Defenders use packet analysis to prove that an attack is happening. Attackers use it to spy on unencrypted traffic.

## 2. Why Do We Need It?

**Example 1: The Invisible Attacker**
A hacker successfully breaches a web server, installs malware, and clears all the server logs. If you only look at the server, everything looks fine. However, the malware is quietly sending stolen database records to a server in Russia. If you analyze the network packets leaving your router, you will catch the thief red-handed, regardless of what the server logs say. "Packets don't lie."

**Example 2: Troubleshooting**
A user complains they cannot reach `google.com`. The IT team captures packets and sees the user's computer sending a DNS request, but no DNS response is coming back. The problem isn't the web browser; it's the DNS server.

## 3. Where Is It Used?

- **Intrusion Detection Systems (IDS)**: Automated systems that read millions of packets per second looking for malicious signatures.
- **Incident Response**: When a breach occurs, analysts look at historical packet captures (PCAPs) to figure out exactly what the attacker stole.
- **Man-in-the-Middle (MitM) Attacks**: Hackers sit on a public Wi-Fi network and analyze all passing packets to steal passwords.

## 4. How Does It Work?

Data doesn't travel across the internet in one giant piece. It is chopped into thousands of tiny **Packets**.

Each packet has layers (following the OSI or TCP/IP model):
1. **Ethernet Layer**: Contains the MAC addresses (Physical hardware addresses).
2. **IP Layer**: Contains the Source and Destination IP addresses (Where is it going on the internet?).
3. **TCP/UDP Layer**: Contains the Source and Destination Ports (Which specific application should receive this data?).
4. **Application Layer**: Contains the actual payload (e.g., The HTML code of a webpage).

A packet analyzer captures this raw electrical data from the network card and translates it back into human-readable text.

## 5. Important Terminology

| Term | Meaning |
|------|---------|
| **Wireshark** | The industry-standard graphical tool for packet analysis. |
| **PCAP** | Packet Capture. A file extension (`.pcap`) used to save recorded network traffic. |
| **Sniffing** | The act of capturing packets off a network wire or Wi-Fi airwaves. |
| **Promiscuous Mode** | A network card setting that forces it to capture *all* packets on the wire, not just the ones addressed to it. |
| **Cleartext** | Unencrypted data. If you sniff cleartext (like HTTP or Telnet), you can read the passwords perfectly. |

## 6. Architecture / Diagram

```text
The Packet Sniffing Process

[ User A ] --(Sends 'Password123' via HTTP)--> [ Switch ] -----> [ Web Server ]
                                                  |
                                                  | (Port Mirroring)
                                                  v
                                          [ Security Analyst ]
                                          (Running Wireshark)
```
*Note: In an unencrypted HTTP connection, the analyst sees `Password123` perfectly in Wireshark. In an encrypted HTTPS connection, the analyst still sees the packet, but the payload looks like `x9!f@z...` (gibberish).*

## 7. Syntax / Commands / Configuration

While Wireshark is the graphical standard, **Tcpdump** is the command-line standard used on almost all Linux servers.

```bash
# Capture packets on the eth0 network interface and save to a file
tcpdump -i eth0 -w evidence.pcap

# Read the file later, filtering only for traffic going to port 80 (HTTP)
tcpdump -r evidence.pcap port 80

# Wireshark Display Filter Syntax:
# Show me only packets where the source IP is 192.168.1.10
ip.src == 192.168.1.10

# Show me only unencrypted HTTP POST requests (often containing passwords)
http.request.method == "POST"
```

## 8. Beginner Example

Imagine a busy post office.
- Normal operation: A mail worker (the network card) only looks at letters (packets) addressed to them, and ignores the rest.
- **Promiscuous Mode**: A rogue mail worker decides to make a photocopy of every single letter that passes through the building before sending it on its way. 
- **Packet Analysis**: The rogue worker goes home, opens the photocopied letters, and reads everyone's mail. If the letter is written in standard English (HTTP), they read the secrets. If the letter is written in a secret code (HTTPS), they know *who* sent it, but not *what* it says.

## 9. Real-World Example

**Situation**: An employee is working at a coffee shop on public Wi-Fi.
**Weakness**: The employee logs into an older corporate web portal that uses standard HTTP instead of encrypted HTTPS.
**Threat**: A hacker is sitting at the next table, running Wireshark with their Wi-Fi card in promiscuous mode (Monitor mode).
**Risk**: Because Wi-Fi travels through the air, the hacker's antenna physically receives the electrical signals of the employee's packets.
**Impact**: The hacker opens the HTTP packet in Wireshark and reads the employee's corporate username and password in cleartext.
**Mitigation**: The corporation MUST force HTTPS on all web portals. Alternatively, the employee must use a VPN, which encrypts all packets before they leave the laptop, making them useless to the hacker in the coffee shop.

## 10. What Happens Internally? (The Three-Way Handshake)

When you analyze a PCAP file of someone visiting a website, you don't just see the website data. You see the strict mathematical rules of the internet.

Before a browser can ask for a webpage, it must establish a reliable TCP connection using the **Three-Way Handshake**:
1. **Packet 1 (SYN)**: Browser says to Server, "Hello, I want to talk to you. My sequence number is 0."
2. **Packet 2 (SYN-ACK)**: Server replies, "I acknowledge your 0 (ACK 1), and I agree to talk. My sequence number is 0."
3. **Packet 3 (ACK)**: Browser replies, "I acknowledge your 0 (ACK 1). We are connected."

Only after this strict 3-packet dance does Packet 4 (the actual HTTP GET request for the webpage) occur. Analysts look for broken handshakes to detect network attacks (like SYN Floods).

## 11. Common Mistakes

1. **Sniffing the wrong interface**: A server might have three network cards (eth0, eth1, eth2). If you run tcpdump on eth0 but the attack is happening on eth1, your PCAP file will be completely empty.
2. **Drowning in Data**: A busy network generates Gigabytes of packets per minute. Trying to scroll through Wireshark without using Display Filters is impossible. You must know exactly what IP or Port you are looking for.
3. **Assuming encryption hides everything**: HTTPS hides the *payload*. It does NOT hide the Source IP, Destination IP, or the volume of traffic. If a PCAP shows your database server sending 500GB of encrypted HTTPS traffic to an unknown IP in North Korea at 3:00 AM, you are still breached, even if you can't read the payload.

## 12. Defensive Best Practices

1. **Encrypt Everything (TLS/VPN)**: The absolute best defense against packet sniffing is encryption. If attackers capture the packets, make sure they only see mathematical gibberish.
2. **Network Segmentation**: Don't put the marketing team's laptops on the same physical switch as the HR database. If a marketing laptop gets hacked, the attacker shouldn't even be able to "see" the HR packets flying by.
3. **Deploy a NIDS**: A Network Intrusion Detection System (like Snort or Suricata) is basically an automated Wireshark that runs 24/7, matching packets against a database of known malware signatures and alerting you instantly.
4. **Retain PCAPs**: Store network traffic logs for at least 30 days. When a breach happens, these logs are the only way to prove exactly what data left the building.

## 13. Security Mindset

When analyzing a packet capture, ask:
- *Why is a workstation communicating directly with another workstation? Workstations should only talk to servers.*
- *I see a DNS request for `www.jhgfjhgfd.com`. Humans don't type domains like that. Is that a piece of malware trying to phone home to a randomly generated command-and-control server?*
- *Is this traffic normal for this time of day?*

## 14. Try It Yourself

(Mental Exercise / Home Lab)
If you install Wireshark on your home PC:
1. Open Wireshark and select your Wi-Fi or Ethernet interface.
2. Click the "Shark Fin" icon to start capturing.
3. Open a web browser and go to `neverssl.com` (a site that intentionally does not use encryption).
4. Stop the capture in Wireshark.
5. In the display filter at the top, type `http`. 
6. Find the packet that says "GET /". Click it. In the bottom pane, you can read the exact raw, cleartext HTTP request your browser sent, and the exact HTML the server sent back.
"""

m17_exercises = [
    {
        "title": "Concept Check: Web vs Network Security",
        "description": "Read the scenario and identify the domain.\\n\\nScenario: You are investigating a breach. The web server logs are completely deleted. You turn to the core network router and pull a historical log of all the raw data (envelopes) that passed through the cables to see where the stolen data went.\\n\\nTask: Are you performing Web Security analysis or Network Security Packet Analysis?",
        "difficulty": "Beginner",
        "starter_code": "Domain: ",
        "solution_code": "Network Security Packet Analysis",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Network Security Packet Analysis"}]
    },
    {
        "title": "Guided Lab: Cleartext Protocols",
        "description": "A hacker is sniffing a public Wi-Fi network. They capture traffic from two users. User A is using HTTPS. User B is using standard HTTP.\\n\\nTask: Which user's passwords will the hacker be able to read perfectly in plain English?",
        "difficulty": "Beginner",
        "starter_code": "Vulnerable User: ",
        "solution_code": "User B (HTTP is cleartext, meaning unencrypted).",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "User B (HTTP is cleartext, meaning unencrypted)."}]
    },
    {
        "title": "Hands-on Task: Wireshark Filtering",
        "description": "You open a massive 10GB PCAP file in Wireshark containing millions of packets. You only want to see the packets that originated from the suspected hacker's IP address: `10.0.0.5`.\\n\\nTask: Write the specific Wireshark Display Filter syntax to only show packets where the source IP is exactly `10.0.0.5`.",
        "difficulty": "Intermediate",
        "starter_code": "Display Filter: ",
        "solution_code": "ip.src == 10.0.0.5",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "ip.src == 10.0.0.5"}]
    },
    {
        "title": "Scenario Analysis: Encryption Limits",
        "description": "An employee uses a highly secure, encrypted VPN connection to transfer a stolen, proprietary database to an offshore server. You capture the network packets using Wireshark.\\n\\nTask: You cannot read the payload (because of the VPN encryption). What two critical pieces of information CAN you still read in the IP header to prove the employee did something suspicious?",
        "difficulty": "Intermediate",
        "starter_code": "Information 1: \\nInformation 2: ",
        "solution_code": "Information 1: The Source and Destination IP addresses (showing the employee's computer talking to a foreign server).\\nInformation 2: The volume of traffic (e.g., proving that 50GB of data left the building, matching the size of the database).",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Information 1: The Source and Destination IP addresses (showing the employee's computer talking to a foreign server).\\nInformation 2: The volume of traffic (e.g., proving that 50GB of data left the building, matching the size of the database)."}]
    },
    {
        "title": "Debugging Task: The Missing Packets",
        "description": "A Linux web server is under attack. The server has two network cards: `eth0` (connected to the internet) and `eth1` (connected to the internal backup drive). You SSH into the server and type `tcpdump -i eth1 -w attack.pcap`. You let it run for an hour, but the PCAP file shows zero attack traffic.\\n\\nTask: What mistake did you make in your command?",
        "difficulty": "Advanced",
        "starter_code": "Mistake: ",
        "solution_code": "Mistake: You told tcpdump to listen on the wrong interface (`-i eth1`). The attack is coming from the internet, so you should have told tcpdump to listen on `eth0`.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Mistake: You told tcpdump to listen on the wrong interface (`-i eth1`). The attack is coming from the internet, so you should have told tcpdump to listen on `eth0`."}]
    },
    {
        "title": "Challenge: TCP State Analysis",
        "description": "You are analyzing a PCAP file in Wireshark. You see a packet from an external IP with the `SYN` flag set. Immediately after, you see a packet from your internal web server replying with an `RST` (Reset) flag. There is no `SYN-ACK` packet.\\n\\nTask: Based on your knowledge of the TCP Three-Way Handshake and port scanning, what exactly just happened?",
        "difficulty": "Challenge",
        "starter_code": "Explanation: ",
        "solution_code": "Explanation: An external scanner probed a port on your web server. Because the internal server replied with an RST instead of a SYN-ACK, it proves that the specific port the attacker probed is CLOSED.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Explanation: An external scanner probed a port on your web server. Because the internal server replied with an RST instead of a SYN-ACK, it proves that the specific port the attacker probed is CLOSED."}]
    }
]

m17_quizzes = [
    {
        "question_text": "What is the primary function of a tool like Wireshark?",
        "options": ["To encrypt hard drives", "To capture, analyze, and translate raw network packets flying across a wire into a human-readable format", "To scan web applications for SQL Injection", "To physically connect two computers together"],
        "correct_answer": "To capture, analyze, and translate raw network packets flying across a wire into a human-readable format",
        "explanation": "Wireshark is the undisputed industry standard for graphical packet analysis and network troubleshooting.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "When an analyst captures network traffic and saves it to a file for later analysis, what is the standard file extension used?",
        "options": [".exe", ".txt", ".pcap (Packet Capture)", ".html"],
        "correct_answer": ".pcap (Packet Capture)",
        "explanation": "PCAP files are universally recognized by almost all network security tools (Wireshark, tcpdump, Snort).",
        "difficulty": "Beginner"
    },
    {
        "question_text": "If a hacker is sitting in a coffee shop sniffing the Wi-Fi, which of the following protocols would allow them to read your passwords perfectly in plain text?",
        "options": ["HTTPS", "SSH", "HTTP", "WPA3"],
        "correct_answer": "HTTP",
        "explanation": "HTTP (and older protocols like Telnet or FTP) do not encrypt the payload. The data is sent in cleartext.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "To capture packets that are NOT specifically addressed to your computer on a network, what setting must your network interface card (NIC) be placed in?",
        "options": ["Stealth Mode", "Promiscuous Mode", "Active Mode", "Passive Mode"],
        "correct_answer": "Promiscuous Mode",
        "explanation": "Promiscuous mode forces the NIC to process every single electrical frame it sees, regardless of the destination MAC address.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "What is `tcpdump`?",
        "options": ["A tool to delete databases", "The command-line equivalent of Wireshark, primarily used on Linux servers to capture packets", "A type of firewall rule", "A protocol for sending emails"],
        "correct_answer": "The command-line equivalent of Wireshark, primarily used on Linux servers to capture packets",
        "explanation": "Linux servers usually don't have graphical interfaces, so security engineers use `tcpdump` in the terminal to capture traffic.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "In Wireshark, if you want to filter a massive packet capture to ONLY show traffic destined for a web server (Port 80), what is the correct display filter?",
        "options": ["port 80", "tcp.port == 80", "show me web traffic", "filter port=80"],
        "correct_answer": "tcp.port == 80",
        "explanation": "Wireshark uses specific dot-notation syntax for display filters.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "A security analyst is reviewing a PCAP file and notices a perfectly formed TCP Three-Way Handshake (SYN, SYN-ACK, ACK) followed immediately by a massive transfer of encrypted data to a foreign IP address. What does this tell the analyst?",
        "options": ["The connection failed", "The firewall successfully blocked the attack", "A successful, reliable connection was established, and data was exfiltrated", "The attacker used a stealth scan"],
        "correct_answer": "A successful, reliable connection was established, and data was exfiltrated",
        "explanation": "The completed 3-way handshake proves the firewall allowed the connection and both computers agreed to communicate.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "Why is packet analysis considered the ultimate source of truth during an incident response investigation?",
        "options": ["Because 'Packets don't lie.' An attacker can delete logs on a hacked server to hide their tracks, but they cannot delete the physical network packets that already passed through the core router.", "Because packet analysis is legally required", "Because Wireshark is free", "Because packets contain the hacker's real name"],
        "correct_answer": "Because 'Packets don't lie.' An attacker can delete logs on a hacked server to hide their tracks, but they cannot delete the physical network packets that already passed through the core router.",
        "explanation": "Network telemetry (PCAPs and NetFlow) provides an unalterable historical record of what actually happened on the wire.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "Even if an attacker uses strong encryption (like a VPN or HTTPS) to steal data, what critical intelligence can a defender STILL gather by analyzing the packets?",
        "options": ["The exact passwords used", "The contents of the stolen files", "The Source IP, Destination IP, Port numbers, and the total volume (size) of the data transferred", "The name of the malware used"],
        "correct_answer": "The Source IP, Destination IP, Port numbers, and the total volume (size) of the data transferred",
        "explanation": "Encryption hides the payload, but the routing metadata (the outside of the envelope) must remain unencrypted for the internet to work.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "What does a Network Intrusion Detection System (NIDS) like Snort do?",
        "options": ["It automatically patches vulnerable servers", "It performs continuous, automated packet analysis, comparing passing packets to a database of known malware signatures to generate alerts", "It encrypts the entire network", "It acts as a Web Application Firewall"],
        "correct_answer": "It performs continuous, automated packet analysis, comparing passing packets to a database of known malware signatures to generate alerts",
        "explanation": "A NIDS is essentially an automated Wireshark working at wire-speed to spot malicious patterns.",
        "difficulty": "Advanced"
    }
]


m18_lesson = """# Malware Concepts & Defensive Analysis

## 1. What Is It?

**Malware** (Malicious Software) is any code written with the intent to cause harm, steal data, or gain unauthorized access. 

While penetration testing (Module 16) relies heavily on exploiting misconfigurations and logic flaws manually, a vast amount of cybercrime relies on delivering pre-packaged malware to a victim. 

**Defensive Analysis** (or Malware Analysis) is the highly specialized skill of safely dissecting a captured piece of malware to understand exactly how it works, what it communicates with, and how to build defenses against it.

## 2. Why Do We Need It?

**Example 1: Ransomware**
A hospital's computers suddenly encrypt all patient records, and the screen demands $1,000,000 in Bitcoin to unlock them. This is Ransomware. Understanding how this specific malware spreads (e.g., via phishing emails or network exploits) is critical to stopping it from infecting the rest of the hospital.

**Example 2: The Reverse Engineer**
When a new virus hits the world (like WannaCry), security analysts must figure out how to stop it. They isolate the virus in a secure lab, reverse-engineer the code, and discover the "kill switch" domain it tries to contact. By registering that domain, they neuter the malware globally.

## 3. Where Is It Used?

- **Endpoint Detection & Response (EDR)**: Next-generation antivirus (like CrowdStrike or SentinelOne) that hunts for malware behavior on laptops.
- **Incident Response (IR)**: Analyzing the malware left behind after a breach to determine exactly what the attackers stole.
- **Threat Intelligence**: Companies dissect malware to attribute attacks to specific nation-state hacker groups (e.g., APT29 in Russia).

## 4. How Does It Work?

Malware comes in many specific flavors based on its primary function:

1. **Virus**: Infects legitimate files and requires a human to execute it (e.g., double-clicking an infected Word document).
2. **Worm**: Self-replicating. It scans the network, finds a vulnerable machine, exploits it, and copies itself without any human interaction.
3. **Trojan**: Disguises itself as legitimate software (like a free video game) to trick the user into installing it. It often opens a backdoor.
4. **Ransomware**: Encrypts files and demands payment for the decryption key.
5. **Spyware / Keylogger**: Silently records keystrokes (stealing passwords) and monitors screen activity.
6. **Rootkit**: Buries itself deep into the core Operating System (the kernel) to hide from antivirus software entirely.

## 5. Important Terminology

| Term | Meaning |
|------|---------|
| **Malware** | Broad term for any malicious software. |
| **C2 (Command and Control)** | The external server controlled by the hacker that the malware "phones home" to for instructions. |
| **Sandbox** | An isolated, heavily monitored virtual machine used to safely detonate and observe malware. |
| **Static Analysis** | Analyzing the malware code *without* running it (looking at strings and hashes). |
| **Dynamic Analysis** | Running the malware in a Sandbox and watching what it does (what files it deletes, what IPs it contacts). |

## 6. Architecture / Diagram

```text
The Command and Control (C2) Architecture

[ Hacker's Server (C2) ] <----------------- (Encrypted instructions)
           |                                         ^
           v                                         |
[ Infected Laptop A ] (Sends 'I am ready' heartbeat) |
[ Infected Laptop B ] -------------------------------+
[ Infected Laptop C ]

*Once thousands of laptops are infected, they form a "Botnet". 
The hacker can use the C2 server to order the entire Botnet 
to launch a massive DDoS attack against a single target.*
```

## 7. Syntax / Commands / Configuration

**Static Analysis Tools**
Before running malware, analysts extract basic information from the file.
```bash
# Get the unique fingerprint (hash) of the file
sha256sum suspected_malware.exe

# Extract all human-readable text from the binary file
# This often reveals hardcoded IP addresses or passwords
strings suspected_malware.exe | grep "http"
```

## 8. Beginner Example

Think of malware like real-world biological threats:
- **Virus**: You catch a cold because you shook hands with someone sick (Human interaction required).
- **Worm**: An airborne virus that infects everyone in the room automatically through the ventilation system (Self-replicating, no interaction).
- **Trojan**: The story of Troy. You bring a beautiful wooden horse (a free movie download) inside your castle walls, and at midnight, soldiers (malware) climb out and open the gates.

## 9. Real-World Example

**Situation**: The Stuxnet Worm (2010).
**Weakness**: Iranian nuclear centrifuges were air-gapped (not connected to the internet), but engineers used USB flash drives.
**Threat**: A highly sophisticated nation-state worm.
**Risk & Impact**: The worm was introduced via an infected USB drive. Because it was a *worm*, it silently copied itself across the internal network. It was specifically programmed to look for Siemens industrial control software. When it found it, it caused the physical centrifuges to spin out of control and destroy themselves, while sending fake "Everything is fine" signals to the operators' monitors.
**Defensive Analysis**: When security researchers finally captured Stuxnet, they had to use deep reverse engineering (Static and Dynamic Analysis) to unravel the incredibly complex, zero-day exploits it used.

## 10. What Happens Internally? (Fileless Malware)

Traditional antivirus software works by scanning the hard drive for files (`.exe`) that match known bad signatures.

Modern attackers use **Fileless Malware** to bypass this.
1. The user clicks a phishing link.
2. The link executes a command that tells the computer's built-in memory (RAM) to download a script directly from the internet and run it in memory.
3. No `.exe` file is ever saved to the hard drive.
4. Traditional antivirus scans the hard drive, finds nothing, and reports the system is clean, while the malware is actively running in RAM.

Defenders must use modern EDR tools that monitor *behavior* (e.g., "Why is Microsoft Word trying to launch a PowerShell script to download a file from Russia?") rather than just scanning files on disk.

## 11. Common Mistakes

1. **Relying Solely on Signature Antivirus**: Assuming that because Windows Defender says a file is clean, it is safe. Attackers use "packers" to mathematically scramble the malware just enough so the signature changes, instantly bypassing old-school antivirus.
2. **Detonating Malware on the Host**: A junior analyst tries to analyze malware by double-clicking it on their actual work laptop, instantly infecting the corporate network. (ALWAYS use an isolated Sandbox).
3. **Paying the Ransom**: When hit with ransomware, companies pay the hacker, expecting the decryption key. Often, the hacker just takes the money and runs, or leaves a backdoor to ransom them again next month.

## 12. Defensive Best Practices

1. **Endpoint Detection and Response (EDR)**: Upgrade from traditional antivirus to EDR tools that analyze behavior, memory, and process trees.
2. **Offline Backups**: The ultimate defense against Ransomware is a completely offline (air-gapped) backup. If the backup is connected to the network, the ransomware will encrypt the backup too.
3. **Application Whitelisting**: Instead of trying to block millions of known bad programs, configure critical servers to *only* allow 10 specific, pre-approved programs to run. Everything else is blocked by default.
4. **Sandboxing**: Train analysts to only handle suspected malware in strict, non-networked virtual machines (like Cuckoo Sandbox).

## 13. Security Mindset

When performing basic malware analysis, ask:
- *Static Analysis: If I run the `strings` command on this file, do I see any URLs or IP addresses it might try to contact?*
- *Dynamic Analysis: When I run this file in the Sandbox, does it immediately try to disable the Windows Firewall or delete Volume Shadow Copies (backups)?*
- *What is the persistence mechanism? (How does this malware ensure it starts running again if the user reboots their computer? Did it add a Registry Key?)*

## 14. Try It Yourself

You can safely perform Static Analysis on any file.
If you receive a highly suspicious email with an attachment (like an invoice.pdf):
1. **DO NOT OPEN IT.**
2. Save the file to your computer.
3. Open a web browser and go to `VirusTotal.com`.
4. Upload the suspicious file (or just search its Hash).
5. VirusTotal will analyze the file against 70 different antivirus engines simultaneously and show you if the security community considers it malicious. You just performed basic threat intelligence!
"""

m18_exercises = [
    {
        "title": "Concept Check: Virus vs Worm",
        "description": "Read the scenario and identify the malware classification.\\n\\nScenario: A piece of malware enters a corporate network. Within 5 minutes, without any employee clicking anything, it scans the network, finds 50 other vulnerable computers, and infects them all automatically.\\n\\nTask: Is this malware a Virus or a Worm?",
        "difficulty": "Beginner",
        "starter_code": "Classification: ",
        "solution_code": "Worm",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Worm"}]
    },
    {
        "title": "Guided Lab: Ransomware Defenses",
        "description": "Ransomware encrypts all files on a network, including network-attached backup drives.\\n\\nTask: What is the only guaranteed way to ensure your backups survive a highly aggressive ransomware infection?",
        "difficulty": "Beginner",
        "starter_code": "Defense: ",
        "solution_code": "Maintain Offline (or Air-gapped / Immutable) backups that are not physically connected to the network.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Maintain Offline (or Air-gapped / Immutable) backups that are not physically connected to the network."}]
    },
    {
        "title": "Hands-on Task: Static Analysis",
        "description": "You capture a suspicious executable file. You want to see if the hacker accidentally left hardcoded IP addresses or web URLs inside the binary code without actually running the file.\\n\\nTask: What standard Linux command-line tool extracts human-readable text from binary files?",
        "difficulty": "Intermediate",
        "starter_code": "Command: ",
        "solution_code": "strings",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "strings"}]
    },
    {
        "title": "Scenario Analysis: Fileless Malware",
        "description": "An antivirus program is configured to scan the `C:\\` drive every night for known malicious `.exe` files. However, an attacker uses a PowerShell script to inject malicious code directly into the computer's active memory (RAM). No file is ever saved to the hard drive.\\n\\nTask: Why will the traditional antivirus completely fail to detect this attack, and what is this attack called?",
        "difficulty": "Intermediate",
        "starter_code": "Why it fails: \\nAttack Name: ",
        "solution_code": "Why it fails: Traditional AV only scans files physically written to the disk (hard drive). It does not scan active memory/RAM.\\nAttack Name: Fileless Malware.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Why it fails: Traditional AV only scans files physically written to the disk (hard drive). It does not scan active memory/RAM.\\nAttack Name: Fileless Malware."}]
    },
    {
        "title": "Debugging Task: Safe Analysis",
        "description": "A junior analyst receives a suspicious `.exe` file via email. To see what it does, they copy it to a secure, isolated Virtual Machine that has no internet connection and no connection to the host corporate network. They run the file and monitor the results.\\n\\nTask: What is this specific defensive analysis environment called, and what type of analysis (Static or Dynamic) are they performing?",
        "difficulty": "Advanced",
        "starter_code": "Environment: \\nAnalysis Type: ",
        "solution_code": "Environment: A Sandbox.\\nAnalysis Type: Dynamic Analysis (because they are actively running/executing the code).",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Environment: A Sandbox.\\nAnalysis Type: Dynamic Analysis (because they are actively running/executing the code)."}]
    },
    {
        "title": "Challenge: Command and Control (C2)",
        "description": "You are analyzing firewall logs. You notice that 500 computers in your company are all sending a small, encrypted HTTP packet to the exact same foreign IP address every 60 seconds, exactly on the minute.\\n\\nTask: What malware architecture does this highly synchronized 'heartbeat' traffic indicate, and what is the technical term for the foreign server?",
        "difficulty": "Challenge",
        "starter_code": "Architecture: \\nTerm for server: ",
        "solution_code": "Architecture: A Botnet (the computers are acting as zombies).\\nTerm for server: Command and Control (C2) server. The computers are checking in to ask for their next instruction.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Architecture: A Botnet (the computers are acting as zombies).\\nTerm for server: Command and Control (C2) server. The computers are checking in to ask for their next instruction."}]
    }
]

m18_quizzes = [
    {
        "question_text": "What is the primary difference between a Virus and a Worm?",
        "options": ["A virus steals data; a worm deletes data", "A virus requires human interaction to execute and spread (like clicking a file); a worm is self-replicating and spreads automatically across a network", "A virus affects Windows; a worm affects Mac", "There is no difference"],
        "correct_answer": "A virus requires human interaction to execute and spread (like clicking a file); a worm is self-replicating and spreads automatically across a network",
        "explanation": "Worms are incredibly dangerous because they spread at machine-speed without needing humans to make mistakes.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "What type of malware disguises itself as a legitimate, desirable program (like a free game or utility) to trick the user into installing it, while secretly installing a backdoor?",
        "options": ["Ransomware", "Worm", "Trojan", "Spyware"],
        "correct_answer": "Trojan",
        "explanation": "Named after the Trojan Horse, it relies entirely on social engineering and human gullibility.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "A hospital's computers are suddenly locked, and a message appears demanding payment in Bitcoin to decrypt the patient records. What type of malware is this?",
        "options": ["Keylogger", "Ransomware", "Rootkit", "Adware"],
        "correct_answer": "Ransomware",
        "explanation": "Ransomware targets Availability (the 'A' in the CIA triad) by encrypting critical data and extorting the victim.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "When a security analyst places a piece of malware into an isolated, heavily monitored Virtual Machine and double-clicks it to watch what it does, what is this process called?",
        "options": ["Static Analysis", "Dynamic Analysis (in a Sandbox)", "Decompiling", "Port Scanning"],
        "correct_answer": "Dynamic Analysis (in a Sandbox)",
        "explanation": "Dynamic Analysis involves observing the active behavior (file creations, network calls) of the detonated malware safely.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "What is the purpose of 'Static Analysis' in malware research?",
        "options": ["Running the malware to see what happens", "Analyzing the malware file *without* executing it, such as extracting its digital hash or reading hardcoded text strings", "Scanning the network for open ports", "Applying Windows updates"],
        "correct_answer": "Analyzing the malware file *without* executing it, such as extracting its digital hash or reading hardcoded text strings",
        "explanation": "Static analysis is safer because the code is never run. Tools like `strings` or decompilers are used.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "In a large-scale malware infection, what does 'C2' stand for?",
        "options": ["Cyber Command", "Computer to Computer", "Command and Control (The external server the malware phones home to for instructions)", "Core CPU"],
        "correct_answer": "Command and Control (The external server the malware phones home to for instructions)",
        "explanation": "Identifying and blocking the C2 server IP address on the firewall instantly neutralizes the malware's ability to act.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "Why is 'Fileless Malware' so difficult for traditional antivirus software to detect?",
        "options": ["Because it is invisible to the human eye", "Because it executes its malicious commands directly in the computer's active memory (RAM) and never saves an executable file to the hard drive for the antivirus to scan", "Because it uninstalls the antivirus program", "Because it only infects printers"],
        "correct_answer": "Because it executes its malicious commands directly in the computer's active memory (RAM) and never saves an executable file to the hard drive for the antivirus to scan",
        "explanation": "Fileless malware bypasses disk-based scanning. Defenders must use modern EDR tools to monitor RAM and behavior.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "What type of highly advanced malware buries itself deep inside the core Operating System (the kernel) to intercept commands and completely hide its presence from both the user and the antivirus software?",
        "options": ["Ransomware", "Worm", "Rootkit", "Spyware"],
        "correct_answer": "Rootkit",
        "explanation": "Rootkits are incredibly hard to remove because they control the very OS the antivirus uses to scan.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "What is 'Application Whitelisting' (Allow-listing)?",
        "options": ["A list of known hackers", "A defensive strategy where a server is configured to ONLY allow a specific list of pre-approved programs to run, instantly blocking any unrecognized malware", "A list of websites you are allowed to visit", "A type of antivirus scan"],
        "correct_answer": "A defensive strategy where a server is configured to ONLY allow a specific list of pre-approved programs to run, instantly blocking any unrecognized malware",
        "explanation": "Whitelisting is infinitely stronger than blacklisting (trying to block all known malware signatures).",
        "difficulty": "Advanced"
    },
    {
        "question_text": "A hacker infects 100,000 smart refrigerators globally with malware. The hacker uses a C2 server to command all 100,000 refrigerators to send a massive amount of web traffic to a single bank's website, crashing the site. What is this network of infected devices called?",
        "options": ["A VPN", "A Botnet (Robot Network)", "A Rootkit", "A Sandbox"],
        "correct_answer": "A Botnet (Robot Network)",
        "explanation": "Botnets are vast armies of compromised devices (zombies) used to launch Distributed Denial of Service (DDoS) attacks.",
        "difficulty": "Advanced"
    }
]


m19_lesson = """# Logging, Monitoring, SIEM & Incident Response

## 1. What Is It?

Welcome to Phase 4: Blue Team / Advanced. The ultimate goal of a Blue Team (defenders) is to detect and stop a hacker *while* the attack is happening, rather than finding out about it six months later in the news.

This is achieved through **Logging and Monitoring**. Every server, firewall, and laptop generates "Logs" (text records of what happened). However, generating logs is useless if nobody reads them. 

A **SIEM** (Security Information and Event Management) system is the 'Brain' of a Security Operations Center (SOC). It ingests millions of logs from across the entire company, analyzes them in real-time, and generates alerts for the human analysts. 

When a SIEM alert proves to be a real attack, the team moves into **Incident Response (IR)**: the high-stress, systematic process of fighting the attacker, kicking them out of the network, and recovering the business.

## 2. Why Do We Need It?

**Example 1: Finding the Needle**
A company has 5,000 employees. Every day, those employees generate 50 million login events, firewall blocks, and file clicks. A human cannot read 50 million lines of text a day. A SIEM uses correlation rules to find the one login event that happened at 3:00 AM from a suspicious foreign IP address, and alerts the human analyst.

**Example 2: The Chaos of a Breach**
Without an Incident Response plan, when ransomware hits, IT staff panic. They might pull the power cords on the servers, which actually destroys the volatile memory (RAM) evidence needed to figure out how the hackers got in. IR provides a calm, rehearsed military-style playbook for handling disasters.

## 3. Where Is It Used?

- **Security Operations Center (SOC)**: The 24/7 "war room" where analysts stare at SIEM dashboards (like Splunk or IBM QRadar) watching for attacks.
- **Incident Response Teams (CERT/CSIRT)**: The elite "SWAT team" of cybersecurity. They fly to hacked companies to stop active breaches.
- **Compliance**: Audits strictly require companies to retain 1 year of logs to prove they are monitoring their data.

## 4. How Does It Work?

**The SIEM Architecture**
1. **Agents / Forwarders**: Small programs installed on every laptop and server. They quietly read the local log files and forward them over the network to the central SIEM.
2. **The Indexer**: The massive database that stores and organizes the incoming billions of logs.
3. **Correlation Engine**: The brain. It runs logic rules. (e.g., *Rule: If User Bob fails to login 5 times in 1 minute on the VPN, AND then successfully logs in, generate an alert called "Brute Force Success".*)

**The Incident Response Lifecycle (NIST Framework)**
1. **Preparation**: Training, buying tools, writing playbooks *before* the attack.
2. **Detection & Analysis**: The SIEM alerts the team. The team investigates to confirm it's a real breach.
3. **Containment, Eradication & Recovery**: Quarantining the infected laptops (Containment), deleting the malware and kicking out the hacker (Eradication), and restoring from backups (Recovery).
4. **Post-Incident Activity**: The "Lessons Learned" meeting to figure out how to stop it from happening again.

## 5. Important Terminology

| Term | Meaning |
|------|---------|
| **SIEM** | Security Information and Event Management. The central log analysis brain (e.g., Splunk). |
| **SOC** | Security Operations Center. The team of human analysts managing the SIEM. |
| **Correlation** | Linking multiple distinct log events together to identify a complex attack. |
| **Playbook** | A step-by-step instruction manual for handling a specific type of attack (e.g., a Ransomware Playbook). |
| **Containment** | The critical IR phase of stopping the bleeding (e.g., disconnecting an infected server from the internet). |

## 6. Architecture / Diagram

```text
The SOC / SIEM Data Flow

[ Web Server Logs ] \
[ Firewall Logs ]    -- (Forwarded) --> [ SIEM (Splunk) ]
[ Antivirus Logs ]  /                         |
                                              | (Runs Correlation Rule)
                                              v
                                   [ High Severity Alert! ]
                                   "Impossible Travel Detected"
                                              |
                                              v
                                     [ SOC Analyst ] 
                                     (Investigates and triggers Incident Response)
```

## 7. Syntax / Commands / Configuration

SIEMs use specific query languages to search through millions of logs in seconds. For example, Splunk uses SPL (Search Processing Language).

```text
# Example Splunk Query: Find all failed logins on Windows servers in the last 24 hours
index=windows EventCode=4625 | stats count by user

# Example Splunk Query: Find "Impossible Travel"
# (A user logged in from New York, and 10 minutes later logged in from China)
index=vpn action=success 
| stats values(Country) as Countries by user 
| where mvcount(Countries) > 1
```

## 8. Beginner Example

Think of a SIEM like a casino security room.
- **Logs**: Every slot machine, door, and cash register has a camera pointing at it.
- **SIEM**: The central security room with hundreds of TV screens. The computer system automatically highlights a screen in red if it detects someone trying to pry open a cash register (Correlation).
- **Incident Response**: The security guard sees the red screen, radios the floor team to surround the thief (Containment), kicks them out of the casino (Eradication), and replaces the broken cash register (Recovery).

## 9. Real-World Example

**Situation**: A SOC Analyst is watching the SIEM dashboard at 2:00 AM.
**Detection**: An alert pops up: "High Volume of File Modifications". The analyst runs a query and sees that a laptop belonging to "HR-User1" is rapidly renaming thousands of files on the shared network drive to `.encrypted`.
**Analysis**: The analyst realizes this is an active Ransomware attack in progress.
**Containment**: Following the IR Playbook, the analyst immediately clicks a button in their EDR tool to logically isolate "HR-User1's" laptop from the network, cutting off its connection to the shared drive.
**Impact**: Because of the SIEM and fast Incident Response, only 500 files were encrypted before the laptop was contained, saving the remaining 5 million corporate files.

## 10. What Happens Internally? (Log Integrity)

When a hacker breaches a Linux server, the very first thing they do is type `rm -rf /var/log/*` to delete the local log files, erasing the evidence of how they got in.

If a company is not using a SIEM, the evidence is gone forever.
If a company IS using a SIEM, the local agent forwarded the logs to the central SIEM *milliseconds* after the attack happened. 

Even if the hacker deletes the local logs, the SIEM already has an immutable, read-only copy of them safely stored on a separate server. The hacker cannot delete the SIEM logs because they don't have the password to the SIEM. This is why centralized log forwarding is the backbone of enterprise security.

## 11. Common Mistakes

1. **Logging Everything (Alert Fatigue)**: If you configure the SIEM to alert you every time a user types the wrong password, the SOC analysts will receive 10,000 emails a day. They will eventually ignore them all (Alert Fatigue), and miss the real attack. 
2. **Failing to Synchronize Clocks**: If the Firewall clock is set to EST, the Web Server is set to PST, and the Database is in UTC, it is impossible for the SIEM to correlate a timeline of the attack. All servers must use NTP (Network Time Protocol) to sync to the exact same millisecond.
3. **Skipping 'Lessons Learned'**: After surviving a breach, executives just want to go back to work. Failing to hold a Post-Incident meeting guarantees the hackers will use the exact same vulnerability to break in again next month.

## 12. Defensive Best Practices

1. **Tune the SIEM**: Spend months writing highly specific correlation rules. A SIEM should only generate an alert if a human actually needs to investigate it.
2. **Collect the Right Logs**: Don't just collect "System" logs. You must collect DNS logs, PowerShell execution logs, and Firewall deny logs to catch advanced attackers.
3. **Practice Tabletop Exercises**: Every quarter, the Incident Response team should sit in a conference room and run a "Tabletop" simulation. ("Okay team, I'm rolling the dice. The CEO's laptop just got ransomware. Go. What is step 1?")

## 13. Security Mindset

When building a monitoring strategy, ask:
- *If a hacker steals a database tonight at 3 AM, how long will it take us to notice? (If the answer is "When the FBI calls us 6 months later", your monitoring is failing).*
- *Do the SOC analysts have the legal authority to unplug a production server to contain a virus, or do they have to wait 4 hours for the CEO to wake up and approve it?*
- *What logs do we actually need to prove someone stole a file?*

## 14. Try It Yourself

If you are on a Windows computer, you can look at your own logs!
1. Click the Start Menu and type "Event Viewer".
2. Open it, expand "Windows Logs", and click "Security".
3. These are the exact logs a SIEM reads. 
4. Look for an Event ID of `4624` (Successful Logon) or `4625` (Failed Logon).
5. If you see hundreds of `4625` events in a row, someone (or a bot) might be trying to guess your password!
"""

m19_exercises = [
    {
        "title": "Concept Check: Centralized Logging",
        "description": "Read the scenario and identify the concept.\\n\\nScenario: An attacker hacks a server and immediately deletes all the local log files to hide their tracks. However, the security team can still see exactly what the attacker did because the logs were instantly copied to a central security server.\\n\\nTask: What is the acronym for this central log analysis brain?",
        "difficulty": "Beginner",
        "starter_code": "Acronym: ",
        "solution_code": "SIEM (Security Information and Event Management)",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "SIEM"}]
    },
    {
        "title": "Guided Lab: Log Correlation",
        "description": "A SIEM is powerful because it links different events together. It notices that User A swiped their physical ID badge at the New York office building, but 5 minutes later, User A successfully logged into the VPN from an IP address in Russia.\\n\\nTask: What is the specific term for this type of SIEM logic rule that flags physically impossible travel?",
        "difficulty": "Beginner",
        "starter_code": "Rule type: ",
        "solution_code": "Correlation (or Impossible Travel rule)",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Correlation"}]
    },
    {
        "title": "Hands-on Task: Alert Fatigue",
        "description": "You are a SOC Manager. Your junior analyst complains they are receiving 500 emails an hour from the SIEM alerting them to 'Ping Requests Dropped by Firewall'. The analyst is so overwhelmed they miss a critical alert about a database breach.\\n\\nTask: What is the psychological term in cybersecurity for this dangerous phenomenon?",
        "difficulty": "Intermediate",
        "starter_code": "Term: ",
        "solution_code": "Alert Fatigue",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Alert Fatigue"}]
    },
    {
        "title": "Scenario Analysis: Incident Response Lifecycle",
        "description": "A company detects a ransomware infection spreading across their network. The IT Director screams, 'Pull the network cables out of the infected servers immediately so it can't spread to the backups!'\\n\\nTask: According to the NIST Incident Response Lifecycle, which specific phase (Detection, Containment, Eradication, or Recovery) is the IT Director executing?",
        "difficulty": "Intermediate",
        "starter_code": "Phase: ",
        "solution_code": "Containment",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Containment"}]
    },
    {
        "title": "Debugging Task: Time Synchronization",
        "description": "You are investigating a breach. The Web Server logs show the hacker uploaded malware at 14:00. The Antivirus logs show the malware executed at 13:58. The Firewall logs show the hacker's IP connected at 18:00. It is impossible to build a timeline.\\n\\nTask: What critical network protocol did the system administrators fail to configure across all servers to ensure their clocks were synchronized perfectly?",
        "difficulty": "Advanced",
        "starter_code": "Protocol: ",
        "solution_code": "NTP (Network Time Protocol)",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "NTP (Network Time Protocol)"}]
    },
    {
        "title": "Challenge: Containment vs Eradication",
        "description": "A hacker breaches a web server. The Incident Response team changes the firewall rules to block the hacker's IP address (Containment). They declare the incident resolved and go back to normal operations.\\n\\nTask: Explain why this is a massive failure of the 'Eradication' phase, and what the hacker will likely do tomorrow.",
        "difficulty": "Challenge",
        "starter_code": "Why it's a failure: ",
        "solution_code": "The hacker still has a backdoor (like a Web Shell) on the server. Because the IR team failed to Eradicate the root cause (removing the malware and patching the vulnerability), the hacker will simply log in tomorrow from a different IP address at a different coffee shop and continue the attack.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "The hacker still has a backdoor (like a Web Shell) on the server. Because the IR team failed to Eradicate the root cause (removing the malware and patching the vulnerability), the hacker will simply log in tomorrow from a different IP address at a different coffee shop and continue the attack."}]
    }
]

m19_quizzes = [
    {
        "question_text": "In a Security Operations Center (SOC), what does a SIEM (like Splunk) actually do?",
        "options": ["It installs antivirus software on laptops", "It acts as the central brain, ingesting millions of log files from across the company to analyze them and generate alerts for human analysts", "It encrypts the company's network traffic", "It physically prevents hackers from entering the building"],
        "correct_answer": "It acts as the central brain, ingesting millions of log files from across the company to analyze them and generate alerts for human analysts",
        "explanation": "A SIEM turns millions of lines of raw text into actionable intelligence.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "What is the primary benefit of forwarding local server logs to a central SIEM immediately?",
        "options": ["It makes the local server run faster", "If a hacker breaches the local server and deletes all the local logs to hide their tracks, the SIEM already has a secure, read-only copy of the evidence", "It compresses the logs to save space", "It translates the logs into different languages"],
        "correct_answer": "If a hacker breaches the local server and deletes all the local logs to hide their tracks, the SIEM already has a secure, read-only copy of the evidence",
        "explanation": "Log integrity is critical. Decentralized logs are easily destroyed by attackers.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "Which phase of the Incident Response lifecycle involves isolating an infected machine from the network to stop the malware from spreading?",
        "options": ["Preparation", "Containment", "Eradication", "Lessons Learned"],
        "correct_answer": "Containment",
        "explanation": "Containment is 'stopping the bleeding'. It is the most critical immediate action during a breach.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "A SIEM receives a log that User Bob failed to log in 100 times in 10 seconds. It also receives a log that User Bob finally logged in successfully. The SIEM combines these two distinct events to generate a 'Brute Force Success' alert. What is this logic called?",
        "options": ["Correlation", "Encryption", "Hashing", "Denial of Service"],
        "correct_answer": "Correlation",
        "explanation": "Correlation is the magic of a SIEM. It connects the dots between seemingly unrelated events to see the bigger picture.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "What is 'Alert Fatigue' in a SOC?",
        "options": ["When a hacker gets tired of attacking", "A dangerous psychological state where analysts receive so many useless, low-priority SIEM alerts that they become desensitized and ignore real, critical attacks", "When the SIEM server runs out of RAM", "When the network cables overheat"],
        "correct_answer": "A dangerous psychological state where analysts receive so many useless, low-priority SIEM alerts that they become desensitized and ignore real, critical attacks",
        "explanation": "SIEMs must be finely tuned to only alert on actionable, high-fidelity threats to protect the analysts' mental focus.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "According to the Incident Response framework, what must a team do during the 'Eradication' phase?",
        "options": ["Unplug the network cables", "Find and completely remove the root cause of the breach, such as deleting the malware, removing the hacker's backdoor, and patching the vulnerability they used", "Restore the database from backups", "Hold a meeting with the CEO"],
        "correct_answer": "Find and completely remove the root cause of the breach, such as deleting the malware, removing the hacker's backdoor, and patching the vulnerability they used",
        "explanation": "If you don't eradicate the root cause, the hacker will just walk right back through the same open door.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "Why is it absolutely critical to configure Network Time Protocol (NTP) on all servers, firewalls, and laptops sending logs to a SIEM?",
        "options": ["Because NTP encrypts the logs", "So that all device clocks are perfectly synchronized, allowing analysts to build an accurate timeline of the attacker's movements across different servers", "So the servers know when to reboot", "Because the SIEM software will crash without it"],
        "correct_answer": "So that all device clocks are perfectly synchronized, allowing analysts to build an accurate timeline of the attacker's movements across different servers",
        "explanation": "If your firewall clock is 5 minutes faster than your web server, the logs will make it look like the hacker stole the data *before* they even logged in.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "What is the purpose of an Incident Response 'Playbook'?",
        "options": ["To log the hours the analysts worked", "To provide a highly detailed, pre-written, and rehearsed step-by-step checklist for responding to a specific type of attack (like Ransomware), preventing panic during a crisis", "To list the IP addresses of known hackers", "To explain how to install antivirus software"],
        "correct_answer": "To provide a highly detailed, pre-written, and rehearsed step-by-step checklist for responding to a specific type of attack (like Ransomware), preventing panic during a crisis",
        "explanation": "During a crisis, people panic and make mistakes. Playbooks ensure a military-style, systematic response.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "Why is the 'Post-Incident Activity' (Lessons Learned) phase critical after a breach?",
        "options": ["To figure out who to fire", "To analyze what went wrong, improve defenses, update playbooks, and ensure the organization never falls victim to the exact same attack again", "To delete the SIEM logs", "To buy new laptops for the executives"],
        "correct_answer": "To analyze what went wrong, improve defenses, update playbooks, and ensure the organization never falls victim to the exact same attack again",
        "explanation": "A breach is a massive failure. If you don't learn from it, it was a waste of a crisis.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "A SOC analyst detects an active breach on a production database server. They want to physically unplug the server's power cord. Why might this be a terrible idea for the investigation?",
        "options": ["Because the server will be heavy", "Because unplugging the power destroys all volatile memory (RAM), which often contains the only evidence of the malware and the hacker's active network connections", "Because it will alert the hacker", "Because the SIEM will explode"],
        "correct_answer": "Because unplugging the power destroys all volatile memory (RAM), which often contains the only evidence of the malware and the hacker's active network connections",
        "explanation": "To contain a server, disconnect the network cable, NOT the power cord. You need the RAM for digital forensics.",
        "difficulty": "Advanced"
    }
]


m20_lesson = """# Digital Forensics, Threat Hunting & Security Architecture

## 1. What Is It?

This is the final Master module. It combines three elite disciplines that tie together everything we have learned across all four phases of this course.

1. **Digital Forensics**: The scientific process of preserving, identifying, extracting, and documenting digital evidence for use in a court of law or a post-breach investigation. 
2. **Threat Hunting**: The proactive approach. Instead of waiting for the SIEM to alert you, a Threat Hunter assumes the network is *already breached* and actively searches through logs and memory for stealthy hackers who bypassed the alarms.
3. **Security Architecture**: The grand design. Using all the knowledge of how attackers work (OSINT, Scanning, Exploitation, Malware) to design networks, applications, and policies that are inherently resilient to attack.

## 2. Why Do We Need It?

**Example 1: The Court Case (Forensics)**
An employee steals corporate secrets on a USB drive. If the IT guy simply turns on the employee's laptop to look around, they alter the timestamps of files, destroying the evidence in the eyes of a judge. Digital forensics ensures the evidence is legally sound and the employee is convicted.

**Example 2: The Silent Attacker (Threat Hunting)**
Nation-state hackers (APTs - Advanced Persistent Threats) are too smart to trigger standard antivirus alarms. They "live off the land," using built-in Windows administrative tools to move around quietly. Only a human Threat Hunter looking for strange behavior can find them.

## 3. Where Is It Used?

- **Law Enforcement**: The FBI/Interpol use digital forensics to catch cybercriminals and recover deleted data from seized hard drives.
- **Enterprise Cyber Defense**: Mature organizations dedicate specialized teams to Threat Hunting 24/7.
- **Chief Information Security Officers (CISOs)**: Use Security Architecture principles (like Zero Trust) to dictate the technical strategy of the entire company.

## 4. How Does It Work?

**The Forensics Process:**
1. **Acquisition**: Creating a mathematically exact, bit-for-bit copy (an Image) of a hard drive or RAM. The analyst *never* works on the original drive.
2. **Analysis**: Searching the Image for deleted files, hidden partitions, and registry changes using tools like Autopsy or EnCase.
3. **Reporting**: Creating an undeniable timeline of the attacker's actions.

**The Threat Hunting Process:**
1. **Hypothesis**: "I believe a hacker is using PowerShell to download malware."
2. **Investigation**: Querying the SIEM for all PowerShell activity in the last 30 days.
3. **Discovery**: Finding a suspicious, heavily obfuscated PowerShell script running at 3 AM.

**Security Architecture (Zero Trust):**
The old architecture was a "Castle and Moat" (Strong firewall on the outside, total trust on the inside). 
Modern architecture is **Zero Trust**: "Never trust, always verify." Every user, every laptop, and every server must cryptographically prove its identity and authorization for *every single action*, regardless of whether it is inside the corporate office or at a coffee shop.

## 5. Important Terminology

| Term | Meaning |
|------|---------|
| **Forensic Image** | A bit-for-bit, exact clone of a storage device used for investigation. |
| **Chain of Custody** | The chronological documentation showing exactly who handled digital evidence and when. |
| **APT** | Advanced Persistent Threat. Elite, well-funded hackers (usually governments) who stay hidden in networks for years. |
| **IoC** | Indicator of Compromise. A forensic artifact (like a specific IP address or file hash) that proves an intrusion occurred. |
| **Zero Trust** | A security framework requiring strict identity verification for every person and device on a network. |

## 6. Architecture / Diagram

```text
Zero Trust Architecture vs Legacy Architecture

[ Legacy "Castle" Architecture ]
(Internet) ---> [ Firewall ] ---> (Corporate Network)
                                      |
       (Once inside the firewall, Laptop A can talk to Server B freely. 
        If a hacker breaches Laptop A, the whole network falls).

[ Zero Trust Architecture ]
(Internet) ---> [ Identity & Access Broker ] <--- (Corporate Network)
                      |
        (Laptop A must prove its identity, health, and 
         authorization via Multi-Factor Authentication just to 
         open a single connection to Server B. Trust is never assumed).
```

## 7. Syntax / Commands / Configuration

Forensic analysts use command-line tools to safely acquire and verify data.

```bash
# Creating a bit-for-bit image of a hard drive (sda) to a file (evidence.img)
# dd is the standard Linux tool for this.
dd if=/dev/sda of=/mnt/evidence_drive/evidence.img bs=4M

# Verifying the mathematical integrity of the original drive
sha256sum /dev/sda
# Output: 8f9a...

# Verifying the image is an EXACT, uncorrupted copy
sha256sum /mnt/evidence_drive/evidence.img
# Output: 8f9a... (Matches exactly. The evidence is legally sound.)
```

## 8. Beginner Example

Imagine securing a bank.
- **SIEM/Monitoring**: The security cameras watching the lobby.
- **Threat Hunting**: A plainclothes detective walking through the lobby, looking for someone sweating nervously or sketching the floor plan.
- **Forensics**: Taking fingerprints off the vault after it's robbed and sending them to a lab to build a court case.
- **Security Architecture (Zero Trust)**: Putting a locked door not just at the front entrance, but placing a lock on every single desk drawer, filing cabinet, and bathroom door inside the bank, requiring a separate key for each.

## 9. Real-World Example

**Situation**: The SolarWinds Hack (2020) - one of the most sophisticated APT supply-chain attacks in history.
**The Breach**: Russian hackers breached the software company SolarWinds and silently inserted malware into their software updates. 18,000 companies and US government agencies downloaded the infected update.
**The Threat Hunt**: The malware was incredibly stealthy. It waited weeks before activating, used fake names, and communicated with C2 servers disguised as Amazon Web Services. Traditional antivirus caught nothing. 
It was discovered because a highly observant Threat Hunter at the cybersecurity firm FireEye noticed a single, strange Multi-Factor Authentication login from a new device that shouldn't have been there. 
**The Forensics**: FireEye forensically pulled apart the SolarWinds software update and found the incredibly complex malware hidden inside.
**The Architectural Lesson**: The world realized that you cannot blindly trust software updates from vendors (Supply Chain Risk). Zero Trust architecture became the mandatory standard for the US Government.

## 10. What Happens Internally? (Deleted Files)

When a hacker (or a criminal) deletes a file and empties the Recycle Bin, the file is NOT gone. 

Internally, the Operating System just deletes the "pointer" (the index card) that tells the OS where the file is physically located on the hard drive. It marks that physical space on the magnetic disk as "Free to be overwritten."

Until new data is physically saved over that exact spot, the original file's 1s and 0s are still sitting there perfectly intact. A Digital Forensics analyst uses tools (like file carving) to scan the "empty" space on a hard drive, bypass the OS index, and successfully recover the "deleted" files.

## 11. Common Mistakes

1. **Breaking the Chain of Custody**: If an IT admin puts a seized hard drive in their desk drawer for the weekend without logging it in the evidence tracker, a defense attorney will argue the drive was tampered with, and the judge will throw out the evidence.
2. **Relying on "IoC" Sweeps instead of Threat Hunting**: Searching your SIEM for a known bad IP address (an IoC) is easy, but it only catches lazy attackers. Real Threat Hunting involves looking for unusual *behaviors* (e.g., "Why is the CEO's account running PowerShell scripts?"), not just bad IPs.
3. **Misunderstanding Zero Trust**: Buying a fancy new firewall and calling it "Zero Trust." Zero Trust is an architecture and a mindset, not a product you can buy off a shelf.

## 12. Defensive Best Practices

1. **Write Blockers**: When performing forensics on a hard drive, ALWAYS use a physical hardware write-blocker to connect the drive to your computer. This physically prevents your computer from accidentally writing data to the evidence drive and altering timestamps.
2. **Hypothesis-Driven Hunting**: Threat hunters must start with an educated guess. ("I hypothesize that attackers are bypassing our spam filter using encrypted zip files. Let's look for evidence of that specific behavior").
3. **Micro-segmentation**: A core principle of Security Architecture. Break the corporate network into tiny, isolated zones. If a hacker breaches the Marketing zone, they hit a firewall trying to reach the Finance zone.

## 13. Security Mindset (The Master Level)

As you complete this course, your mindset should shift from focusing on individual tools to focusing on the **System**:
- *An attacker will eventually bypass the firewall.*
- *An attacker will eventually bypass the antivirus.*
- *An attacker will eventually trick an employee with a phishing email.*
- *Knowing this, how do I architect a system that assumes compromise, detects the attacker quickly, contains them to a tiny blast radius, and forensically recovers with zero data loss?*

That is the mindset of a Cybersecurity Master.

## 14. Try It Yourself

(Mental Exercise: The Threat Hunter)
Look at your own computer's behavior. 
1. Open Task Manager (Windows) or Activity Monitor (Mac).
2. Look at the list of running processes. You will see dozens of background tasks you don't recognize. 
3. A Threat Hunter doesn't panic; they investigate. Right-click a strange process and search online for what it is. 
4. Is it a legitimate Microsoft updater? Or is it malware pretending to be `svchost.exe` but running from the wrong folder (like the Downloads folder)? 
Threat hunting is the art of knowing what "Normal" looks like, so "Abnormal" stands out clearly.
"""

m20_exercises = [
    {
        "title": "Concept Check: Forensics Integrity",
        "description": "Read the scenario and identify the critical error.\\n\\nScenario: The police seize a criminal's laptop. To find evidence quickly, an officer opens the laptop, logs in, opens Microsoft Word, and searches for a specific document.\\n\\nTask: What fundamental rule of digital forensics did the officer just violate, which will cause the evidence to be thrown out of court?",
        "difficulty": "Beginner",
        "starter_code": "Violated rule: ",
        "solution_code": "They worked on the original evidence. By logging in and opening programs, the officer altered hundreds of timestamps and files on the hard drive. They must ALWAYS work off a bit-for-bit forensic clone (Image) of the drive.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "They worked on the original evidence. By logging in and opening programs, the officer altered hundreds of timestamps and files on the hard drive. They must ALWAYS work off a bit-for-bit forensic clone (Image) of the drive."}]
    },
    {
        "title": "Guided Lab: Deleted Files",
        "description": "A criminal deletes an incriminating spreadsheet and empties the Recycle Bin just before their laptop is seized.\\n\\nTask: Explain briefly why a forensic analyst can still easily recover this file using 'file carving' tools.",
        "difficulty": "Beginner",
        "starter_code": "Reason: ",
        "solution_code": "Because 'deleting' a file only removes the operating system's pointer to the file. The actual physical 1s and 0s of the data remain on the hard drive until they are overwritten by new files.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Because 'deleting' a file only removes the operating system's pointer to the file. The actual physical 1s and 0s of the data remain on the hard drive until they are overwritten by new files."}]
    },
    {
        "title": "Hands-on Task: Data Hashing",
        "description": "A forensic analyst creates a clone (`evidence.img`) of a seized hard drive. They need to prove in court that the clone is a mathematically perfect, unaltered copy of the original drive.\\n\\nTask: What specific type of one-way cryptographic algorithm must the analyst run on both drives to prove they match exactly?",
        "difficulty": "Intermediate",
        "starter_code": "Algorithm type: ",
        "solution_code": "A Hashing algorithm (like SHA-256 or MD5).",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "A Hashing algorithm (like SHA-256 or MD5)."}]
    },
    {
        "title": "Scenario Analysis: Threat Hunting",
        "description": "An antivirus scanner alerts on a known malware file and blocks it. The IT team considers the incident resolved. However, a Threat Hunter starts an investigation based on the hypothesis: 'If this malware was blocked, how did it get onto the machine in the first place?'\\n\\nTask: What is the fundamental difference in mindset between the IT team relying on the antivirus, and the Threat Hunter?",
        "difficulty": "Intermediate",
        "starter_code": "Difference: ",
        "solution_code": "The IT team relies on reactive alerts (waiting for the alarm). The Threat Hunter is proactive; they assume the network is already compromised and actively search for the stealthy root cause (e.g., a phishing email or backdoor) that the automated tools missed.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "The IT team relies on reactive alerts (waiting for the alarm). The Threat Hunter is proactive; they assume the network is already compromised and actively search for the stealthy root cause (e.g., a phishing email or backdoor) that the automated tools missed."}]
    },
    {
        "title": "Debugging Task: The Castle and Moat",
        "description": "A company has a massive, highly expensive firewall protecting their office (The Castle and Moat). An employee takes their corporate laptop to a coffee shop, gets infected with a worm, brings the laptop back to the office, and plugs it into the wall. The worm instantly infects all servers inside the office.\\n\\nTask: Explain why the 'Castle and Moat' architecture failed completely here.",
        "difficulty": "Advanced",
        "starter_code": "Why it failed: ",
        "solution_code": "Why it failed: The architecture assumes total trust for any device physically inside the firewall (the Moat). The infected laptop bypassed the firewall physically. Once inside, because there were no internal security checks (Zero Trust), the worm spread freely.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Why it failed: The architecture assumes total trust for any device physically inside the firewall (the Moat). The infected laptop bypassed the firewall physically. Once inside, because there were no internal security checks (Zero Trust), the worm spread freely."}]
    },
    {
        "title": "Challenge: Zero Trust Application",
        "description": "You are redesigning a network using Zero Trust principles. A legitimate employee, logged into their corporate laptop with the correct password, tries to access the Finance Database.\\n\\nTask: Under Zero Trust ('Never trust, always verify'), describe at least two additional checks the network must perform before granting the employee access to the database.",
        "difficulty": "Challenge",
        "starter_code": "Check 1: \\nCheck 2: ",
        "solution_code": "Check 1: Multi-Factor Authentication (MFA) - Prove the human is actually the employee.\\nCheck 2: Device Health - Prove the laptop has the latest antivirus and OS patches installed before allowing the connection.",
        "language": "text",
        "test_cases": [{"input": "", "expected_output": "Check 1: Multi-Factor Authentication (MFA) - Prove the human is actually the employee.\\nCheck 2: Device Health - Prove the laptop has the latest antivirus and OS patches installed before allowing the connection."}]
    }
]

m20_quizzes = [
    {
        "question_text": "What is the most fundamental rule of Digital Forensics when handling electronic evidence?",
        "options": ["Always turn the computer off immediately", "Never work on or alter the original evidence; always create a bit-for-bit forensic image (clone) and perform analysis on the clone", "Print out all the files for the judge to read", "Upload the files to the internet for safekeeping"],
        "correct_answer": "Never work on or alter the original evidence; always create a bit-for-bit forensic image (clone) and perform analysis on the clone",
        "explanation": "Altering the original evidence, even by just turning the computer on, destroys timestamps and renders the evidence legally inadmissible.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "How does a forensic analyst mathematically prove in court that their forensic image (clone) is an exact, uncorrupted copy of the seized hard drive?",
        "options": ["By weighing the hard drives", "By taking a photograph of the screen", "By generating a Cryptographic Hash (like SHA-256) of both drives and showing that the hashes match perfectly", "By reading every file aloud"],
        "correct_answer": "By generating a Cryptographic Hash (like SHA-256) of both drives and showing that the hashes match perfectly",
        "explanation": "If even one single bit (a 1 or a 0) changed during the copying process, the hashes would be completely different.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "If a suspect deletes a file and empties the Recycle Bin, why is a forensic analyst usually still able to recover the file?",
        "options": ["Because the government keeps a copy of all files", "Because the operating system only deletes the file's 'pointer' (index), leaving the actual physical data intact on the hard drive until it is overwritten by new data", "Because deleted files are sent to the cloud", "Because deleting files is actually impossible"],
        "correct_answer": "Because the operating system only deletes the file's 'pointer' (index), leaving the actual physical data intact on the hard drive until it is overwritten by new data",
        "explanation": "Forensic tools scan the 'unallocated space' on a drive to carve out data that the OS claims is gone.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "What is the 'Chain of Custody'?",
        "options": ["A type of malware", "A physical lock placed on server racks", "The strict chronological documentation showing exactly who seized, handled, analyzed, and stored digital evidence to prove it was never tampered with", "The hierarchy of passwords in a database"],
        "correct_answer": "The strict chronological documentation showing exactly who seized, handled, analyzed, and stored digital evidence to prove it was never tampered with",
        "explanation": "If the Chain of Custody is broken (e.g., an analyst took the drive home for the weekend without logging it), the defense attorney wins.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "What is the core philosophy of 'Threat Hunting'?",
        "options": ["Waiting for the antivirus to delete a virus", "Assuming that the network has already been breached by advanced stealthy attackers, and proactively searching through logs and systems to find them before they cause damage", "Searching the internet for pictures of hackers", "Physically hunting down cybercriminals with the police"],
        "correct_answer": "Assuming that the network has already been breached by advanced stealthy attackers, and proactively searching through logs and systems to find them before they cause damage",
        "explanation": "Threat Hunters do not wait for alarms. They actively look for behavioral anomalies that automated tools miss.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "In the context of Threat Hunting, what is an 'APT'?",
        "options": ["Automated Penetration Test", "Advanced Persistent Threat (Elite, usually nation-state hacking groups that remain hidden inside networks for months or years)", "Anti-Phishing Tool", "Application Programming Threat"],
        "correct_answer": "Advanced Persistent Threat (Elite, usually nation-state hacking groups that remain hidden inside networks for months or years)",
        "explanation": "APTs (like Russian or Chinese intelligence agencies) are the primary targets of elite Threat Hunters.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "What is the fundamental flaw with the traditional 'Castle and Moat' security architecture?",
        "options": ["It relies too heavily on antivirus software", "It assumes that anyone or anything inside the firewall (the Castle) is inherently trusted, meaning if an attacker breaches the perimeter, they have free rein to attack the entire internal network", "It requires too many passwords", "It is illegal to use"],
        "correct_answer": "It assumes that anyone or anything inside the firewall (the Castle) is inherently trusted, meaning if an attacker breaches the perimeter, they have free rein to attack the entire internal network",
        "explanation": "The 'hard crunchy outside, soft chewy inside' model is obsolete in the modern era of remote work and cloud computing.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "What is the core philosophy of 'Zero Trust' architecture?",
        "options": ["Never trust employees, and fire them if they click a phishing link", "Disable all firewalls because they don't work", "Never trust, always verify. Every user and device must continuously prove their identity and authorization for every single request, regardless of whether they are inside or outside the corporate network", "Only trust Apple devices"],
        "correct_answer": "Never trust, always verify. Every user and device must continuously prove their identity and authorization for every single request, regardless of whether they are inside or outside the corporate network",
        "explanation": "Under Zero Trust, the internal network is treated as equally hostile and dangerous as the public internet.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "What is an 'IoC' (Indicator of Compromise)?",
        "options": ["A tool used to crack passwords", "A forensic artifact, such as a specific malicious IP address, malware hash, or strange registry key, that serves as evidence an intrusion occurred", "A type of firewall rule", "The final report given to the CEO"],
        "correct_answer": "A forensic artifact, such as a specific malicious IP address, malware hash, or strange registry key, that serves as evidence an intrusion occurred",
        "explanation": "When an attack happens, analysts share IoCs with the community so other companies can search their SIEMs to see if they were also hit.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "A Threat Hunter formulates a hypothesis: 'Attackers are using PowerShell to bypass the antivirus.' What is the hunter's next step?",
        "options": ["Reboot all the servers", "Query the SIEM logs to search for unusual, encoded, or unauthorized PowerShell execution commands occurring across the network", "Buy a new antivirus program", "Perform a physical penetration test on the building"],
        "correct_answer": "Query the SIEM logs to search for unusual, encoded, or unauthorized PowerShell execution commands occurring across the network",
        "explanation": "Threat hunting is hypothesis-driven. You think of a way an attacker might hide, and then you hunt for the evidence in the logs.",
        "difficulty": "Advanced"
    }
]




cyber_lessons = [
    m1_lesson,
    m2_lesson,
    m3_lesson,
    m4_lesson,
    m5_lesson,
    m6_lesson,
    m7_lesson,
    m8_lesson,
    m9_lesson,
    m10_lesson,
    m11_lesson,
    m12_lesson,
    m13_lesson,
    m14_lesson,
    m15_lesson,
    m16_lesson,
    m17_lesson,
    m18_lesson,
    m19_lesson,
    m20_lesson,
]

cyber_exercises_list = [
    m1_exercises,
    m2_exercises,
    m3_exercises,
    m4_exercises,
    m5_exercises,
    m6_exercises,
    m7_exercises,
    m8_exercises,
    m9_exercises,
    m10_exercises,
    m11_exercises,
    m12_exercises,
    m13_exercises,
    m14_exercises,
    m15_exercises,
    m16_exercises,
    m17_exercises,
    m18_exercises,
    m19_exercises,
    m20_exercises,
]

cyber_quizzes_list = [
    m1_quizzes,
    m2_quizzes,
    m3_quizzes,
    m4_quizzes,
    m5_quizzes,
    m6_quizzes,
    m7_quizzes,
    m8_quizzes,
    m9_quizzes,
    m10_quizzes,
    m11_quizzes,
    m12_quizzes,
    m13_quizzes,
    m14_quizzes,
    m15_quizzes,
    m16_quizzes,
    m17_quizzes,
    m18_quizzes,
    m19_quizzes,
    m20_quizzes,
]

cyber_module_titles = [
    "Phase 1: What Cyber Security actually is",
    "Phase 1: Computer & OS fundamentals",
    "Phase 1: Networking fundamentals",
    "Phase 1: TCP/IP, ports, protocols",
    "Phase 1: Linux fundamentals",
    "Phase 1: Windows security fundamentals",
    "Phase 2: CIA Triad, threats, vulnerabilities & risk",
    "Phase 2: Authentication, authorization & cryptography",
    "Phase 2: Hashing, encryption, encoding & certificates",
    "Phase 2: Web security fundamentals",
    "Phase 2: OWASP Top 10",
    "Phase 2: Secure coding & input validation",
    "Phase 3: Reconnaissance & OSINT",
    "Phase 3: Scanning & enumeration",
    "Phase 3: Vulnerability assessment",
    "Phase 3: Web penetration-testing concepts",
    "Phase 3: Network security & packet analysis",
    "Phase 3: Malware concepts & defensive analysis",
    "Phase 4: Logging, monitoring, SIEM & incident response",
    "Phase 4: Digital forensics, threat hunting & security architecture",
]
