# Solution

## URL
- [Bandit Level 15 → Level 16](https://overthewire.org/wargames/bandit/bandit16.html)

## Steps

### Level Goal

#### The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL encryption. Helpful note: Getting “HEARTBEATING” and “Read R BLOCK”? Use -ign_eof and read the “CONNECTED COMMANDS” section in the manpage. Next to ‘R’ and ‘Q’, the ‘B’ command also works in this version of that command…:
1. Enter the command: `openssl s_client -connect localhost:30001`.
2. Enter the password for current level.
3. Got the password for the next level: `JQttfApK4SeyHwDlI9SXGR50qclOAil1`.
4. ssh to the next level: `ssh bandit16@bandit.labs.overthewire.org -p 2220`.