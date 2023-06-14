# Solution

## URL
- [Bandit Level 12 → Level 13](https://overthewire.org/wargames/bandit/bandit13.html)

## Steps

### Level Goal

#### The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work using mkdir. For example: mkdir /tmp/myname123. Then copy the datafile using cp, and rename it using mv (read the manpages!):
1. Enter `ls` to list contents of current working directory.
2. You will find a flag called `data.txt`.
3. Run these commands:
    ```
    cd /tmp
    mkdir mytest
    cd mytest
    mv ~/data.txt .
    xxd -r data.txt > test
    ```
4. Now use the file command to check the type of file: `file test`, it is a gzip compressed data.
5. Change the name to match the gzip extension (.gz): `mv test test.gz`.
6. Now use gzip, bunzip2 and tar extract commands depending upon the type of file you get till you get the actual password file:
    ```
    gunzip file-name.gz
    bunzip2 file-name
    tar -xvf file-name
    ```
7. Reading the password file using cat we get: `wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw`.
8. ssh to the next level: `ssh bandit13@bandit.labs.overthewire.org -p 2220`.