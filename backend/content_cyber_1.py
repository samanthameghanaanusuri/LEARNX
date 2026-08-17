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
