from Crypto.Util.number import long_to_bytes

string = '''MyFirst CTF!!!! MyFirst MyFirst CTF!!!! CTF!!!! MyFirst CTF!!!! MyFirst CTF!!!! CTF!!!! CTF!!!! CTF!!!! MyFirst MyFirst CTF!!!! MyFirst CTF!!!! MyFirst MyFirst MyFirst CTF!!!! CTF!!!! MyFirst MyFirst CTF!!!! CTF!!!! MyFirst CTF!!!! MyFirst MyFirst CTF!!!! MyFirst CTF!!!! CTF!!!! CTF!!!! MyFirst MyFirst CTF!!!! MyFirst MyFirst CTF!!!! CTF!!!! CTF!!!! MyFirst MyFirst CTF!!!! CTF!!!! MyFirst CTF!!!! CTF!!!! CTF!!!! MyFirst CTF!!!! MyFirst MyFirst MyFirst CTF!!!! MyFirst MyFirst MyFirst MyFirst CTF!!!! CTF!!!! MyFirst CTF!!!! MyFirst CTF!!!! MyFirst CTF!!!! MyFirst MyFirst MyFirst CTF!!!! MyFirst MyFirst MyFirst CTF!!!! CTF!!!! MyFirst MyFirst CTF!!!! CTF!!!! CTF!!!! CTF!!!! MyFirst CTF!!!! CTF!!!! MyFirst CTF!!!! CTF!!!! MyFirst MyFirst MyFirst CTF!!!! MyFirst MyFirst MyFirst CTF!!!! CTF!!!! MyFirst CTF!!!! MyFirst MyFirst MyFirst CTF!!!! CTF!!!! MyFirst MyFirst MyFirst CTF!!!! CTF!!!! MyFirst MyFirst CTF!!!! CTF!!!! MyFirst MyFirst MyFirst MyFirst MyFirst CTF!!!! MyFirst MyFirst CTF!!!! CTF!!!! CTF!!!! MyFirst MyFirst CTF!!!! MyFirst CTF!!!! CTF!!!! CTF!!!! CTF!!!! CTF!!!! MyFirst CTF!!!! CTF!!!! MyFirst CTF!!!! MyFirst MyFirst CTF!!!! MyFirst MyFirst CTF!!!! CTF!!!! MyFirst CTF!!!! MyFirst CTF!!!! MyFirst CTF!!!! MyFirst CTF!!!! CTF!!!! CTF!!!! CTF!!!! CTF!!!! MyFirst CTF!!!! CTF!!!! MyFirst MyFirst MyFirst CTF!!!! MyFirst MyFirst CTF!!!! MyFirst MyFirst CTF!!!! CTF!!!! CTF!!!! CTF!!!! MyFirst CTF!!!! CTF!!!! CTF!!!! MyFirst MyFirst CTF!!!! MyFirst MyFirst MyFirst CTF!!!! CTF!!!! MyFirst MyFirst CTF!!!! CTF!!!! MyFirst CTF!!!! CTF!!!! MyFirst MyFirst CTF!!!! MyFirst MyFirst MyFirst MyFirst CTF!!!! MyFirst MyFirst CTF!!!! CTF!!!! MyFirst MyFirst CTF!!!! MyFirst MyFirst MyFirst CTF!!!! MyFirst CTF!!!! MyFirst CTF!!!! CTF!!!! CTF!!!! CTF!!!! MyFirst CTF!!!! MyFirst MyFirst CTF!!!! CTF!!!! CTF!!!! CTF!!!! CTF!!!! MyFirst CTF!!!!'''
binary = ''
for i in string.split():
    if 'M' in i:
        binary += '0'
    else:
        binary += '1'

flag = long_to_bytes(int(binary, 2)).decode('utf-8')
print(flag)

"""
flag = ''
for i in range(0, len(binary), 8):
    flag += chr(int(binary[i:i+8], 2))

print(flag)
"""
