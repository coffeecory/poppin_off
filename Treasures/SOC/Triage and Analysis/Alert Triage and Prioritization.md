
![](../../../Media/Pasted%20image%2020230402192019.png)

![](../../../Media/Pasted%20image%2020230402203318.png)

![](../../../Media/Pasted%20image%2020230402203331.png)
![](../../../Media/Pasted%20image%2020230402203344.png)
![](../../../Media/Pasted%20image%2020230402203355.png)

#Alert If multiple alerts regarding one source inside your network that seems to be piling up alerts indicating sensitive information has been accessed and then an laert showing command line activity for the host zipping files up in mass or through #ThreatHunt 

#Alert A large number of FW failures on different ports from a single machine can be an attacker attempting to find a way out

#Alert Large Volume uploads

#Alert long running connections from a single machine

#Alert Look for threat matches to IP and Domain on proxy

#Alert Look at large uploads to dropbox like accounts

#Alert Use of non-standard archive tools, especially using passwords, breaking the file into pieces, or just run from the cmd line. Look for 7z or winrar with password flags via cmdline. Most people wont run these tools from the CMD line should be low-volume, High Fidelity Detection. 

#Alert Look for alot of Connections with URL data with base64 encoded parameters GET encoded exfil.




![](../../../Media/Pasted%20image%2020230402203407.png)

#Alert Look for worm-like malware and layer or group with other detections for malware famalies known to destroy disks such as Destover or Shamoon. 

#Alert Trigger on tools for secure data deletion, sdelete, built-in cipher.exe. On linux look for shred, wipe, and srm should all be alerted on. 

#Alert Look for install of drivers that may give attackers raw disk access and alllow them to dodge NTFS file permissions. Breaches like Destover and Shamoon, RawDisk driver from EldoS was used. 


![](../../../Media/Pasted%20image%2020230402203419.png)

#Enrichment Get User, Asset and Naming Convetion of servers and users job titles.

#SIEMENG Naming Convetion list and Critcal Asset Invetory Enrichment List.


![](../../../Media/Pasted%20image%2020230402203435.png)

#Alert Match URLs to known Threat Intel will catch oppurtunistic attacks, #Automation automate this look up outside if no match on threat feed then look at domain age or if domain not on open-source tools at all bc this is suspicous. 

#Alert  Files like domains if identified and are assoicated to malware families known to be used by Advanced attack groups raise priority. 

#Alert For files no knowledge is SUS, most cloud db's will come back with score and how common file is. #Automation here to look at file in sandbox and then if no data comes back then its highly likely to be a targeted attack. See Rob Joyce NSA TAO team comment about reputation service and exe.

#Triage Look for company logo in traige if you see this it most likely is a targeted attack.  Same goes for lists of targeted email users especially high profile or IT employees being hit with phishing. Watch phish alerts for this type of behavoir. 







![](../../../Media/Pasted%20image%2020230402203448.png)
![](../../../Media/Pasted%20image%2020230402203503.png)
![](../../../Media/Pasted%20image%2020230402203519.png)
![](../../../Media/Pasted%20image%2020230402203534.png)
![](../../../Media/Pasted%20image%2020230402203549.png)
![](../../../Media/Pasted%20image%2020230402203602.png)

---

## Alert and Links

LM-White-Paper-Intel-Driven-Defense.pdf
chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/LM-White-Paper-Intel-Driven-Defense.pdf

Endpoint Protection - Symantec Enterprise
https://community.broadcom.com/symantecenterprise/communities/community-home/librarydocuments/viewdocument?DocumentKey=f7186c7c-8a82-4a36-b6a1-15c5b80969ef&CommunityKey=1ecf5f55-9545-44d6-b0f4-4e4a7f5f5e68&tab=librarydocuments

Shamoon: Destructive Threat Re-Emerges with New Sting in its Tail | Symantec Enterprise Blogs
https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/shamoon-destructive-threat-re-emerges-new-sting-its-tail

Pareto principle - Wikipedia
https://en.wikipedia.org/wiki/Pareto_principle



