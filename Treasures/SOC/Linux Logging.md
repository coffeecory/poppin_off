Linux logging is very different than Windows logging:
OS written logs are in syslog format

Traditionally used plaintext files for logging instead of
channels
- journald system service replaces plain text files on some systems with
a more structured binary format, similar to Windows

Event IDs are not used — no standardization

Categorized by a facility and severity

Format varies per message

Can be sent over UDP, TCP, and optionally encrypted

### Syslog Disambiguation

Syslog is an overloaded term: "syslog format logs are picked up
by a syslog daemon and sent to the SIEM via syslog protocol"

1. Syslog format
	- How the actual log text should be formatted
1. Syslog daemon — Rsyslog, syslog-ng, syslogd, etc.
	- Program that facilitates writing text files/forwarding logs
1. Syslog network protocol
	- Network traffic — traditionally used UDP port 514

Format:
```
                   <time> <hostname> <log source> : <message>
Example: Dec 11 16: 41: 40 ubuntu dhc1ient[64507] : DHCPACK of 192.168.42.147 from 192.168.42.254
```

Unencrypted over UDP 514 defualt

UDP 1k size limit may be violated
TCP 4k size limit can also use TLS encrypt

### Syslog Daemons

Syslogd
- The original syslog project from 1980
Syslog-ng
- Released in 1998 to improve syslogd
- Easier to read config for filtering, free/premium edition
Rsyslog
- Created in 2004 as alternative to syslog-ng
- Syslogd config, Linux version is free, Windows agent available
Both syslog-ng and rsyslog support many output formats!

In addition, they support multiple output formats such as sending logs directly to a log broker such as RabbitMQ or Kafka and can output directly to some databases as well, such as MySQL MongoDB, Elasticsearch. or even Hadoop hdfs. Syslog-ng. which was made by Balabit, has recently been acquired by the company One Identity and offers an open source as well as a premium edition of their agent. Rsyslog also has a Windows agent which offers basic, professional. and enterprise versions that can be used as a third-party collection tool.

![Pasted image 20230401235746.png](../../Media/Pasted%20image%2020230401235746.png)

	/etc/rsyslog.d/50-defualt.conf

	var/log/auth.log

	var/log/messages

log msg > syslog daemon >all auth or all local log

/var/log/auth. log or /var/log/secure
• Authentication attempts collected here
• Sorted by process (sshd, sudo, su,
/var/log/syslog or /var/log/messages
Generic system activity, first place to check for most things
• Similar to Windows System log
/var/ log/ audit/ kern . log — Kernel logs (noisy)
/ var/ log/ audit/ audit . log — Auditd logs
/var/ log/ audit/ u fw . log — Firewall logs
/var/10g/apache2 (or httpd) / access . log — Apache logs
/var/log/httpd/mysqld.log — MySQL logs

### Systemd journal

A newer method of Linux logging to fix syslog pains:
systemd-journald is a system service that collects log data
Stores information in /var/ log/ j ournal/ (machineid] /
Uses a structured binary format, similar to Windows EVTX
Log contents are primarily text, but can contain binary data
• Allow structured format and custom fields, unlike normal syslog
• View using journalctl command, specify "unit" with -u
	$ journalctl -u suricata

### Other CMD line logging Linux

https://github.com/Sysinternals/SysmonForLinux

https://github.com/a2o/snoopy

Auditd - built in subsystem
