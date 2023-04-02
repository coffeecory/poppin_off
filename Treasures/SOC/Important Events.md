


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

