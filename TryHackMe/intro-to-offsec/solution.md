# Solution

## URL
- [Intro to Offensive Security](https://tryhackme.com/room/introtooffensivesecurity)

## Steps
1. Click on `Start Machine`.
2. Start attack box by clicking on `Show Split View`.
3. Run GoBuster: `gobuster -u http://fakebank.com -w wordlist.txt dir`
4. You will get a hidden page at `/bank-transfer`
5. Transfer $2000 from account no. 2276 to 8881.
6. Go back to home page, you will find the answer: `BANK-HACKED`.