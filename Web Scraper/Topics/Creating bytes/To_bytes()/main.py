key = (int(input())).to_bytes(2, byteorder='little')
print(key[0] + key[1])
