line = input()
encrypted_line = [chr(ord(char) + 1) for char in line]
print("".join(encrypted_line))
