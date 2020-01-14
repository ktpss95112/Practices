# keyword: rsa oracle
# reference: https://crypto.stackexchange.com/questions/11053/rsa-least-significant-bit-oracle-attack

from pwn import *
from Crypto.Util.number import long_to_bytes

while True:
    e, c, n = 65537, -1, -1
    r = remote('34.82.101.212', 20001)

    r.sendlineafter('> ', '1')
    exec(r.recvline()[:-1].decode('ascii'))
    exec(r.recvline()[:-1].decode('ascii'))

    if n%3 == 2: break

    r.close()

bound = [0, n]

def query(x):
    r.sendlineafter('> ', '2')
    r.sendlineafter('c = ', str(x))
    return int(r.recvline().decode('ascii')[4:-1])

i = 1
while int(bound[0]) + 2 <= int(bound[1]):
    print('bound of n:', bound)
    print('diff:', bound[1]-bound[0])
    m = query( (c * pow(pow(3, i, n), e, n)) % n )
    bound = [ bound[0], (2*bound[0]+bound[1])//3, (bound[0]+2*bound[1])//3, bound[1]-1 ][m:m+2]
    bound[1] += 1

    i += 1

print(long_to_bytes(bound[0]))
# BAMBOOFOX{SimPlE0RACl3}
