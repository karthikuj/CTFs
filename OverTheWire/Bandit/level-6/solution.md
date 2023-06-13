# Solution

## URL
- [Bandit Level 6 → Level 7](https://overthewire.org/wargames/bandit/bandit7.html)

## Steps

### Level Goal

#### The password for the next level is stored somewhere on the server and has all of the following properties:
    - owned by user bandit7
    - owned by group bandit6
    - 33 bytes in size
1. Enter `ls` to list contents of current working directory.
2. Change current working directory to `inhere` by typing `cd inhere`.
3. Enter `find / -user bandit7 -group bandit6 -size 33c 2> /dev/null` to find the file with the given specs.
5. Reading that using `cat /var/lib/dpkg/info/bandit7.password`, we get the password: `z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S`.
6. ssh to the next level: `ssh bandit7@bandit.labs.overthewire.org -p 2220`.