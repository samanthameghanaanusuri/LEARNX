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
