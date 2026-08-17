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
