# Solution

## URL
- [Python Wrangling](https://play.picoctf.org/practice/challenge/166?page=1)

## Steps

### Description

#### Python scripts are invoked kind of like programs in the Terminal... Can you run this Python script using this password to get the flag?
1. Dowanload task files.
2. Run the command `python3 ende.py -d flag.txt.en < pw.txt | grep -Po "picoCTF\{.*?\}" | tee flag-decoded.txt`
3. Got the flag: `picoCTF{4p0110_1n_7h3_h0us3_ac9bd0ff}`.