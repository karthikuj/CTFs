# Solution

## URL
- [Bandit Level 14 → Level 15](https://overthewire.org/wargames/bandit/bandit15.html)

## Steps

### Level Goal

#### The password for the next level can be retrieved by submitting the password of the current level to port 30000 on localhost.:
1. In the last level we were told that the password is in `/etc/bandit_pass/bandit14`.
2. Reading that we get: `fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq`.
3. Now we need to submit it to port 30000 on localhost, so run these:
    ```
    nc localhost 30000
    fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq
    ```
4. Got the password for the next level: `jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt`.
5. ssh to the next level: `ssh bandit15@bandit.labs.overthewire.org -p 2220`.