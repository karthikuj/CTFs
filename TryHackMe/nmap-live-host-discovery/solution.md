# Solution

## URL:
- [Nmap Live Host Discovery](Nmap Live Host Discovery)

## Steps:

### Task 2:
#### How many devices can see the ARP Request?
1. The answer is `4`.

#### Did computer6 receive the ARP Request? (Y/N)
1. The answer is `N`, because it is in a different subnet.

#### How many devices can see the ARP Request?
1. The answer is `4`.

#### Did computer6 reply to the ARP Request? (Y/N)
1. The answer is `Y`.

### Task 3:
#### What is the first IP address Nmap would scan if you provided 10.10.12.13/29 as your target?
1. To check the list of targets NMAP will scan we can use the `-sL` flag.
2. When we run `nmap -sL 10.10.12.13/29`, the first target in the list is `10.10.12.8`.
3. So the answer is `10.10.12.8`.

#### How many IP addresses will Nmap scan if you provide the following range 10.10.0-255.101-125?
1. In the first range (`0-255`) we have 256 options.
2. In the second range (`101-125`) we have 25 options.
3. Together they can make 256 x 25 options.
4. The answer is `6400`.

### Task 4:
#### What is the type of packet that computer1 sent before the ping?
1. The answer is `ARP request`.

#### What is the type of packet that computer1 received before being able to send the ping?
1. The answer is `ARP response`.

#### How many computers responded to the ping request?
1. The answer is `1`.

#### What is the name of the first device that responded to the first ARP Request?
1. The answer is `router`.

#### What is the name of the first device that responded to the second ARP Request?
1. The answer is `computer5`.

#### Send another Ping Request. Did it require new ARP Requests? (Y/N)
1. The answer is `N`.

### Task 5:
#### How many devices are you able to discover using ARP requests?
1. The answer is `3`.

### Task 6:
#### What is the option required to tell Nmap to use ICMP Timestamp to discover live hosts?
1. The answer is `-PP`.

#### What is the option required to tell Nmap to use ICMP Address Mask to discover live hosts?
1. The answer is `-PM`.

#### What is the option required to tell Nmap to use ICMP Echo to discover life hosts?
1. The answer is `-PE`.