# Solution

## URL
- [Passive Reconnaissance](https://tryhackme.com/room/passiverecon)

## Steps

### Task 3:
#### When was TryHackMe.com registered?
1. Run `whois tryhackme.com` and you will find that it was registered on 2018-07-05T19:46:15Z.
2. The hint shows the format as `YYYYMMDD`, so the answer is `20180705`.

#### What is the registrar of TryHackMe.com?
1. The answer is `namecheap.com`.

#### Which company is TryHackMe.com using for name servers?
1. The answer is `cloudflare.com`.

### Task 4:
#### Check the TXT records of thmlabs.com. What is the flag there?
1. For this you can either use `nslookup` or `dig`.
2. Using `nslookup`: `nslookup -type=TXT thmlabs.com`
3. Using `dig`: `dig thmlabs.com TXT`
4. The flag: `THM{a5b83929888ed36acb0272971e438d78}`.

### Task 5:
#### Lookup tryhackme.com on DNSDumpster. What is one interesting subdomain that you would discover in addition to www and blog?
1. The answer is `remote`.

### Task 6:
#### According to Shodan.io, what is the 2nd country in the world in terms of the number of publicly accessible Apache servers?
1. Go to shodan and search `apache`.
2. Check the top countries list on the left. The answer is `Germany`.

#### Based on Shodan.io, what is the 3rd most common port used for Apache?
1. Check the top ports list on th left. The answer is `8080`.

#### Based on Shodan.io, what is the 3rd most common port used for nginx?
1. On shodan search `nginx`.
2. Check the top ports list on the left. The answer is `888`.