# Solution

## URL
- [Protocols and Servers](https://tryhackme.com/room/protocolsandservers)

## Steps

### Task 2:
#### To which port will the telnet command with the default parameters try to connect?
1. The answer is `23`.

### Task 3:
#### Launch the attached VM. From the AttackBox terminal, connect using Telnet to 10.10.227.153 80 and retrieve the file flag.thm. What does it contain?
1. Run the command `telnet 10.10.227.153 80`.
2. Next type in `GET /flag.thm HTTP/1.1` press enter and type `host: telnet`, press enter twice.
3. The answer is `THM{e3eb0a1df437f3f97a64aca5952c8ea0}`.

### Task 4:
#### Using an FTP client, connect to the VM and try to recover the flag file. What is the flag?
1. Run these commands:
    ```
    ftp 10.10.227.153
    frank
    D2xc9CgD
    ls -al
    get ftp_flag.thm
    ```
2. The answer is `THM{364db6ad0e3ddfe7bf0b1870fb06fbdf}`.