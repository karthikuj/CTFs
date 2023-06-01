# Solution

## URL
- [Nmap Basic Port Scans](https://tryhackme.com/room/nmap02)

## Steps 

### Task 2:
#### Which service uses UDP port 53 by default?
1. The answer is `DNS`.

#### Which service uses TCP port 22 by default?
1. The answer is `SSH`.

#### How many port states does Nmap consider?
1. The answer is `6`.

#### Which port state is the most interesting to discover as a pentester?
1. The answer is `open`.

### Task 3:
#### What 3 letters represent the Reset flag?
1. The answer is `RST`.

#### Which flag needs to be set when you initiate a TCP connection (first packet of TCP 3-way handshake)?
1. The answer is `SYN`.

### Task 4:
#### Which port number was closed in the scan above but is now open on this target VM?
1. Run a scan with NMAP like this: `nmap -sT 10.10.64.42 | tee nmap-tcp-connect-scan.txt`
2. The answer is `110`.

#### What is Nmap’s guess about the newly installed service?
1. The answer is `pop3`.

### Task 5:
#### Launch the VM. Some new server software has been installed since the last time we scanned it. On the AttackBox, use the terminal to execute nmap -sS 10.10.141.53. What is the new open port?
1. Run a scan with NMAP like this: `sudo nmap -sS 10.10.141.53 | tee nmap-tcp-syn-scan.txt`.
2. The answer is `6667`.

#### What is Nmap’s guess of the service name?
1. The answer is `irc`.

### Task 6:
#### Launch the VM. On the AttackBox, use the terminal to execute nmap -sU -F -v 10.10.165.81. A new service has been installed since the last scan. What is the UDP port that is now open?
1. Run a scan with NMAP like this: `sudo nmap -sU -F -v 10.10.165.81 | tee nmap-udp-scan.txt`.
2. The answer is `53`.

#### What is the service name according to Nmap?
1. The answer is `domain`.

### Task 7:
#### What is the option to scan all the TCP ports between 5000 and 5500?
1. The answer is `-p5000-5500`.

#### How can you ensure that Nmap will run at least 64 probes in parallel?
1. The answer is `--min-parallelism=64`.

#### What option would you add to make Nmap very slow and paranoid?
1. The answer is `-T0`.