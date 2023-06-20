from Crypto.Util.number import long_to_bytes

with open('values', 'r') as rf:
    values = rf.readlines()

n = int(values[2].split(':')[1].strip())
c = int(values[1].split(':')[1].strip())
e = int(values[3].split(':')[1].strip())
print(f'c = {c}\nn = {n}\ne = {e}\n')

p = 1955175890537890492055221842734816092141
q = 670577792467509699665091201633524389157003
print(f'From factordb.com we got the factors for n:\np = {p}\nq = {q}\n')

print('PHI = (p - 1)(q - 1), so:')
PHI = (p - 1) * (q - 1)
print(f'PHI = {PHI}\n')

print('Now d (private key) can be calculated with e ^ -1 (Mod PHI):')
d = pow(e, -1, PHI)
print(f'd = {d}\n')

print(f'In RSA a message (m) is ciphered (c) using c = m ^ e (Mod n)\nAnd deciphered using m = c ^ d (Mod n).')
m = pow(c, d, n)
print(f'm = {m}\n')

flag = long_to_bytes(m).decode()
print(f'flag = {flag}')