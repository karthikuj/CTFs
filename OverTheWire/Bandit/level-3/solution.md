# Solution

## URL
- [Bandit Level 3 → Level 4](https://overthewire.org/wargames/bandit/bandit4.html)

## Steps

### Level Goal

#### The password for the next level is stored in a hidden file in the inhere directory.
1. Enter `ls` to list contents of current working directory.
2. Change current working directory to `inhere` by typing `cd inhere`.
3. Enter `ls -a` to list everything in the directory including hidden files.
4. Read the hidden file `.hidden` using `cat` command: `cat .hidden`.
5. We got the password: `2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe`.
6. ssh to the next level: `ssh bandit4@bandit.labs.overthewire.org -p 2220`.