murmur: 這題真的超讚的，很有趣又學到不少東西，第一次這麼仔細看C跟python的接口原來長這樣。

丟線上工具解pyc，解出如下的python code：
```python=
# Python bytecode 3.7 (3394)
# Embedded file name: H0W.py
# Size of source mod 2**32: 387 bytes
# Decompiled by https://python-decompiler.com
import sys, struct
from terrynini import *
if len(sys.argv) != 2:
    print('Usage: python3 H0W.py filename')
    exit(0)
nini3()
f = open(sys.argv[1], 'rb').read()
if len(f) % 4 != 0:
    f += (4 - len(f) % 4) * '\x00'
nini1()
nini4()
for i in range(0, len(f), 4):
    nini6(nini5(struct.unpack('<i', f[i:i + 4])[0]))

for i in list(map(ord, nini2())):
    nini6(i)

print('Complete')
```

發現有`nini1`~`nini6`這6個怪怪的函數，估計應該是在`terrynini.so`裡面。
用ghidra來decompile `terrynini.so`，發現有6個沒有名稱的函數，又剛剛好這6個函數裡面都有呼叫一個C library的函數，還不重複，所以可以得到每個nini函數和一個C library函數的對應關係。
```
$ gdb python3
gdb-peda$ # set breakpoint at time, gmtime, fopen, srand, rand, fwrite
gdb-peda$ r H0W.pyc input.txt
gdb-peda$ # use `continue` to observe the sequence of the functions
```
![](https://i.imgur.com/tA0058H.png)
得到了這6個C library函數的先後出現順序，再比對一下decompyle出來的python code，就可以得到每個nini函數是對應到terrynini.so裡面的哪個函數了，結果如下圖：
![](https://i.imgur.com/bKQ1rtX.png)

所以整個H0W.pyc的行為，就是srand(time)之後，把argv[1]的檔案每4個byte一組，每組根據當前的rand()來決定要使用「ichinokata」（日文：方法一）、「ninokata」（日文：方法二）、「sannokata」（日文：方法三）、「yonnokata」（日文：方法四）的哪個方法來加密。最後，把當前的年、月、星期、時、分、秒給寫進輸出檔案的最後面。**特別注意，寫進輸出檔案裡面的是星期而不是日期，還有月份跟星期是從0開始算的。**

因此，我們可以透過output.txt的檔案結尾來猜測srand()當下的時間（總共有4種可能，因為給的是星期而不是日期），然後把output.txt用那四種加密方法的逆操作來還原出原本的檔案。

解出4個檔案之後，`strings`找一下發現都沒有flag的字串在裡面，還心想是不是解爛了，想了10分鐘之後通靈到有可能檔案不是純文字，`file`看一下還真的有圖片檔，果然就有flag了~~~
![](https://i.imgur.com/J1FO66r.jpg)

人生第一次在CTF首殺某個感覺有點複雜的題目❤

flag: `FLAG{H3Y_U_C4NT_CHiLL_H3R3}`
