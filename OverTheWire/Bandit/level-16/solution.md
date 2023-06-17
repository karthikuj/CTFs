# Solution

## URL
- [Bandit Level 16 → Level 17](https://overthewire.org/wargames/bandit/bandit17.html)

## Steps

### Level Goal

#### The credentials for the next level can be retrieved by submitting the password of the current level to a port on localhost in the range 31000 to 32000. First find out which of these ports have a server listening on them. Then find out which of those speak SSL and which don’t. There is only 1 server that will give the next credentials, the others will simply send back to you whatever you send to it.:
1. Enter the command: `nmap -vv -p 31000-32000 localhost -sV`.
2. We can see that 2 ports have ssl on it `31518` and `31790`. Out of them 31518 is `ssl/echo` and 31790 is `ssl/unknown`.
3. Connect to port `31790` using openssl: `openssl s_client -connect localhost:31790`.
4. Enter the password for the current level: `JQttfApK4SeyHwDlI9SXGR50qclOAil1`. It spits out a private key, copy it to a file with the name `bandit17.pem`.
5. Secure the file by changing permissions: `chmod 600 bandit17.pem`.
6. ssh to the next level: `ssh -i bandit17.pem bandit17@bandit.labs.overthewire.org -p 2220`.