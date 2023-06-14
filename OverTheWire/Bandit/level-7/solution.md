# Solution

## URL
- [Bandit Level 7 → Level 8](https://overthewire.org/wargames/bandit/bandit8.html)

## Steps

### Level Goal

#### The password for the next level is stored in the file data.txt next to the word millionth:
1. Enter `ls` to list contents of current working directory.
2. You will find a flag called `data.txt`.
3. Enter `grep "millionth" data.txt` to get the password: `TESKZC0XvTetK0S9xNwm25STk5iWrBvP`.
4. ssh to the next level: `ssh bandit8@bandit.labs.overthewire.org -p 2220`.