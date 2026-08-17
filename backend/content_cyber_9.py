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
