# Solution

## URL
- [Server Side Request Forgery](https://tryhackme.com/room/ssrfqi)

## Steps

### Task 1:
#### What does SSRF stand for?
1. The answer is `Server Side Request Forgery`.

#### As opposed to a regular SSRF, what is the other type?
1. The answer if `blind` ssrf.

### Task 2:
#### What is the flag from the SSRF Examples site?
1. In the challenge change the value of server param to `server.website.thm/flag?id=9&x=`.
2. Got flag: `THM{SSRF_MASTER}`.

### Task 3:
#### What website can be used to catch HTTP requests from a server?
1. The answer is `requestbin.com`.

### Task 4:
#### What method can be used to bypass strict rules?
1. The answer is `open redirect`.

#### What IP address may contain sensitive data in a cloud environment?
1. The answer is `169.254.169.254`.

#### What type of list is used to permit only certain input?
1. The answer is `allow list`.

#### What type of list is used to stop certain input?
1. The answer is `deny list`.

### Task 5:
#### What is the flag from the /private directory?
1. Sign up and go to `/customers/new-account-page`.
2. Inspect element for any of the radio button and you will find the path to the image in the `value` attribute.
3. Change the value of the `value` attribute to `private` and click on `Update Avatar`.
4. You will get the error saying `URL cannot start with private`.
5. Now change the value of the `value` attribute to `assets/../private` and click on `Update Avatar`.
6. Now your current avatar image will appear empty, right click on it and inspect element.
7. Copy the base64 encoded string and run the command: `echo "VEhNe1lPVV9XT1JLRURfT1VUX1RIRV9TU1JGfQ==" | base64 -d`.
8. Got the flag: `THM{YOU_WORKED_OUT_THE_SSRF}`.