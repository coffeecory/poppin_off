
### Log Pipeline

![](../../Media/Pasted%20image%2020230402162054.png)

### Log Collection Methods

![](../../Media/Pasted%20image%2020230402162456.png)

Agentless = logs into machine from remote and pulls logs or sched script run on the host that push logs outbound. 


### Win log Collection Options 

![](../../Media/Pasted%20image%2020230402162957.png)

### Linux Log Collection Options

![](../../Media/Pasted%20image%2020230402163511.png)

### Unsctructered Logs

![](../../Media/Pasted%20image%2020230402163843.png)

### Structured Log Formats

![](../../Media/Pasted%20image%2020230402164207.png)

Remember though nested objects cant be parsed using Regex. but have to be parsed using another tool. 

### SIEM Centric Formats

![](../../Media/Pasted%20image%2020230402164459.png)

### Log Structure Importance

![](../../Media/Pasted%20image%2020230402164650.png)

#SIEMENG Parse out key fields of each log, write some of those key fields into a DB that can be queried at comparable high speeds. Devo is failing at this for FW and WinEventLogs


### Effecient SIEM Searches

![](../../Media/Pasted%20image%2020230402164955.png)

#SIEMENG 1- Ask SIEM vendor what are the fields that are being indexed into a DB for our different logsource's? Not all fields are indexed into quickly searchable DB's...

### Log Enrichment

![](../../Media/Pasted%20image%2020230402170012.png)

Enrich Dest IP, Site known bad, How old, User accessing. 

### Normalization or Common Information Models

![](../../Media/Pasted%20image%2020230402170137.png)

Analyst should know fields available in all data models ingested into the SIEM. 

Normalization can be done at ingestion by renaming fields in flight, or after as a secondary field, preserving the orignal name, or at search time on the fly to leave OG data intact. 

### Log Normalization Categorization 

![](../../Media/Pasted%20image%2020230402170716.png)

Categorization can be possible to find logins in a generic way that does not require analysts to know Win EID codes or other specific abouts how a login event would look. They just know there is a category for login. 

#SIEMENG Predifined categories built in with parsers that will attempt to auto-categorize all events it understands; or more basic. Tagging is a cheater way if SIEM doesn't support. Ensure all login events are tagged with login then anlaysts know that tags for login exist they can pull all login events and search user=mike or tag=login.

### Log Storage

![](../../Media/Pasted%20image%2020230402171222.png)

### Log LifeCycle

![](../../Media/Pasted%20image%2020230402171607.png)

### Questions for the SIEM Engineer

![](../../Media/Pasted%20image%2020230402171754.png)

### Log Collection, Parsing, and Normalization 

![](../../Media/Pasted%20image%2020230402171918.png)





