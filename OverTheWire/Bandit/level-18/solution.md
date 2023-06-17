# Solution

## URL
- [Bandit Level 18 → Level 19](https://overthewire.org/wargames/bandit/bandit19.html)

## Steps

### Level Goal

#### The password for the next level is stored in a file readme in the homedirectory. Unfortunately, someone has modified .bashrc to log you out when you log in with SSH.:
1. Enter the command: `ssh bandit18@bandit.labs.overthewire.org -p 2220 -f "cat /home/bandit18/readme"`.
2. This will spit out the password for the next level: `awhqfNnAbc1naukrpqDYcF95h7HoMTrC`.
3. ssh to the next level: `ssh bandit19@bandit.labs.overthewire.org -p 2220`.