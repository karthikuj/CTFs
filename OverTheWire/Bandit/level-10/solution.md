# Solution

## URL
- [Bandit Level 10 → Level 11](https://overthewire.org/wargames/bandit/bandit11.html)

## Steps

### Level Goal

#### The password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by several ‘=’ characters:
1. Enter `ls` to list contents of current working directory.
2. You will find a flag called `data.txt`.
3. Enter `base64 -d data.txt` to get the password: `6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM`.
4. ssh to the next level: `ssh bandit11@bandit.labs.overthewire.org -p 2220`.