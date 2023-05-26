# Solution

## URL
- [Active Reconnaissance](https://tryhackme.com/room/activerecon)

## Steps

### Task 2:
#### Browse to the [following website](https://static-labs.tryhackme.cloud/sites/networking-tcp/) and ensure that you have opened your Developer Tools on AttackBox Firefox, or the browser on your computer. Using the Developer Tools, figure out the total number of questions.
1. Go to the website and open dev tools (`Ctrl+Shift+I`).
2. Open the sources tab and go to the `script.js` file.
3. In there, there is a `questions` object which has 8 questions.
4. So the answer is `8`.

### Task 3
#### Which option would you use to set the size of the data carried by the ICMP echo request?
1. Run the command `ping --help` to learn more about the ping command.
2. You will notice the flag `-s` is there to set the number of data bytes to be sent.

#### What is the size of the ICMP header in bytes?
1. Run the command `man ping` to open the man pages for the ping command.
2. Now enter `/header` to search for the keyword header in the man pages. To go to the next search result press `n`.
3. You will notice that the ICMP header size is `8` bytes.

#### Does MS Windows Firewall block ping by default? (Y/N)
1. The answer is `Y`.

#### Deploy the VM for this task and using the AttackBox terminal, issue the command ping -c 10 10.10.57.66. How many ping replies did you get back?
1. The answer is `10`.

### Task 4:
#### In Traceroute A, what is the IP address of the last router/hop before reaching tryhackme.com?
1. In the codeblock there are 2 IPs in the last line.
2. The first one is the answer: `172.67.69.208`.

#### In Traceroute B, what is the IP address of the last router/hop before reaching tryhackme.com?
1. In the second codeblock check the last line.
2. The answer is: `104.26.11.229`.

#### In Traceroute B, how many routers are between the two systems?
1. The answer is `26`.

### Task 5:
#### What is the name of the running server?
1. Run the command: `telnet 10.10.57.66 80`.
2. Enter `GET / HTTP/1.1`. And then enter: `Host: example`, hit enter twice.
3. You will get the response headers from the website.
4. The answer is `Apache`.

#### What is the version of the running server (on port 80 of the VM)?
1. In the response headers, in the `Server` header to be specific, you can see the version number.
2. The answer is `2.4.10`.

### Start the VM and open the AttackBox. Once the AttackBox loads, use Netcat to connect to the VM port 21. What is the version of the running server?
1. Run the command: `nc 10.10.42.245 21`.
2. In the output it will show you `220 debra2.thm.local FTP server (Version 6.4/OpenBSD/Linux-ftpd-0.17) ready.`.
3. So the answer is `0.17`.