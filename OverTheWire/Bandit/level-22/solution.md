# Solution

## URL
- [Bandit Level 22 → Level 23](https://overthewire.org/wargames/bandit/bandit23.html)

## Steps

### Level Goal

#### A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.:
1. Run the command `ls -al /etc/cron.d/`.
2. Notice there is a cron called `crontab_bandit23`. Read that using cat.
3. It is running the script `/usr/bin/cronjob_bandit23.sh` every minute. Read that using cat.
4. That script is storing the password to a file whose name is determined by the md5sum of the string `I am user <username>`. Get the password using command `cat /tmp/$(echo I am user bandit23 | md5sum | cut -d ' ' -f 1)`.
5. Got the password: `QYw0Y2aiA672PsMmh9puTQuhoz8SyR2G`.
4. ssh to the next level: `ssh bandit23@bandit.labs.overthewire.org -p 2220`.