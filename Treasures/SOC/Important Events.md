

### EventlD 4104 — 

Script block logging
• Contains commands run, if turned on in audit policy
• Noisy!!!
• Note location


### EventID 4624/4625

Windows logins are an extremely
frequent event
Fields of primary interest:
- Account Name
- Account Domain
- Logon Type
- Network Info (if remote)
Lots of noise from "computer
accounts"! ($ on the end)

Type 2 = Local accounts
Type 11 = Domain accounts
Type 10 = RDP
Type 5 = Domain account if a service with aits own account logs in. 
Type 3 = Win Explorer file share or other SMB connection. 

### Event ID 4648

RunAs style logins:
• Like "sudo" for Windows
User X becoming account Y
• Used by attackers for pivoting
through network
• Tells you who (subject)
• Which account they used
• Where it was used (Target)

#Alert Look for anom of a user connecting to PC they should not be connecting runas

### Linux Logins

In contrast to Windows, Linux logins are relatively simple
• Unfortunately, they are inconsistent and span multiple lines
• Usually reference "pam" — pluggable authentication module

Example SSH login with key:

```bash

ubuntu sshd[459) : Connection from 123.45 .67.89 port 57356 on 99. 99.99.99 port 22

ubuntu sshd[459J : Postponed publickey for root from 123.45.67.89 port 57356
ssh2 [preauth]

ubuntu sshd[459] : Accepted publickey for root from 123.45.67.89 port 57356
ssh2: RSA SHA256:a098RFOF9sdffaf09vijw877afsd1MfMFKLEe

ubuntu sshd[459J : pam unix (sshd : session) : session opened for user root by (uid=O)

ubuntu sshd[459) : Starting session: shell on pts/O for root from 123.45.67.89 port 57356 id O

```

### Linux Login Failures

```bash
Logon failures can take many forms:
Bad Username:
Time ubuntu sshd[num]: Invalid User Pi from <ip>
```
![/Media/Pasted image 20230402130015.png](../../Media/Pasted%20image%2020230402130015.png)

Diff fails for SSH, Desktop manager, others

### Process Creation 

![](../../Media/Pasted%20image%2020230402135909.png)

Good use of powershell with a konw script, from a bad one. Add this to the fact that the path, hash and signature(or lack of) of a program can ez help ID anomalous program execution in the environment.

![](../../Media/Pasted%20image%2020230402140338.png)

#### Event ID 1 vs Event ID 4688  process creation
Sysmon benifit - Signed programs that give descritpion, product name, and company. Get multiple hashes directly inside the log. But Sysmon is makeshift EDR. 

#Alert This allows us to run hash based checks to not only have to interact with the file but also letting us find devs not signing there code. This requires PKI and also tracking down users and harping on them. Figure out how to do this with your EDR tools.

### AuditD

![](../../Media/Pasted%20image%2020230402141125.png)

AuditD output example

![](../../Media/Pasted%20image%2020230402141513.png)

### Snoopy Process Creation Logger

![](../../Media/Pasted%20image%2020230402141729.png)

Perfection solution fallacy: "Just because it's not perfect, doesn't mean it's not useful."

#Alert linux sys enum commands above.

### Windows Firewall and Advanced Security Logs

![](../../Media/Pasted%20image%2020230402142212.png)

### Intrepreting Linux IPTables FW logs

![](../../Media/Pasted%20image%2020230402142557.png)

Layer 3/4 information and protocol are most likely to be of use in identifying interesting traffic.

### Object Access Auditing Win

![](../../Media/Pasted%20image%2020230402142849.png)
 
Event ID 4660 An object was deleted can catch Ransomware.

### Service Creation Win EventID 7045/4697

![](../../Media/Pasted%20image%2020230402143445.png)



#Alert Look at Service File Name, Service Name, and Service Account all services have a name as a label and sometimes evil ones will try to blend in and use an innocuous sounding name like "google updater". Also Random names to avoid signature detections. Create detection to look for random .exe files. Most malware will use the local system defualt to run triage knowing this.

#ThreatHunt Look in random directories for Service File Names like temp. Should it be there? 

### New Scheduled Task

![](../../Media/Pasted%20image%2020230402150224.png)


### USB PNP Events

![](../../Media/Pasted%20image%2020230402150728.png)

Log shows Vendor ID, location for the physical port, Device Name

Show VID and PID act like OUI MACs for SUB

#Alert Look for USB policy volations by creating an allow list and spotting misconfigurations. 

#lookups Auto Enrichment to logs if values from USB DB can be preloaded for lookup at search time. 

### New User Creation and Group Mgmt

![](../../Media/Pasted%20image%2020230402151512.png)

### Windows Defender

![](../../Media/Pasted%20image%2020230402151830.png)

Collect 1006 and 1116 if at all

### Powershell Script Block log

![](../../Media/Pasted%20image%2020230402152200.png)

https://www.sans.org/podcasts/blueprint/powershell-for-the-blue-team-with-josh-johnson/

4104 event decodes the obsfucated powershell commands. bc its logging actual text that is executed by the PWSH engine. 

Doesn't log output of command but can enable transcription logging for that info. 

### Kerberos Auth and TGS

![](../../Media/Pasted%20image%2020230402152640.png)

##### Kerberos Auth Visualized

![](../../Media/Pasted%20image%2020230402153059.png)

#### Kerberos Log Events

![](../../Media/Pasted%20image%2020230402153541.png)

### Event ID 4768: Kerb Auth Ticket TGT requested

![](../../Media/Pasted%20image%2020230402153829.png)

0 = Success if not 0 lookup fail code

IOE = User account success or fail combined with ip. If see TGT for a device the user doesn't own, that may mean their account has been compromised. If  we are not sure what device a user was using at time or user active at certian IP addr, 4768 can tie that togther. 

We can also go deeper was it a normal pass vs smart card using preauth type field and what encryption suite in Ticket encryption type field. Outlier and Anomolies may be worth investigating as well. 

#Alert Apply allow or deny lists for attempts to authenticate sensitive or deactivated accounts. or use reg expressions to look for non-conforming account name authentication attempts. 

#Triage or #ThreatHunt Group by account name, domain, or result codes to look for attackers or misconfigs. $ = Computer accounts and Certain failures for that will generate EID = 4771 Kerb preauth failed

### EID 4769/4770 Kerb Service Ticket was Requested/Renewed


![](../../Media/Pasted%20image%2020230402154934.png)

Service Name and SID shows the account or Computer Object the ticket was requested for when possible the WEV maps SID to name. 

#Triage See ServiceName for FileShare notice the client address and then pivot to the logs for fileshare and see login following the event where ticket was used. use fail code to see if something had gone wrong. 

#Alert Anomaly detection for 4769 and 4770 events are same as 4768. Sus number of attempts or usage of accounts from unexpected locations, plus any anomalies in the extra fields can be a tip off of an attack. 

Filter Failure Code 0x20 TGS ticket Expired on 4769 little to no sec value.

### Logging in with Kerberos

![](../../Media/Pasted%20image%2020230402155910.png)

#Alert Look for Any connection using NTLM package Name in the 4624 logs and look for NTLMv1 or LM. 

![](../../Media/Pasted%20image%2020230402160444.png)

Securing Windows Workstations: Developing a Secure Baseline – Active Directory Security
https://adsecurity.org/?p=3299

Securing Domain Controllers to Improve Active Directory Security – Active Directory Security
https://adsecurity.org/?p=3377

Spotting the Adv. with Win Event Log Monitoring
https://cryptome.org/2014/01/nsa-windows-event.pdf
https://www.ultimatewindowssecurity.com/webinars/register.aspx?id=281
https://www.redblue.team/2015/09/spotting-adversary-with-windows-event_21.html

Cheat-Sheets — Malware Archaeology
https://www.malwarearchaeology.com/cheat-sheets/

Windows Security Log Encyclopedia
https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/default.aspx

Event Forwarding Guidance
https://github.com/nsacyber/Event-Forwarding-Guidance

https://securitythings.medium.com/windows-event-collecting-8-simple-steps-to-protect-your-organizations-pcs-using-nsa-standards-dcf79c0d88b3

https://itworldjd.wordpress.com/2016/05/21/detecting-intrusions-using-windows-event-log-monitoring/

https://www.cyber.gov.au/sites/default/files/2021-10/PROTECT%20-%20Windows%20Event%20Logging%20and%20Forwarding%20%28October%202021%29.pdf

https://hannahsuarez.github.io/2021/Winlogbeat_NSAEventstoMonitor/

https://hannahsuarez.github.io/

#FutureGoals Consider spending
some regular time keeping up on new attack
techniques and ideally synthesizing them in a lab
to try to understand what types of marks they
will make in the environment