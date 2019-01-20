from pwn import *

r = remote('mf-pwn.ais3.org', 6666)
context.arch = 'amd64'

# stage 1
r.recvuntil('Stage 1:\n')
for _ in range(50):
    line = r.recvline().decode('utf-8')
    line = line[line.find('"')+1:]
    line = line[:line.find('"')]
    print(line)
    r.sendline(b64e(asm(line)))

# stage 2
r.recvuntil('Stage 2:\n')
for i in range(500):
    line = r.recvline().decode('utf-8')
    line = line[line.find(' ')+1:]
    line = line[:line.find('=')-1]
    print(line)
    r.sendline(str(eval(line)))



r.interactive()
