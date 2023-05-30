# Solution

## URL
- [Git Happens](https://tryhackme.com/room/githappens)

## Steps

### Enumerate:
1. Run a full NMAP port scan: `sudo nmap -v -sS -p- 10.10.48.67 | tee nmap-scan.txt`.
2. A website is running on port 80, fuzz the directories/files: `sudo ffuf -u http://10.10.48.67/FUZZ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-lowercase-2.3-medium.txt -mc 200,301,302,403 -fs 6890 -v | tee ffuf-dir-fuzz.txt`.
3. `/robots.txt` and `/sitemap.xml` did not reveal anything.
4. The index page's source code has some obfuscated JS code, let's [deobfuscate](https://deobfuscate.io/) that.
5. Saved it in the file `index-script-deobfuscated.js`.

### Task 1:
#### Find the Super Secret Password