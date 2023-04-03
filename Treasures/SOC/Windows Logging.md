Log collection...isn't that someone else's job?
- Maybe, but understanding it will vastly improve your capability as an analyst
- Understanding logs is understanding the available tools
- Interpreting logs is at least a daily occurrence!
- To succeed, we must know:
	- Log formats
	- Log content
	- Log collection


Windows logging is much more complex than Linux:
• The OS and applications write to various log channels
• Channels are recorded in XML-formatted .evtx files
• Files must be interpreted with tool
Cannot read directly like Linux log text files
• Windows Event Viewer is most common tool
Shows channels on the left side
Application, Security, System are most familiar
There are MANY channels beyond this, some useful, some not

	C:\Windows\System32\winevt\Logs folder

OS built-in options:
- Windows audit policies
Additional logging add-ons
- Sysmon
- Custom scripts
Applications
- Depends on settings and capabilities
- May log to Windows events
- My write separate log files

Per channel, logs written with:
- Level: Information, Warning, or Error?
- Source (Provider): What program wrote the log?
- EventlD: Unique number for event type
- Task Category: Additional description of event

### Windows Event Templates

```powershell
Get-WinEvent -ListProvider* | Select name
//This command will list all providers in the
system
```
 
```powershell
$provider = Get-WinEvent -ListProvider
Microsoft-Windows-Security-Auditing //This
commands sets the provider to the Windows
Security Log
```

```Powershell
$provider.events | Where-Object {$_.id -eq
4624} | select id,template,description | fl #*
//This command selects event id 4624 and
dumps the ID, Template (pictured above),
and the description (shown on the next
slide).
```

However you modify the template it will display this way in Message view in the general tab and it will appear with Security ID %1. 

![Pasted image 20230401231420.png](../../Media/Pasted%20image%2020230401231420.png)

Not easily auto parsible by SIEM. For extraction of the data. it is much better to use the structure XML source or a log agent that converts it to another format like JSON in a reliable way. Trying to write a regular expression to parse the fields out of the message format of the log will be an exercise in frustration due to the conditional nature and unstructured format and, in doing so, lead to sub-par parsing with missed
fields.

System XML + EvetData XML + Intrumentation Manifest Template = Message

### Channels of Intrest

Commonly collected:
• Application
. Security
• System
Less commonly collected, but very useful:
- PowerShell/Operational
- Security-Mitigations/(Kernel & User Mode), EMET
- Code Integrity/Operational
- AppLocker/(EXE and DLL, MSI and script, ...)
- Windows Defender/Operational
- Windows Firewall with Advanced Security/Firewall

• What is your Windows Auditing policy, and
do you have any third-party programs
generating additional information?


• What about scripts or programs that write
their own logs outside of the Windows event
collection system?


• What log channels and additional sources
of data are you picking up?


• In your SIEM, do you see the XML fields, the
General tab "message" version of the log, or
both? Does your SIEM properly parse all the
fields?


---

Greater Visibility Through PowerShell Logging | Mandiant
https://www.mandiant.com/resources/blog/greater-visibility

Understand and use attack surface reduction (ASR) | Microsoft Learn
https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/overview-attack-surface-reduction?view=o365-worldwide

Using Event Viewer with AppLocker (Windows) | Microsoft Learn
https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/applocker/using-event-viewer-with-applocker

Microsoft Defender Antivirus event IDs and error codes | Microsoft Learn
https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide

Audit MPSSVC Rule-Level Policy Change (Windows 10) | Microsoft Learn
https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-mpssvc-rule-level-policy-change

Sysmon - Sysinternals | Microsoft Learn
https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon

Defining Severity Levels - Win32 apps | Microsoft Learn
https://learn.microsoft.com/en-us/windows/win32/wes/defining-severity-levels

Identifying the Provider - Win32 apps | Microsoft Learn
https://learn.microsoft.com/en-us/windows/win32/wes/identifying-the-provider

Defining Events - Win32 apps | Microsoft Learn
https://learn.microsoft.com/en-us/windows/win32/wes/defining-events

Message Text Files - Win32 apps | Microsoft Learn
https://learn.microsoft.com/en-us/windows/win32/eventlog/message-text-files

How to get a list of XML data name elements in (Windows 10) | Microsoft Learn
https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/how-to-list-xml-elements-in-eventdata