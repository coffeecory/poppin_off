
![](../../Media/Pasted%20image%2020230402172355.png)

### File ID

![](../../Media/Pasted%20image%2020230402172726.png)

### File Command

![](../../Media/Pasted%20image%2020230402172933.png)

### Magic Bytes

![](../../Media/Pasted%20image%2020230402173104.png)
Must use HexDump for manual ID

### Nested Files

![](../../Media/Pasted%20image%2020230402173319.png)

See 00015be0 .PK and then c00 and c10 lines show the filename.xml file

### Polyglots


![](../../Media/Pasted%20image%2020230402174017.png)

### Unicode and Encoding

![](../../Media/Pasted%20image%2020230402174042.png)

UTF-8 encoded strings hex encoded values if read in by the SIEM will need to parse data in as so. 

#SIEMENG How does MSFT read in data for chinese characters and we see our SIEM and EDR tools cant interpret them properly we need to find a way to convert the UTF-? Encoding when we are sending those logs to the parsers or convert via Querying the logs. 

### Strings

![](../../Media/Pasted%20image%2020230402175026.png)


![](../../Media/Pasted%20image%2020230402175756.png)

![](../../Media/Pasted%20image%2020230402180139.png)


	strings -n 10 sample.exe

	strings -n 10 -e l -t x sample.exe

https://en.wikipedia.org/wiki/List_of_Unicode_characters


![](../../Media/Pasted%20image%2020230402180511.png)

Scrap strings out of memory during dynamic analysis where packed or compressed strings may not be picked up by static analysis. 

![](../../Media/Pasted%20image%2020230402180859.png)


