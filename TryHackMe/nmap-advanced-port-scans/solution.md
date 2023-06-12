# Solution

## URL
- [Nmap Advanced Port Scans](https://tryhackme.com/room/nmap03)

## Steps

### Task 2:
#### In a null scan, how many flags are set to 1?
1. The answer is `0`.

#### In a FIN scan, how many flags are set to 1?
1. The answer is `1`.

#### In a Xmas scan, how many flags are set to 1?
1. The answer is `3`.

#### Start the VM and load the AttackBox. Once both are ready, open the terminal on the AttackBox and use nmap to launch a FIN scan against the target VM. How many ports appear as open|filtered?
1. Run the command `sudo nmap -v -sF 10.10.53.225`.
2. The answer is `7`.

#### Repeat your scan launching a null scan against the target VM. How many ports appear as open|filtered?
1. Run the command `sudo nmap -v -sN 10.10.53.225`.
2. The answer is `7`.

### Task 3:
#### In the Maimon scan, how many flags are set?
1. The answer is `2`.

### Task 4:
#### In TCP Window scan, how many flags are set?
The answer is `1`.

#### You decided to experiment with a custom TCP scan that has the reset flag set. What would you add after --scanflags?
1. The answer is `RST`.

#### The VM received an update to its firewall ruleset. A new port is now allowed by the firewall. After you make sure that you have terminated the VM from Task 2, start the VM for this task. Launch the AttackBox if you haven't done that already. Once both are ready, open the terminal on the AttackBox and use Nmap to launch an ACK scan against the target VM. How many ports appear unfiltered?
1. Run the command `sudo nmap -v -sA 10.10.232.167`.
2. The answer is `4`.

#### What is the new port number that appeared?
1. The asnwer is `443`.

#### Is there any service behind the newly discovered port number? (Y/N)
1. The answer is `N`.

### Task 5:
#### What do you need to add to the command sudo nmap 10.10.232.167 to make the scan appear as if coming from the source IP address 10.10.10.11 instead of your IP address?
1. The answer is `-S 10.10.10.11`.

#### What do you need to add to the command sudo nmap 10.10.232.167 to make the scan appear as if coming from the source IP addresses 10.10.20.21 and 10.10.20.28 in addition to your IP address?
1. The answer is `-D 10.10.20.21,10.10.20.28,ME`.

### Task 6:
#### If the TCP segment has a size of 64, and -ff option is being used, how many IP fragments will you get?
1. The `-f` flag will divide the data into 8 bytes or less, and adding another `-f` flag will divide it into `16` bytes or less.
2. So, `-ff` will divide `64` bytes of data into `64 / 16 = 4` fragments.
3. The answer is `4`.

### Task 7:
#### You discovered a rarely-used network printer with the IP address 10.10.5.5, and you decide to use it as a zombie in your idle scan. What argument should you add to your Nmap command?
1. The answer is `-sI 10.10.5.5`.

### Task 8:
#### Launch the AttackBox if you haven't done so already. After you make sure that you have terminated the VM from Task 4, start the VM for this task. Wait for it to load completely, then open the terminal on the AttackBox and use Nmap with nmap -sS -F --reason MACHINE_IP to scan the VM. What is the reason provided for the stated port(s) being open?
1. Run the command `sudo nmap -sS -F --reason 10.10.58.107`.
2. In the `Reason` column we can see that it received a `syn-ack` packet back.
3. The answer is `syn-ack`.