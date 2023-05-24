# Solution

## URL
- [Burp Suite Basics](https://tryhackme.com/room/burpsuitebasics)

## Steps

### Task 2:
#### Which edition of Burp Suite will we be using in this module?
1. The answer is `Burp Suite Community`.

#### Which edition of Burp Suite runs on a server and provides constant scanning for target web apps?
1. The answer is `Burp Suite Enterprise`.

#### Burp Suite is frequently used when attacking web applications and ______ applications.
1. The answer is `Mobile`.

### Task 3:
#### Which Burp Suite feature allows us to intercept requests between ourselves and the target?
1. The answer is `proxy`.

#### Which Burp tool would we use if we wanted to bruteforce a login form?
1. The answer is `intruder`.

### Task 7:
#### In which Project options sub-tab can you find reference to a "Cookie jar"?
1. The answer is `sessions`.

#### In which User options sub-tab can you change the Burp Suite update behaviour?
1. The answer is `misc`.

#### What is the name of the section within the User options "Misc" sub-tab which allows you to change the Burp Suite keybindings?
1. The answer is `hotkeys`.

#### If we have uploaded Client-Side TLS certificates in the User options tab, can we override these on a per-project basis (Aye/Nay)?
1. The answer is `aye`.

### Task 8:
#### Which button would we choose to send an intercepted request to the target in Burp Proxy?
1. The answer is `Forward`.

#### [Research] What is the default keybind for this?
1. The answer is `Ctrl+F`.

### Task 9:
#### There is one particularly useful option that allows you to intercept and modify the response to your request.
1. The answer is `response to this request`.

### Task 13:
#### What is the flag you receive?
1. Add the given IP to scope and stop logging everything else.
2. Go and manually click through all the links on the webpage.
3. In Burp Target > Site Map, we can see the tree of all links for our website.
4. In that a request has been made to `/5yjR2GLcoGoij2ZK` which stands out from others.
5. Click on that and check the response for the flag: `THM{NmNlZTliNGE1MWU1ZTQzMzgzNmFiNWVk}`.
6. Another way is after manually clicking on all links go to Proxy > HTTP history > filter. In `filter by search item` just enter `THM{` and this will filter out the HTTP message which has the flag.

#### What is the typical severity of a Vulnerable JavaScript dependency?
1. The answer is `low`.