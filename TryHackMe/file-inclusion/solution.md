# Solution

## URL
- [File Inclusion](https://tryhackme.com/room/fileinc)

## Steps

### Task 3:
#### What function causes path traversal vulnerabilities in PHP?
1. The answer is `file_get_contents`.

### Task 4:
#### Give Lab #1 a try to read /etc/passwd. What would the request URI be?
1. In the lab, go to `Lab #1`.
2. In the text box enter `welcome.php` and submit.
3. The URL is `/lab1.php?file=welcome.php`.
4. If we change the value of `file` parameter to `/etc/passwd`, we will be able to see the contents of the file.
5. So, the request URI would be `/lab1.php?file=/etc/passwd`.

#### In Lab #2, what is the directory specified in the include function?
1. Go to `Lab #2`.
2. Enter `welcome.php` and submit.
3. The URL is `/lab2.php?file=welcome.php`.
4. If we change the value of `file` parameter to `/etc/passwd`, we will get an error:
`Warning: include(includes//etc/passwd) [function.include]: failed to open stream: No such file or directory in /var/www/html/lab2.php on line 26`
5. So the directory specified in the `include` function is `includes` as evident from the error message.
7. To exploit this, we will need to traverse to the root directory first: `/lab2.php?file=../../../../etc/passwd`.

### Task 5:
#### Give Lab #3 a try to read /etc/passwd. What is the request look like?
1. Go to `Lab #3`.
2. Enter a non existent value such as `gohan` and submit.
3. In the error we can see that it is inside `includes/` directory and `.php` has been appended to our string.
4. Also, the server path is disclosed `/var/www/html/lab3.php`.
5. Now if we try to traverse the path with `/lab3.php?file=../../../../etc/passwd`, there is still the `.php` we need to bypass.
6. Append NULL BYTE character `%00` to close the string and disregard the `.php` that was appended.
7. So the full URI would be: `/lab3.php?file=../../../../etc/passwd%00`.

#### Which function is causing the directory traversal in Lab #4?
1. Go to `Lab #4`.
2. Enter a non existent value such as `gohan` and submit.
3. The answer is in the error message: `file_get_contents`.

#### Try out Lab #6 and check what is the directory that has to be in the input field?
1. Go to `Lab #6`
2. Enter a non existent value such as `gohan` and submit.
3. The answer is in the error message: `THM-profile`.

#### Try out Lab #6 and read /etc/os-release. What is the VERSION_ID value?
1. So we need to add `THM-profile` in the path.
2. Let us first enter the valid file `THM-profile/tryhackme.txt`(given in placeholder of input box)
3. Now let us traverse the path after the `THM-profile` part, `THM-profile/../etc/os-release`.
4. We can see in the error message the full server path is `/var/www/html/lab6.php`, so will need to go back 4 directories.
5. So the full URI would be: `/lab6.php?file=THM-profile/../../../../etc/os-release`.
6. The value of `VERSION_ID` as seen in the file is `12.04`.

### Task 8:
#### Capture Flag1 at /etc/flag1
1. Go to `/challenges/chall1.php`.
2. It says that the form is broken and we need to send a `POST` requiest with `file` parameter.
3. Enter `welcome.php` and submit while capturing the request in burp.
4. Send the request to repeater.
5. Right click on the request > `Change request method`.
6. Now send the request, it will work as intended.
6. Change the value of file parameter to an unintended value such as `gohan`.
7. In the error message we can see that they are not prepending or appending anything, we also got the server path `/var/www/html/chall1.php`.
8. Change the value of file parameter to `/etc/flag1` for the flag `F1x3d-iNpu7-f0rrn`.

#### Capture Flag2 at /etc/flag2
1. Go to `/challenges/chall2.php`, we are greeted with the message: `Only admins can access this page!`.
2. If we open the cookies in `Application` tab in chrome dev tools, we can see a cookie named `THM` with value `Guest`.
3. Now change the value of that cookie to `Admin` and refresh the page for admin privileges.
4. We can now see an error message saying: `Warning: include(includes/Admin.php) [function.include]: failed to open stream: No such file or directory in /var/www/html/chall2.php on line 37`.
5. So maybe it is using the value of the `THM` cookie?
6. Let's change the value to `../../../../etc/flag2` and refresh the page again.
7. Now the error is showing `include(includes/../../../../etc/flag2.php)`, so it is definitely using the value of the cookie. 
8. It is also appending `.php` to the cookie value, we can try to bypass that by appending the NULL BYTE character to our payload.
9. Change the cookie value to `../../../../etc/flag2%00` and refresh the page.
10. Found the flag: `c00k13_i5_yuMmy1`.

#### Capture Flag3 at /etc/flag3
1. Go to `/challenges/chall3.php`.
2. Enter `gohan` and submit for the error message: `Warning: include(gohan.php) [function.include]: failed to open stream: No such file or directory in /var/www/html/chall3.php on line 30`
3. In the error message we can see that the application is appending `.php` to the param value.
4. But if you notice it added another forward slash in the URI: `/challenges//chall3.php?file=gohan`
4. Try the payload: `/etc/flag3%00`, notice that it is stripping the forward slash, that explains that extra forward slash they added.
5. Try this payload: `jchdsd78346127.,\/.:"}{@*(@jksdghajk`.
6. In the error message we can see that they removed all special characters and numbers from the payload.
7. Change the request method to post and send the request, in this we can see nothing is being stripped out, so the application is probably using `$_REQUESTS`.
8. Try the payload: `/etc/flag3%00` for the flag: `P0st_1s_w0rk1in9`.