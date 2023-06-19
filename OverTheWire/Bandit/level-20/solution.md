# Solution

## URL
- [Bandit Level 20 → Level 21](https://overthewire.org/wargames/bandit/bandit21.html)

## Steps

### Level Goal

#### There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21). NOTE: Try connecting to your own network daemon to see if it works as you think:
1. Create 2 ssh sessions.
2. In the first one run `echo "VxCazJaVykI6W36BkBU0mJTCM8rR95XT" | nc -lvnp 4444`.
2. In the second one run `./suconnect 4444`.
3. You will get the password for the next level in the first session: `NvEJF7oVjkddltPSrdKEFOllh9V1IBcq`.
4. ssh to the next level: `ssh bandit21@bandit.labs.overthewire.org -p 2220`.