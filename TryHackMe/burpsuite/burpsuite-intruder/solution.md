# Solution

## URL
- [BurpSuite Intruder](https://tryhackme.com/room/burpsuiteintruder)

## Steps

### Task 2:
#### Which section of the Options sub-tab allows you to control what information will be captured in the Intruder results?
1. The answer is `attack results`.

#### In which Intruder sub-tab can we define the "Attack type" for our planned attack?
1. The answer is `positions`.

### Task 5:
#### If you were using Sniper to fuzz three parameters in a request, with a wordlist containing 100 words, how many requests would Burp Suite need to send to complete the attack?
1. The answer is `3 x 100 = 300`. So `300`.

#### How many sets of payloads will Sniper accept for conducting an attack?
1. The answer is `1`.

#### Sniper is good for attacks where we are only attacking a single parameter, aye or nay?
1. The answer is `aye`.

### Task 6:
#### What would the body parameters of the first request that Burp Suite sends be?
1. Go to `/support/login/` and login while capturing the request.
2. Send it to intruder using `Ctrl+I`.
3. Set the attack type to `battering ram`.
4. In payload list add `admin` and `Guest`.
5. Start the attack. Go to the first request and copy the request body.
6. The answer is `username=admin&password=admin`.

### Task 7:
#### What is the maximum number of payload sets we can load into Intruder in Pitchfork mode?
1. The answer is `20`.

### Task 8:
#### We have three payload sets. The first set contains 100 lines; the second contains 2 lines; and the third contains 30 lines. How many requests will Intruder make using these payload sets in a Cluster Bomb attack?
1. The answer is `100 x 2 x 30 = 6000`. So `6000`.

### Task 9:
#### Which payload type lets us load a list of words into a payload set?
1. The answer is `simple list`.

#### Which Payload Processing rule could we use to add characters at the end of each payload in the set?
1. The answer is `add suffix`.

### Task 10:
#### Bruteforce the login page.
1. Download and unzip the task files.
2. Go to `/support/login/` and login while capturing the request.
3. Send it to intruder using `Ctrl+I`.
4. Add the username and password fields to payload positions.
5. Set attack type as `Cluster bomb`.
6. In the payloads tab, in payload set 1 load the usernames.txt file we extracted and in payload set 2 load the passwords.txt file.
7. Start the attack and wait for it to complete.
8. Sort the attacks by Length and you will find an attack that stands out. The credentials are: `m.rivera:letmein1`.

### Task 11:
#### Which attack type is best suited for this task?
1. The answer is `sniper`.

#### Either using the Response tab in the Attack Results window or by looking at each successful (i.e. 200 code) request manually in your browser, find the ticket that contains the flag. What is the flag?
1. After logging in click on any of the tickets assigned to the user.
2. Intercept the request and send it to intruder.
3. Add the number at the end of the url as the payload position and set the attack type as sniper.
4. Set the payload type as `Numbers` and set the values to 1 to 100 with a step of 1.
5. Start the attack and sort it by status code to easily see all requests with 200 status code.
6. Check those requests with 200 status code and in the response of one of those you will find the flag: `THM{MTMxNTg5NTUzMWM0OWRlYzUzMDVjMzJl}`.