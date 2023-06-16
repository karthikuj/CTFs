# ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

with open('enc', 'r') as rf:
    enc = rf.read()

for c in enc:
    for i in range(0, 128):
        for j in range(0, 128):
            if (i << 8) + j == ord(c):
                print(f'{chr(i)}{chr(j)}', end='')