# Solution

## URL:
- [Content Discovery](https://tryhackme.com/room/contentdiscovery)

## Steps:

### Task 2:
#### Disallowed directory:
1. Go to `/robots.txt.`.
2. You will find the directory `/staff-portal` in the `Disallow:` directive.

### Task 3:
#### Favicon Framework:
1. Run this to get the md5 hash of favicon file: `curl -s 'https://static-labs.tryhackme.cloud/sites/favicon/images/favicon.ico' | md5sum > content-discovery/favicon-md5.hash`
2. Now look up the hash on [OWASP favicon db](https://wiki.owasp.org/index.php/OWASP_favicon_database).
3. You will find that it is for `cgiirc` framework.

### Task 4:
#### sitemap.xml secret area:
1. Go to `/sitemap.xml`.
2. You will find a path called: `/s3cr3t-area`.

### Task 5:
#### X-Flag flag:
1. Run the command: `curl http://10.10.64.158 -v`.
2. Check the response headers for the flag: `X-FLAG: THM{HEADER_FLAG}`.

### Task 6:
#### Admin portal flag:
1. Check comments in the source code of website and you'll find the link to framework website.
2. In the framework's website check docs to find links and default creds of the admin portal: `/thm-framework-login` & `admin:admin`.
3. Using this login to the admin portal to find the flag: `THM{CHANGE_DEFAULT_CREDENTIALS}`.

### Task 7:
#### Dork operator:
1. The way to filter search results by site is by using the `site:` operator.

### Task 8:
#### Tool to identify website tech:
1. A popular browser extension called `wappalyzer` can be used for this.

### Task 9:
#### Wayback machine:
1. You can go to `https://archive.org/web/` to check historical archive of websites.

### Task 10:
#### Git:
1. Git is a `version control system`.

### Task 11:
#### S3 Buckets:
1. Amazon S3 buckets URLs end with `.s3.amazonaws.com`.

### Task 12:
#### Directory starting with `/mo`:
1. Run the command: `ffuf -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt -u http://10.10.64.158/FUZZ`.
2. You will discover a directory called: `/monthly`.

#### Log file:
1. In the output of the above command you will also find a log file called `/development.log`.