# Solution

## URL
- [Bandit Level 4 → Level 5](https://overthewire.org/wargames/bandit/bandit5.html)

## Steps

### Level Goal

#### The password for the next level is stored in the only human-readable file in the inhere directory. Tip: if your terminal is messed up, try the “reset” command.
1. Enter `ls` to list contents of current working directory.
2. Change current working directory to `inhere` by typing `cd inhere`.
3. Enter `ls -a` to list everything in the directory including hidden files.
4. Use the file command to see the type of file: `file ./*`
5. In the output we can see that only `-file07` is ASCII text.
6. Reading that using `cat ./-file07`, we get the password: `lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR`.
7. ssh to the next level: `ssh bandit5@bandit.labs.overthewire.org -p 2220`.