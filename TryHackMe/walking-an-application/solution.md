# Solution

## URL
- [Walking an Application](https://tryhackme.com/room/walkinganapplication)

## Steps:

### Task 3:
#### HTML comment flag:
1. Go to page source of app.
2. Fing link to `/new-home-beta` in a comment.
3. Visit the page for the flag: `THM{HTML_COMMENTS_ARE_DANGEROUS}`.

#### Secret link flag:
1. Go to page source of app.
2. In an anchor tag (`<a>`) you will find link to a hidden page: `/secret-page`.
3. Visit it for the flag: `THM{NOT_A_SECRET_ANYMORE}`.

#### Directory listing flag:
1. Check the source code to find links to static files such as: `/assets/bootstrap.min.css`.
2. Now just go to `/assets/` directory to find a file named `flag.txt`.
3. Open that for the flag: `THM{INVALID_DIRECTORY_PERMISSIONS}`.

#### Framework flag:
1. Go to page source of app.
2. At the bottom you will find a website for the framework.
3. In that website check CHANGELOG.
4. It is revealed that at location `/tmp.zip` of applications using this framework backup file was leaked.
5. Download and extract for the flag: `THM{KEEP_YOUR_SOFTWARE_UPDATED}`.


### Task 4:
#### Flag behind the paywall:
1. Go to `/news/article?id=3` to find the paywall blocking the page.
2. Open dev tools.
3. You will find that `<div class="premium-customer-blocker">` is blocking the page.
4. Right click on that div and select `Delete element`.
5. Flag: `THM{NOT_SO_HIDDEN}`.

### Task 5:
#### Flag in the red box:
1. Open the page `/contact` and notice a red box appears and vanishes in a fraction of a second.
2. Open dev tools and go to sources tab to inspect all resources the current page is using.
3. Go to assets folder to find a file called `flash.min.js`.
4. In that file scroll to the bottom to find `flash['remove']();`.
5. Set a breakpoint just above this line by clicking on that line.
6. Reload the page and get the flag: `THM{CATCH_ME_IF_YOU_CAN}`.

### Task 6:
#### Flag in contact-msg network request:
1. Go to `/contact` page.
2. Open the network tab, fill and send the form.
3. Check the response of the request called `contact-msg` for the flag: `THM{GOT_AJAX_FLAG}`.