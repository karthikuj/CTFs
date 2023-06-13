# Solution

## URL
- [Bandit Level 5 → Level 6](https://overthewire.org/wargames/bandit/bandit6.html)

## Steps

### Level Goal

#### The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:
    - human-readable
    - 1033 bytes in size
    - not executable
1. Enter `ls` to list contents of current working directory.
2. Change current working directory to `inhere` by typing `cd inhere`.
3. Enter `find ./ ! -executable -size 1033c -exec file {} \; | grep ASCII` to find the file with the given specs.
5. Reading that using `cat ./maybehere07/.file2`, we get the password: `P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU`.
6. ssh to the next level: `ssh bandit6@bandit.labs.overthewire.org -p 2220`.