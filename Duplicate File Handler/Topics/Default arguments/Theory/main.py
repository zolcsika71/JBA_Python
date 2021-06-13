import sys

alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"

args = sys.argv

filename = args[1]
print(f'{filename}')
opened_file = open(filename)
encoded_text = opened_file.read()  # read the file into a string


def decode_Caesar_cipher(s, n_):
    s = s.strip()
    text = ''
    for c in s:
        text += alpha[(alpha.index(c) + n_) % len(alpha)]
    print(f'{n_} Decoded text: "' + text + '"')


for n in range(1, len(alpha)):
    decode_Caesar_cipher(encoded_text, n)

opened_file.close()  # always close the files you've opened
