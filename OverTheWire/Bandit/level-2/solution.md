# Solution

## URL
- [Bandit Level 2 → Level 3](https://overthewire.org/wargames/bandit/bandit3.html)

## Steps

### Level Goal

#### The password for the next level is stored in a file called spaces in this filename located in the home directory.
1. Enumerate the current working directory with `ls`.
2. Trying to read the file we got `spaces in this filename` gives an error because cat thinks that it is 4 different files because of the spaces.
3. We can fix that by running any of the following:
    ```
    cat "spaces in this filename"
    cat spaces\ in\ this\ filename
    cat *
    ```
4. Got the password: `aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG`
4. ssh into next level with the new password: `ssh bandit3@bandit.labs.overthewire.org -p 2220`.