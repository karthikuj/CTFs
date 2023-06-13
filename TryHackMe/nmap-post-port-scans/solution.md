# Solution

## URL
- [Nmap Post Port Scans](https://tryhackme.com/room/nmap04)

## Steps

### Task 2:
#### Start the target machine for this task and launch the AttackBox. Run nmap -sV --version-light 10.10.28.150 via the AttackBox. What is the detected version for port 143?
1. Run the command `nmap -sV --version-light 10.10.28.150`.
2. The answer is `Dovecot imapd.

#### Which service did not have a version detected with --version-light?
1. The answer is `rpcbind`.

### Task 3:
#### Run nmap with -O option against 10.10.28.150. What OS did Nmap detect?
1. Start AttackBox and open the terminal.
2. Run the command `sudo nmap -O 10.10.28.150`.
3. The answer is `Linux`.

### Task 4:
#### Knowing that Nmap scripts are saved in /usr/share/nmap/scripts on the AttackBox. What does the script http-robots.txt check for?
1. Open the script `/usr/share/nmap/scripts/http-robots.txt.nse` in a text editor.
2. Check the description.
3. The answer is `disallowed entries`.

#### Can you figure out the name for the script that checks for the remote code execution vulnerability MS15-034 (CVE2015-2015-1635)?
1. Run the command `ls /usr/share/nmap/scripts/*cve2015*`.
2. In the output you will get the name of the file which checks for `CVE-2015-1635`.
3. The answer is `http-vuln-cve2015-1635`.

#### Launch the AttackBox if you haven't already. After you ensure you have terminated the VM from Task 2, start the target machine for this task. On the AttackBox, run Nmap with the default scripts -sC against 10.10.101.5. You will notice that there is a service listening on port 53. What is its full version value?
1. Run the command `sudo nmap -sS -sC 10.10.101.5`.
2. The answer is `9.9.5-9+deb8u19-Debian`.

#### Based on its description, the script ssh2-enum-algos “reports the number of algorithms (for encryption, compression, etc.) that the target SSH2 server offers.” What is the name of the key exchange algorithms (kex_algorithms) that relies upon “sha1” and is supported by 10.10.101.5?
1. Run the command `sudo nmap -sS --script "ssh2-enum-algos" 10.10.101.5`.
2. The answer is `diffie-hellman-group14-sha1`.

#### Terminate the target machine of the previous task and start the target machine for this task. On the AttackBox terminal, issue the command scp pentester@10.10.16.164:/home/pentester/* . to download the Nmap reports in normal and grepable formats from the target virtual machine. Note that the username pentester has the password THM17577. Check the attached Nmap logs. How many systems are listening on the HTTPS port?
1. Run the scp command `scp pentester@10.10.16.164:/home/pentester/* .` with the password `THM17577`.
2. Run the grep command `grep -o "443/open" scan_172_17_network.gnmap | wc`.
3. The answer is `3`.

#### What is the IP address of the system listening on port 8089?
1. Run the command `grep "8089" scan_172_17_network.gnmap`.
2. The answer is `172.17.20.147`.