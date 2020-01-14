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

plain = b'FLAG{'
pool = ''.join(['\x00'] + [chr(i) for i in range(32, 127)]).encode()

# leak c3
for target in range(-2, 0):    
    for p in pool:
        new_c2 = bytes_to_long(c2) + (p - (ord('|')) << (8*(abs(target)-1)))

        r.sendlineafter('> ', '2')
        r.sendlineafter('ticket = ', (long_to_bytes(new_c2) + c3).hex())
        if debug: r.recvline()
        result = r.recvline()
        # print(result)
        if b'Oops' not in result:
            plain += bytes([p])
            print(plain)


# leak c4
for target in range(-16, 0):
    for p in pool:
        new_c3 = bytes_to_long(c3) + (p - (ord('|')) << (8*(abs(target)-1)))

        r.sendlineafter('> ', '2')
        r.sendlineafter('ticket = ', (long_to_bytes(new_c3) + c4 + c5).hex())
        if debug: print(r.recvline().decode()[:-1])
        result = r.recvline()
        # print(result)
        if b'Oops' not in result:
            plain += bytes([p])
            print(plain)

print(plain.replace(b'\x00', b''))
# FLAG{cBCNEVERGetSoLD}

# r.interactive()
r.close()
