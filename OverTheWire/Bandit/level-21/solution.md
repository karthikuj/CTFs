# Solution

## URL
- [Bandit Level 21 → Level 22](https://overthewire.org/wargames/bandit/bandit22.html)

## Steps

### Level Goal

#### A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.:
1. Run the command `ls -al /etc/cron.d/`.
2. Notice there is a cron called `crontab_bandit22`. Read that using cat.
3. It is running the script `/usr/bin/cronjob_bandit22.sh` every minute. Read that using cat.
4. That script is storing the password to `/tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv`. Read that using cat.
5. Got the password: `WdDozAdTM2z9DiFEQ2mGlwngMfj4EZff`.
4. ssh to the next level: `ssh bandit22@bandit.labs.overthewire.org -p 2220`.