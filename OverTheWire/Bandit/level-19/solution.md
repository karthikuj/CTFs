# Solution

## URL
- [Bandit Level 19 → Level 20](https://overthewire.org/wargames/bandit/bandit20.html)

## Steps

### Level Goal

#### To gain access to the next level, you should use the setuid binary in the homedirectory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary.:
1. Enter the command: `./bandit20-do cat /etc/bandit_pass/bandit20`.
2. This will spit out the password for the next level: `VxCazJaVykI6W36BkBU0mJTCM8rR95XT`.
3. ssh to the next level: `ssh bandit20@bandit.labs.overthewire.org -p 2220`.