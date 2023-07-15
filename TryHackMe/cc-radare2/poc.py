s1 = "83797f6e736e737e" # the output from sym.get_password
s2 = "796f756469646974" # hex for "youdidit"

difference = int(s1, 16) - int(s2, 16)

print(f"The difference is: {hex(difference)}")

passDec = int(s2, 16) - difference
print(f"Hex of password is: {hex(passDec)}")