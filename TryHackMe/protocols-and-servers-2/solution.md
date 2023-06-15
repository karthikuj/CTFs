# Solution

## URL
- [Protocols and Servers 2](https://tryhackme.com/room/protocolsandservers2)

## Steps

### Task 2:
#### What do you need to add to the command sudo tcpdump to capture only Telnet traffic?
1. The answer is `port 23`.

#### What is the simplest display filter you can use with Wireshark to show only IMAP traffic?
1. The answer is `imap`.

### Task 3:
#### How many different interfaces does Ettercap offer?
1. The answer is `3`.

#### In how many ways can you invoke Bettercap?
1. The answer is `3`.

### Task 4:
#### DNS can also be secured using TLS. What is the three-letter acronym of the DNS protocol that uses TLS?
1. The answer is `DoT`.

### Task 5:
#### Use SSH to connect to MACHINE_IP as mark with the password XBtc49AB. Using uname -r, find the Kernel release?
1. Run the command: `ssh mark@10.10.87.193`.
2. Enter the password when asked - `XBtc49AB`.
3. Run the command: `uname -r`.
4. The answer is `5.4.0-84-generic`.

#### Use SSH to download the file book.txt from the remote system. How many KBs did scp display as download size?
1. Run the command `scp mark@10.10.87.193:/home/mark/book.txt .`.
2. The answer is `415`.

### Task 6:
#### We learned that one of the email accounts is lazie. What is the password used to access the IMAP service on 10.10.87.193?
1. Run the command: `hydra -VV -t 16 -l lazie -P /usr/share/wordlists/rockyou.txt 10.10.87.193 imap`.
2. The answer is `butterfly`.