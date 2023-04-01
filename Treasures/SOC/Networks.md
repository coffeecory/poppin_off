https://support.ixiacom.com/sites/default/files/resources/whitepaper/915-3534-01-tap-vs-span-ltr.pdf

Flow logs - layer 3-4 - Huge Volumes, top talkers, most frequent connections, and odd port numbers/bad IP addresses. 

sflow Sampled flow - Speed Networks where flow capture cannot done. Sflow partial

Zeek - Http methods, DNS Requests, hostnames, SMTP connections Details, etc, plus all flow logs tool data. Details SUS activity but still small data sets. 

https://twitter.com/taosecurity/status/1066377040256004096

Full PCAP - Elephant sized solution of the bunch. 

	$ tshark -r [pcap file] -z conv,tcp -q -n

Flow logs Detections

High bandwith or long running connections 
communication between endpoints that shouldnt be
matching of the IP addr to threat intell
Audit remote ADM protocols like SMB, RDP, powershell, etc.
Unexpected ports

PCAP on perimiter is zeek everywhere else

Zeek - HTTP, DNS, SMTP, SMB, SSL/TLS, etc

# DNS

Stub Resolver - localhost
	ipconfig/displaydns

Forwarding Server - Internal Servers

Caching Servers - 1.1.1.1 and 8.8.8.8 pihole project

Authoritative Server- only have that domains DNS and do not recurse like ns1.google.com have answers for mail.google, doc.google, www.google.com


Are you recording only DNS requests? or responses as well?
What is happening with those response records? logging this can be used in investigation.

If someone isnt using your DNS server you wont see it logged? EDR will catch this. I
If we dont block contacting external DNS servers at the FW level.

Use Defensive OPSec

https://centralops.net/co/

SUS TLD's

Block or alert on .tk, .poker, .xxx or other free domains?

Track or Visualize anomalous TLD usage?

### Domain Reputation 

Check all domain Rep with any service 

Block any med+ risk and bad categories sites

Uncat sites - Consider block or using splash screen.

Visualize chart - who is hitting these sites most.

Do not blindly trust categorization.

### Domain Age

Use any method available to check age of domain 

Track. visualize and alert on new domains

Consider new to you as well

	whois domain_name

Use mark baggets domain stats python tool to enrich your detections.
https://github.com/MarkBaggett/domain_stats2

DNS research sites

- Centralops.net
- dnsstuff.com
- who.is

Create lookup list of all domains visited in the past x amount of time can be used for fidelity and for threat hunting and investigation.

### Domain Randomness and Length

Malware usees RNG alg to avoid takedown.

What is longest domain ever typed?
longer is more and more procedurally generated likliness

- Auto Asses domain randomness and length
- Alert on anomalies, chart and visualize for threat hunting and awareness.

Filter Content Delivery Networks and Cloud services by assessing the parent level domain. random subdomain and not *.Safedomain.com

Pay attention to long subdomains as well as DNS tunneling see below. <Link this later>

### ASN

- File downloads
- Make geolocation data better
- Useful for inbound traffic, but trends can be found

Risky Download from top 10 bad ASN
https://www.spamhaus.org/statistics/botnet-asn/

### Geolocation

Web traffic that should not be coming or going to a location can help build use case profiling but may not be a smoking gun.

# DNS Attacker Tricks

Recon to Exfil

- Unauth DNS server use
- Malicous sites on shared hosting
- Modifying your DNS records
- DNS Tunneling
- Blockchain DNS
- IDN's

### Unauthed DNS server use

log block bad queries

Attacker ignores System DNS and uses their own.
- Browsers do this.

- Block External DNS with firewalls only all to approved servers.
- Log all DNS, wether it goes to your serv or attempts otherwise.
- New ThreatL Decrypt TLS and block/log DOH usage.

#Alert on any attempts to use DNS in unexpected ways(Watch for FW deny messages relating to outbound DNS attempts.)

TLS decrypt is necessary to spot rougue dns server usage through DOH. 

Malware will do checks to confirm it can hit 8.8.8.8 first.

#Controls Dont allow outside resolvers.

Indicative of misconfiguration or malware that uses its own settings. Easy way to ID infected devices.

### Detecting Unauth DNS 

Firewall logs - ANy logs(Block or Allow) from the inside going outbound should record the activity.

Netflow/Network Metadata: Any service that is recording layer 3-4 stats for outbound traffic can be searched for UDP 53 with Inside Src and External Dst.

Host FW logs: if you use a host FW on your servers or Desktops that records out traffic search here.

IDS Alerts: Check if external DNS activity has occured.

Host Integrity Checks: Malware changed sys settings for DNS, monitor system state drift. 

Endpoint Detections and Response: Any EDR tool should have the capability to record DNS traffic for each host. Search solutions for all DNS traffic that is not bound for the authed internal DNS server this is a EZ win. 

Manual investigation IP before blocking if located on hosting provider. Block domain and IP if so. 

### DNS Record Mods

Clone your orgs website on an evil server
obtain a tls cert for your domain - they can if they control DNS
Clone your orgs webpage, send your employees there, intercept data.

Use MFA and #alert change detection for DNS admin or DNS activity altogether

### DNS Tunneling 

Send req direct to attacker owned nameserver
Send reg through normal org dns resolver

CNAME tunneling
TXT record tunneling

Doesnt use BIND but DNS tunneling software like iodine or dsncat2

#Alert long queries in excessive volume to a single domain. Sophos does this for good. Quick search using SOAR to kick off and then ChatOPS to analyst to check and then move forward with flow. 

#Alert NULL request type, highly sus considering very large query with non-standard char sets. Iodine can do this and again SOAR > ChatOPS domain check confirm > Continue SOAR flow.

#Alert Lookup lists for FP's matching AV suites, CDN's, DNS hijacking tests

High-Volume DNS requests to an unkown or known malicous parent domain should be investigated as fast as possible. 

#Alert Excessive Queries for one domain with many subdomains

#Alert Excessive DNS queries from one source

#Alert Excessive amount of odd query types
- TXT, CNAME, MX, NULL

#Alert Long/random looking subdomains, especially with odd parent domain dest.

#Alert Encoded Data in TXT responses

#Alert Usage of unauthorized DNS servers 


### Blockchain DNS

OpenNIC maitains peering agreement with EmerDNS and doesn't register with ICANN. Rquires special browser based extension software most of the time. Is a way for an attacker to use Domain to IP mappings and never get there payload C2's disabled. 

#Alert Look for DNS requests with any blockchain DNS BDNS root zones. If software is wrapping the reqs in another protocol like TLS for DoH its important to know what protocols are in use and monitor DNS drift to try and catch BDNS over different protocol. 

### IDN's

punycode to take alt english language and convert it back into the original DNS design. 

Homoglyph attack #AE

#Alert Check the xn-- prefix must use SOAR or manual tool to decode punycode probably cyberchef or https://www.punycoder.com/

### DOH

Uses TCP 443 to DOH server Destination
Sends HTTP/2 Req with MIME-Type: Application/dns-message
- Decrypt - Using TLS inspections methods best method
- Disable - DOH not use clients with canary domains
- Log - Use an internal DOH-Capable server that records reqs
- Tell DNS client to log( Firefox can write DNS log.)

Traditional DNS wrapped up and sent as content of a http/2 POST reqeust, which is sent to the web server wrapped in TLS encryption via client 2 remote DOH service.


Cloudflare is default Firefox DOH provider. but when looking at DOH its shows as TLS traffic so after decrypting it you can spot DOH or HTTP/2 requests to malicous domains.

#ThreatHunt Search for port 443 traffic to well-known DNS server IP addr like 1.1.1.1, 8.8.8.8, 9.9.9.9. 

Android uses DoT already and windows 11 will support this so blocking port 853 is warranted.  The day is coming when we will be blinded by DNS requests using TLS or HTTP make a plan now. 

# HTTP

Decoding a URI 


![[Pasted image 20230401132622.png]]

HTTP GET is most common and should not use sensitive data

HTTP POST can hide malware in the POST body so look for data=Obsfucated_strings

Request Headers: Cookie, User-Agent, Referer 
Conent Headers are entitiy headers. 

Host: Domain was contacted (1 IP to many domains is possible)

User-Agent: Describes Browser or Client used to access site.

Referer: URL user was at prevouisly to being redirected there.

Accept*: Multiple Types of items and formats accepted by client browser: Filetypes, language preferences, and endcoding, etc. First item preffered in a list. 

Cookie: Unique ID as user to webserver, allows login state and other info to be preserved. 

X-Forwarded-For: ID true source IP if the client is connecting through proxy. Only visable on outgoing side of proxy not client itself. 

#Triage Host: use DNS tactics like is domain safe. Useragent: Common or not, Do we run this sys or version?, PATH: Do folder and filenames look SUS like random, phish, encoding, etc? CONTENT: Unusual unneeded encoding, etc?


### HTTP Response 

Content-Type: Transaction for all connections resulted in a downloaded file 
https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers


### HTTP Response Codes 

407: User must auth to proxy before accessing a resource indicative of malware but noisey.


Look for HTTP Response header values, Data and Time, 200 OK or other status, File byte size and Content-Type - text/plain


### HTTP/2 SPDY

No longer require requests for each file to be sent. nor each request made be broken into individual packets. HTTP/2 will make one TCP connection and within the one connect it will use streams, each with individual frames. Seperate frames for HTTP headers and data, these frames will contain binary data - not plaintext not like http/1. If that wasn't already hard enoughj to analyze, the standard mandates that HTTP/2 use encryption but non browser use is optional. 

Server push is were server assumes pre-emptively push assets unlike HTTP/1 where you ask for each asset individually. This makes it hard for analysts to see why a request was made or impossible. When not encrypted it is a bit easier to see but is not like the typical 200 OK ease of spotting was something succesfull. 

Follow stream ID's for HEADERS and DATA and follow them to find the RESPONSE 

HPACK - Standard for Header Encoding no longer can follow streams. 



# 12 Days of Defense - Day 10: How to Analyze HTTP/2 Traffic in Wireshark
https://www.youtube.com/watch?v=weT02x9R7wk


### HTTP/3 QUIC

TCP+TLS+HTTP2 but on top of UDP.  HTTP/2 over UDP

Wireshark Ver 3.7+ to decrypt

Can be used for carrying SMB over the net which is available as of early 2022 in Win 11 and Server 2022 Datacenter: Azure Edition

https://www.chromium.org/quic/

https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-over-quic

Most important Response headers 
Virtual Host, User-Agents, Referer, Method, MIME Type

### HTTP Analysis 

Automated Methods:
URL and Site reputation Checks
Screenshots
Sandboxing Sites
- HTML Anlaysis
- Full VM-based Anlaysis

Manual Methods:
Examin Headers - Request/Response analysis
Examin Contents - Content Analysis, File Extraction, Anomaly Hunting

### Manual Header and Content Analysis

Header analysis: URL's, User-Agents, etc
GET/POST Content
File Analysis
Anomalous Behavoir
- Base64 endoded content
- Naked IP addresses
- Repetitive beaconing
- Other anomalies

#### User-Agent Analysis

Malware creators dont take time to match user-agents to internal software. Even if the attacker uses a new user-agent and doesn't have coded updates for this in his malsoft then with time or right away updates will let us see this lagging behind connection type. 

#Alert Frequency Analysis of user-agent can help highlight descrepencies and be a great lead for hunt-teaming. #ThreatHunt 

https://github.com/mitchellkrogza/nginx-ultimate-bad-bot-blocker/blob/master/_generator_lists/bad-user-agents.list

#Alert Use the list above and match on this > baseline > look for additional new connections using the above list. 


### Base64 4 Evil

I see base64 ina place that maybe shouldn't be used AND it seems to associated with mal host names, AND the requests contain User-Agents that are also SUS. 

### File Anlaysis 

Sometimes its the only way to spot the bad guy.

### File Extraction

Carve files using Wireshark Export Objects > HTTP, TFTP, SMB, IMF, and DICOM Files.

Take EXE and dump onto a linux host. Also .js, .vbs, .ps1, etc 

HTTP/2 Requires manual carving of data from the DATA frame. 

### HTTP C2

#Alert More than 100 post's to a non-top 1000 website in under 1hr 

This is not a perfect rule bc of beacon speed intervals. 

GET/POST 
- High Volume
- Periodic in nature
- New/untrusted domains - great SIEM filter if possible
- Going to a root of a website (GET or POST to /)
- Contain encoded data in request/response body

RITA can be used. 

#### Naked IP's

Could be Vendor warrants a look

POST req to / doesn't seem like scripting like PHP file, REST-Style API just straight to the ROOT Folder strange. 

Host = IP addr

### Exploit Kits

Automatic Exploit Selection and arbitrary delivery system. Must get a redirect to there exploit kit server most likely oppurtunistic not targeted. 

Use NoScirpt to disable running 3rd party scripts on webpages.

Fully patched is usually best unless on rare occusion they are weaponized with a Zero-Day exploit. 

Likely see highly obsfucated Javascript on redirect site or initial refferer. 

### Dynamic DNS 

#Alert Alert on Dynamic DNS hits 

### TLS Decryption 

Must have root level Cert authority created in org that can sign certs for other websites and installed this in your browser. 

Client gets internal CA > Decryptor > to Site 
Site gives its cert < back to Decryptor  < then Decrypter uses the client org assigned CA to connect back to client then this happens back and forth. 

No TLS Decryptor?

- Still see Dest IP use Deny List, ASN and Geo info, along with passive DNS.
- TCP Layer shows dest port user used to create the TLS tunnel. Mostly port 443 but if you saw SSL/TLS connect to port 4444 may still have an opportunity for the occasional detection. 
- Session Layer most intresting info here. You may see site bc DNS already but the SSL/TLS is passed in plaintext which means so it can be used a secondary source for seeing site connections. Also see who issued cert and optional org details.
- Connection Data like volume send and rcv looking for large upload to trigger anomaly alert based on this volume. 

### SSL/TLS Certs

Attackers dont usually fill out the optional fields.
Attackers also create self-signed certs that are not signed by any authority. 

### JA3, JA3S, JARM TLS Fingerprints

All Software makes TLS connections with slightly diff params. Firefox vs tor client vs emotet malware.

JA3 Concats and hashes fields from ClientHello TLS packets.
- JA3 is a client fingerprint, JA3S is a server fingerprint
- TLS Version, Accepted Ciphers, List of Extensions, Elliptic Curves, Elliptic Curve Formats.
- Firefox on windows : 771,4865-4867-4866-...
- Hash of above can be output and then converted to the user agent. 

Check your browsers JA3 hash or any hash at ja3er.com*
Also check out JARM for a method to actively fingerprint servers!

For server connects that dont fall under threat intel we can use JARM to catch C2 but make sure OPSEC wants to have there cover blown. 

Zeek will create both JA3 and JA3S hashes for all connections to help ID and Stop malicous software. 

JA3 can help ID gold image drift but baselining known good and spotting deviations. 

Aids well with OSQUERY. 

### TLS1.3

Cert details not visable without Decryption

Domain is still Visable in Server Name Indication Field for now.
- Encrypted Client Hello (ECH) will soon encrypt domain 

TLS 1.3 more difficult to inspect:
- Prtection from downgrade attacks
- Enforces without pre-master secrets from browsers
- Encrypted SNI standard means we will eventually lose visibility of the domain being visited without Decryption.

# SMTP and Email

![[Pasted image 20230401163516.png]]

Message User Agent - MUA
Message Transfer Agent - MTA
Message Delivery Agent - MDA

![[Pasted image 20230401164114.png]]

### Email Headers
Trace Headers
- Written by each MTA that Touches the email.
- Recieved headers trace email back through MTA's.
- Additional Fields add detail for receiving MDA/Client to interpret.
	- Return-Path
	- Recieved

Message headers
- Written by client sending email or submission MTA
- Contain message metadata
	- From
	- To 
	- Subject
	- Date
	- Message-ID
	- MIME-Version
	- Content-Type
	- Content-Transfer-Encoding 
	- x-mailer
	- Thread-index
	- Content-Language

Body 
- Shows "plaintext" and HTML view of the email content.
- Attachments are usually base64 encoded. 

### Recieved Header

from EHLO string(Rsults of ptr lookup for IP\[IP that connected to MTA Cant be spoofed\]) by \<recieving MTA\>


### Spoofed Email
SPF record helps MTA look for FROM line by doing a DNS TXT record request then pull allowed IP senders for that domain. If the IP was not from that domain it would drop, spam, or quarintine. 

### Verify Mail Source

SPF - Sender Policy Framework
- Mail source from verified source. 
DKIM - Domain keys Identified Mail
- Message Content verified via digital signature
DMARC - Domain-based message authentication, reporting, and compliance)
- Prevents attacks based on different from address and displayed address.

### SPF Results

- Pass - Client is listes as authorized for sending email
- None/Neutral: Either there is no policy listed, or the policy
does not address the source specifically
- Soft fail: Between neutral and fail, client is allowed, but should
be treated as suspicious (when "~all" is used)
- Fail: The client is listed as unauthorized for sending email,
usually falls under "-all" rule

1. Authentication-Results header
2. Recieved-SPF header 

### DKIM

DKIM verifies email source via digital signatures

1. Sender picks header/body/both parts of email to sign (selector)
2. Upon sending a new message:
- Selector is hashed
- The hash is encrypted with private key at the email gateway (signed)
3. The receiver uses the domain/selector combo to:
- Pull the public key for the domain from DNS
- Hash the same sections from selector
- Validate decryption under public key creates the same hash
Takeaway: Look for dkim=pass in authentication-results header!

DKIM= pass, fail, or none

### DMARC

SMTP has other issues:
• From fields may differ from "Envelope" vs. "Content"
DMARC builds on SPF and DKIM to fix this
• Allows domain owners to specify if SPF/DKIM is set up
• Enables reporting on authentication failures!
• To pass DMARC a message must
	- Pass SPF and/or DKIM and be, "aligned"
	- SPF aligned: RFC5322.From matches RFC5331.MailFrom field
	- DKIM aligned: RFC5322.From matches DKIM "d=" field


# Other Net Protocols

DHCP can be used by Defenders

Protocols used for Lateral Movement/Exfil
- SMB
- SSH
- RDP/VNC
- Pwsh Remoting
- ICMP/FTP
- Any remote access or admin tool, regardless of protocol.

### DHCP

Why is DHCP interesting?
• Most incidents require mapping IP address to computer
	- DHCP provides the link from IP address to computer name
	- Computer name can be used to find the device's owner
Can be used to detect rogue 4evices!
• Hostname: Matching against naming pattern, deny/allow list
• MAC Address OUI
	- Deny list: Wi-Fi routers, IoT devices
	- Allow list: Company authorized laptop vendors, etc.


## SMB

One of the most commonly attacked services!
• Windows native, runs with Samba on Linux
• Used for connecting to Windows file shares
• Port 445, exposed by default in a domain environment
	- Attackers use to pivot, should never be available to/from internet
• For attackers: Program execution and remote login!
	- Compare to SSH capabilities, but must be admin to use
• Used by the most dangerous exploits of the past
	- 9 Equation Group tools

Dont password re-use

SMB Versions:
• CIFS - Windows NT 4.0
• SMBI - Windows xp, Server 2000, 2003, and 2003 R2
• SMB2- Windows Vista, Server 2008
• SMB2.1 - Windows 7, Server 2008 R2
• SMB3.O/3.02 - Windows 8/8.1, Server 2012/2012 R2
• SMB3.1 — Windows 10, Server 2016
Clients will use highest version both sides support
SMB 1 MUST be turned off — extremely dangerous

### SSH

Your best friend, and worst enemy:
• Good: SSH allows dependable, secure remote connectivity
• Bad: You can use that capability to send anything over the tunnel
Need to...
• Tunnel out of your organization, skipping all filters? SSH!
• Route an external device's traffic to inside your network? SSH!
• Forward traffic through a dual-homed network machine? SSH!
• Use XII forwarding for GUI access from a remote machine? SSH!
Conclusion: We need to lock down and monitor SSH!

#Alert Allowing listing for SSH to internet, limit who can use it, what net segment from and where dst. Then monitor any connects outside that usage. 

SSH out, RDP IN

https://www.mandiant.com/resources/blog/bypassing-network-restrictions-through-rdp-tunneling

### RDP and VNC

Requires exploit of password

#Controls Prevent: Use host- and network-based firewalls to block
#Controls Prevent: Disable accounts from RDP that don't need access
#Alert Monitor: Evaluate all port 3389 traffic (use flow logs and FW logs)
#Alert Monitor: Use Windows login events to find odd RDP usage

VNC is port 5900 or application = VNC on NGFW then investigate

### Powershell Remoting

Like SSH for Windows, but implemented on top of other protocols
- PSRP = PowerShell Remoting Protocol
- WSMV = Web Services Management Extensions for Windows Vista
- SOAP = Simple Object Access Protocol
- PowerShell 6.0+ now supports SSH connections as well
Also known as WinRM (Windows Remote Management)
Connects using port 5985 (http)/5986 (https)
Workgroup or domain membership required
Off by default for desktops
On by default for servers

IP <> TCP <> HTTP/HTTPS <> SOAP <> WSMV (WinRM) <> PSRP

#Alert Detect traffic on port 5985/5986. Baseline attempts from pre-determined src and dest subnets and anything not in that pre-determined range is flagged as an alert. 

### FTP

• Old-school protocol for transferring files
• Still used in some networks, but should be phased out
• Action: Monitor for unexpected use, why?
	- It's used for exfiltration: Target credit card data was exfil'd via FTP
	- Passwords can be sniffed
	- Data can be tampered with
	- Many old servers are vulnerable to exploitation
• Especially if you do not use it, alert when seen!
• Not just the on perimeter, pay attention to internal, too!


#Alert Exclude known good and alert on any lillicit use of the protocol and stop the activity.

### Evil ICMP

Packet has Payload section with arbitrary contents
Instead of standard payload, smuggle data inside it.
 65507 bytes max payload size

### Any Protocol

Having a list of approved items (allow listing) is one of the strongest detection tactics because it doesn't rely on signatures, only deviations from known good (which means it can pick up both known and unknown attack styles). strive for a monitoring solution that will help them detect intrusions and post-exploitation activity,  known method or not.

Therefore, you must be able to watch for odd behavior
- Deep packet inspection to log metadata for transactions
- Protocol compliance on firewalls
- Network security monitoring
- Layer 3- and 4-based detection layered on top
- Outbound default deny
Well-defined subnets and traffic flow are key to attack detection!