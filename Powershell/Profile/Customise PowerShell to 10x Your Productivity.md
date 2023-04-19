
Install Nerd Fonts

https://www.nerdfonts.com/

Set environment variables 
https://github.com/microsoft/winget-cli/issues/725

https://learn.microsoft.com/en-us/windows/package-manager/winget/

Step by step powershell profile

https://lazyadmin.nl/powershell/powershell-profile/

[How to make the ultimate Terminal Prompt on Windows 11 - This video is LONG and WORDY and DETAILED - YouTube](https://www.youtube.com/watch?v=VT2L1SXFq9U&t=960s)
- Powershell $PROFILE setup
- <a class="youtubeTimestamp" href="https://www.youtube.com/watch?v=VT2L1SXFq9U&t=1055">17:35</a>


	New-Item C:\\Users\\Administrator\\Documents\\PowerShell\\Microsoft.PowerShell_profile.ps1

OR 

	New-Item -Path $PROFILE -Type File -Force

	notepad $PROFILE

Add in the profile info from the https://www.jondjones.com/tactics/productivity/customise-your-powershell-prompt-like-a-boss/#:~:text=if%20(%24host.Name%20%2Deq%20%27ConsoleHost)

	Install-Module -Name PowerShellGet -Force -AllowClobber -AllowPrerelease



