# Solution

## URL
- [Nice netcat...](https://play.picoctf.org/practice/challenge/156?page=1)

## Steps

### Description

#### There is a nice program that you can talk to by using this command in a shell: $ nc mercury.picoctf.net 21135, but it doesn't speak English...
1. Run the command: `nc mercury.picoctf.net 21135 | tee code.txt`.
2. It looks like it is printing out ASCII values for the characters in the flag.
3. Get the flag using the poc we made: `python3 poc.py`.
4. Got the flag: `picoCTF{g00d_k1tty!_n1c3_k1tty!_afd5fda4}`.