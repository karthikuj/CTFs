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