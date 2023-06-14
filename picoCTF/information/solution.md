# Solution

## URL
- [information](https://play.picoctf.org/practice/challenge/186?page=1)

## Steps

### Description

#### Files can always be changed in a secret way. Can you find the flag?
1. Download task file.
2. Run exiftool: `exiftool cat.jpg`
3. You will find a base64 encoded string in the value of `License`.
4. Decode that: `echo "cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9" | base64 -d`
5. Got the flag: `picoCTF{the_m3tadata_1s_modified}`.