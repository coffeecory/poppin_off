Select-String -Path "Web\*.txt" -Pattern "suspendedpage.cgi" -Context 1 | Select-Object -ExpandProperty Context -First 1 | Format-List


EDIT: If you want just text _and_ get rid of the single line you've mentioned:

```powershell
Get-ChildItem | 
    where {(New-TimeSpan -Start $_.LastWriteTime).TotalHours -lt 24} | 
    select-string 'SUMMARY' -context 0,10 | 
    foreach {@($_.Line) + @($_.Context.PostContext) } | 
    where { $_ -notmatch 'Files updated on right side' }
```

```powershell
Get-Content *.yml | Select-String -Pattern tags -Context 0,5 | where {$_ -notmatch "String to not match on"}
```

```Powershell
Select-String -Pattern "tags" -Path .\* -Context 0,5 | Out-File -Path C:\Stor\TestFile.txt
```
