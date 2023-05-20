# Solution

## URL:
- [Subdomain Enumeration](https://tryhackme.com/room/subdomainenumeration)

## Steps:

### Task 1:
#### What is a subdomain enumeration method beginning with B?
1. The answer is `Brute force`.

#### What is a subdomain enumeration method beginning with O?
1. The answer is `OSINT`.

#### What is a subdomain enumeration method beginning with V?
1. The answer is `Virtual host`.

### Task 2:
#### What domain was logged on crt.sh at 2020-12-26?
1. Go to [crt.sh](https://crt.sh/) and type `tryhackme.com` to find its Certificate Transparency (CT) logs.
2. Search for `2020-12-26` and you'll find the domain `store.tryhackme.com`.

### Task 3:
#### What is the TryHackMe subdomain beginning with B discovered using the above Google search?
1. Use the google dork `-site:www.tryhackme.com  site:*.tryhackme.com` to find subdomains for `tryhackme.com`.
2. In the search results find the subdomains starting with `b`.
3. You will find the subdomain `blog.tryhackme.com`.

### Task 4:
#### What is the first subdomain found with the dnsrecon tool?
1. Click `View Site`.
2. Use the simulator to find the domain `api.acmeitsupport.thm`.
3. In real life we can use [dnsrecon](https://www.kali.org/tools/dnsrecon/) to do the same.

### Task 5:
#### What is the first subdomain discovered by sublist3r?
1. Click `View Site`.
2. Use the simulator to find the domain `web55.acmeitsupport.thm`.
3. In real life we can use [sublist3r](https://github.com/aboul3la/Sublist3r) or [amass](https://github.com/owasp-amass/amass) or [subfinder](https://github.com/projectdiscovery/subfinder) to do the same.

### Task 6:
#### What is the first subdomain discovered?
1. Some subdomains aren't always hosted in publically accessible DNS results, such as development versions of a web application or administration portals. Instead, the DNS record could be kept on a private DNS server or recorded on the developer's machines in their /etc/hosts file which maps domain names to IP addresses. Since multiple websites can exist on a server, the server knows which website to serve using the `Host` header.
2. So we will fuzz the `Host` header using ffuf.
3. Use the command: `ffuf -w /usr/share/wordlists/SecLists/Discovery/DNS/namelist.txt -H "Host: FUZZ.acmeitsupport.thm" -u http://10.10.0.42`.
4. Now this will give lots of garbage, take note of the response size of garbage output and filter that out using the `-fs` flag.
5. Use the command: `ffuf -w /usr/share/wordlists/SecLists/Discovery/DNS/namelist.txt -H "Host: FUZZ.acmeitsupport.thm" -u http://10.10.0.42 -fs 2395`
6. Subdomain discovered: `delta`

#### What is the second subdomain discovered?
1. In the output of the last command we will find the answer to this one as well: `yellow`.