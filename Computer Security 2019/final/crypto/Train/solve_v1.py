from pwn import *
from Crypto.Util.number import long_to_bytes, bytes_to_long

# debug = True
debug = False

if not debug:
    r = remote('eductf.zoolab.org', 20002)
else:
    r = process('./server.py')


r.sendlineafter('> ', '1')
n = int(r.recvline()[4:-1].decode('ascii'))
e = int(r.recvline()[4:-1].decode('ascii'))
ticket = bytearray.fromhex(r.recvline()[9:-1].decode('ascii'))
iv, c1, c2, c3, c4 = [ ticket[i:i+128] for i in range(0, 640, 128) ]
c5 = long_to_bytes(pow(bytes_to_long(c4)+bytes_to_long(b'|'), e, n)) # c5 will be decrypted to b'|'

plain = b'0|secret:FLAG{'
plain2 = b'\x00'*10
date = b':2019/1/11'
pool = ''.join([chr(i) for i in range(32, 127)] + ['\x00']).encode()

# leak c3
for target in range(-2, 0):
    new_c2 = bytes_to_long(c2)
    for i, j in zip(range(target-10, target), range(10)):
        new_c2 += (plain[16+i] - date[j]) << (8*(abs(i)-1))
    
    for p in pool:
        final_c2 = new_c2 + (p - (ord('|')) << (8*(abs(target)-1)))

        r.sendlineafter('> ', '2')
        r.sendlineafter('ticket = ', (long_to_bytes(final_c2) + c3).hex())
        if debug: r.recvline()
        result = r.recvline()
        if b'Wrong' in result:
            plain += bytes([p])


# leak c4
for target in range(-16, 0):
# for target in range(-11, -9):
    new_c3 = bytes_to_long(c3)
    # final_c3 = new_c3 + ((ord('i') - date[j]) << (8*(abs(i)-1)))
    for i, j in zip(range(target-10, target), range(10)):
        # print(10+16+i, chr(plain2[10+16+i]), j, date[j], target)
        new_c3 += (plain2[10+16+i] - date[j]) << (8*(abs(i)-1))
    
    # r.sendlineafter('> ', '2')
    # r.sendlineafter('ticket = ', (long_to_bytes(new_c3)+c4+c5).hex())

    for p in pool:
        final_c3 = new_c3 + (p - (ord('|')) << (8*(abs(target)-1)))

        r.sendlineafter('> ', '2')
        r.sendlineafter('ticket = ', (long_to_bytes(final_c3)+c4+c5).hex())
        if debug: print(r.recvline().decode()[:-1])
        result = r.recvline()
        if b'Pass' in result:
            plain2 += bytes([p])

print(plain, plain2)
# FLAG{cBCNEVERGetSoLD}

r.interactive()
