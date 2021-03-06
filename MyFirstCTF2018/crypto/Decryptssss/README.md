題目給了兩個檔案：`cipher`, `privatekey`
可以得到`c, e, d, n`。
根據RSA的解密方式，得到明文`m = pow(c, d, n)`

```python=
from Crypto.Util.number import inverse, long_to_bytes
from gmpy2 import iroot

c = 33393702979801369923488948870130363400493384070897866654748370685847844083361250729334318529264776694785260030713770003216573777946579875191976906800464341055547257181517606613851693655835213272865834305066913054186191119089523811131253574621301535189609804012114542465980061824020961479665152439178410850207
e,d,n = (
    65537,
    33933195743849759511610934102459747851157130150934022466513791192050687598012102529874246392623075675664832239161540677393317045839771787568917291390721029574162464998685268963327939869293391550943034554739122109496726471311817971658189313863651455662010199147043168242706724283190467940093624410881841657745,
    94766261109842829893571644789402330716379803072474667847953054644966374615882693292724612683058699900117020090251412254413679602556829745681345401025852669339169332041491481265741813298044536985105477842619843977775071935702331200460439921784845083692855295548304192842183376356386505584170549260088202046731,
)

m = pow(c, d, n)

```

得到
```
>>> m
b"Hello~ my first classical: EqXajklULX{XImpjPMkDhhhh} (Ljq pgj lzw kljafy '4444444444444' lg ywl jwsd xdsy)"
```

通靈：看到classical，腦袋出現凱薩加密
```python= 
def ceasar(source, shift=None):
    '''
    source : bytes
    shift  : number (default None)
    If shift is None, ceasar will return all possible results (a list of 26 bytes).
    '''
    lower = b'abcdefghijklmnopqrstuvwxyz'
    upper = b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    def ceasar_char(char, shift):
        if char in lower: table = lower
        else:             table = upper
        return table[ ((char - table[0]) + shift) % 26 ]

    if shift != None:
        return bytes([ ceasar_char(c, shift) if (c in lower+upper) else c for c in source ])
    return [ bytes([ ceasar_char(c, i) if (c in lower+upper) else c for c in source ]) for i in range(26) ]
```

找到`MyFirstCTF{FQuxrXUsLpppp} (Try xor the string '4444444444444' to get real flag)`

使用xor
```python=
>>> from pwn import xor
>>> xor(reALFlaGxDDDD)
b'reALFlaGxDDDD'
```

所以得到flag為`MyFirstCTF{reALFlaGxDDDD}`。
 
