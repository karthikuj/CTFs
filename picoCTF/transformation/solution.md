# Solution

## URL
- [Transformation](https://play.picoctf.org/practice/challenge/104?page=1)

## Steps

### Description

#### I wonder what this really is... enc 
    ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
1. Download task file
2. Run `poc.py` file.
3. Got the flag: `picoCTF{16_bits_inst34d_of_8_d52c6b93}`.
