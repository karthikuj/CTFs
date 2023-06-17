# Solution

## URL
- [Bandit Level 17 → Level 18](https://overthewire.org/wargames/bandit/bandit18.html)

## Steps

### Level Goal

#### There are 2 files in the homedirectory: passwords.old and passwords.new. The password for the next level is in passwords.new and is the only line that has been changed between passwords.old and passwords.new. NOTE: if you have solved this level and see ‘Byebye!’ when trying to log into bandit18, this is related to the next level, bandit19:
1. Enter the command: `diff passwords.old passwords.new`.
2. In the last line we have the password for the next level: `hga5tuuCLF6fFzUpnagiMN8ssu9LFrdg`.
3. ssh to the next level: `ssh bandit18@bandit.labs.overthewire.org -p 2220`.