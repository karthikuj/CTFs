# Solution

## URL
- [Bandit Level 11 → Level 12](https://overthewire.org/wargames/bandit/bandit12.html)

## Steps

### Level Goal

#### The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions:
1. Enter `ls` to list contents of current working directory.
2. You will find a flag called `data.txt`.
3. [Decode](https://www.dcode.fr/rot-13-cipher) the ROT13 cipher to get the password: `JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv`.
4. ssh to the next level: `ssh bandit12@bandit.labs.overthewire.org -p 2220`.