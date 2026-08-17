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
