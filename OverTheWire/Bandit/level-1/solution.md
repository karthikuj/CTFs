# Solution

## URL
- [Bandit Level 1 → Level 2](https://overthewire.org/wargames/bandit/bandit2.html)

## Steps

### Level Goal

#### The password for the next level is stored in a file called - located in the home directory
1. Check the files in current working directory with `ls`.
2. We found a file named `-`, trying to read that with `cat -` gives nothing probably because it is treating it as the start of some command line argument.
3. But we are able to fix that by prepending `./`, so the full command is `cat ./-`.
4. We got the password for the next level: `rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi`.
5. ssh into the next level: `ssh bandit2@bandit.labs.overthewire.org -p 2220`.