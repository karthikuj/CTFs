# Solution

## URL
- [Bandit Level 0 → Level 1](https://overthewire.org/wargames/bandit/bandit1.html)

## Steps

### Level Goal

#### The password for the next level is stored in a file called readme located in the home directory. Use this password to log into bandit1 using SSH. Whenever you find a password for a level, use SSH (on port 2220) to log into that level and continue the game.
1. After completing the previous level you will be logged-in to the system.
2. Enter `ls` to see the files in the current working directory, there is a file named readme.
3. Read the file using the `cat` command: `cat readme`.
4. You will get the password for `bandit1` - `NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL`, ssh into it: `ssh bandit1@bandit.labs.overthewire.org -p 2220`
5. You will be logged-in.