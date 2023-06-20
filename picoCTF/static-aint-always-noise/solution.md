# Solution

## URL
- [Static ain't always noise](https://play.picoctf.org/practice/challenge/163?page=1)

## Steps

### Description

#### Can you look at the data in this binary: static? This BASH script might help!
1. Download the task files
2. Give executable permission to the script using: `chmod u+x ltdis.sh`.
3. Execute the script `./ltdis.sh`.
4. You will get the flag in `static.ltdis.strings.txt` file.
5. Another way to solve this is just by using this command: `strings static | grep pico`.
6. The flag is `picoCTF{d15a5m_t34s3r_6f8c8200}`. 