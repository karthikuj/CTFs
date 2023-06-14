# Solution

## URL
- [Bandit Level 8 → Level 9](https://overthewire.org/wargames/bandit/bandit9.html)

## Steps

### Level Goal

#### The password for the next level is stored in the file data.txt and is the only line of text that occurs only once:
1. Enter `ls` to list contents of current working directory.
2. You will find a flag called `data.txt`.
3. Enter `cat data.txt | sort | uniq -u` to get the password: `EN632PlfYiZbn3PhVK3XOGSlNInNE00t`.
4. ssh to the next level: `ssh bandit9@bandit.labs.overthewire.org -p 2220`.