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
