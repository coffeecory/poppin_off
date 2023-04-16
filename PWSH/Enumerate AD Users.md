```powershell
$date = (Get-Date).ToString("yyyyMMdd")  
$path = "C:\\TEMP\\"  
$NameUsers = "ADusers"  
$OutputUsers = $date + "ADusers.csv"  
  
New-Item $path$OutputUsers -Force  
$SearchBase = "DC=example,DC=example1,DC=com"  
$DC = "[myDC.example.com](http://mydc.example.com/)"  
Get-ADuser  -Server $DC -SearchBase $SearchBase -filter '(ObjectClass -eq "user")' -Properties Enabled, cn, givenName, mail, ou, sn, objectClass, memberOf, sAMAccountName, objectguid -ResultSetSize $null|select Enabled, cn, givenName, mail, @{n='OU';e={$_.DistinguishedName -replace '^.*?,(?=[A-Z]{2}=)'}}, sn, objectClass,  @{n='MemberOf'; e= { ( $_.memberof | % { (Get-ADObject $_).Name }) -join "," }}, sAMAccountName, objectguid | Export-Csv  $path$OutputUsers -Encoding UTF8 -delimiter '|' -NoTypeInformation | % { $_ -replace '"', ""}
```

How to view the value of MaxGroupOrMemberEntries
https://social.technet.microsoft.com/Forums/en-US/35972b25-f453-4b8c-9bb0-96eda51a018d/how-to-view-the-value-of-maxgroupormemberentries?forum=winserverDS

powershell - Get-ADGroupMember : The size limit for this request was exceeded - Stack Overflow
https://stackoverflow.com/questions/46078880/get-adgroupmember-the-size-limit-for-this-request-was-exceeded/46079714#46079714

Get-ADUser (ActiveDirectory) | Microsoft Learn
https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-aduser?view=windowsserver2022-ps

How to view the value of MaxGroupOrMemberEntries
https://social.technet.microsoft.com/Forums/en-US/35972b25-f453-4b8c-9bb0-96eda51a018d/how-to-view-the-value-of-maxgroupormemberentries?forum=winserverDS