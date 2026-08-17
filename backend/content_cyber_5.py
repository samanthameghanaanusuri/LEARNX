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
