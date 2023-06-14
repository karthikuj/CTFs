with open('code.txt', 'r') as rf:
    codes = rf.readlines()

flag = ''.join(map(chr, [int(x.strip()) for x in codes]))
print(flag)