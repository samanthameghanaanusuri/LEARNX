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
