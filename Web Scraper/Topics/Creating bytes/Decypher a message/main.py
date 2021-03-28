encoded = input()
key = (int(input())).to_bytes(2, byteorder='little')
key = key[0] + key[1]
decoded = [chr(ord(char) + key) for char in encoded]
print(''.join(decoded))
