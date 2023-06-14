# Solution

## URL
- [Bandit Level 9 → Level 10](https://overthewire.org/wargames/bandit/bandit10.html)

## Steps

### Level Goal

#### The password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by several ‘=’ characters:
1. Enter `ls` to list contents of current working directory.
2. You will find a flag called `data.txt`.
3. Enter `strings data.txt | grep "==="` to get the password: `G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s`.
4. ssh to the next level: `ssh bandit10@bandit.labs.overthewire.org -p 2220`.