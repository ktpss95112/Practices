題目敘述中給了這長串：
`MyFirst CTF!!!! MyFirst MyFirst CTF!!!! CTF!!!! MyFirst CTF!!!! MyFirst CTF!!!! CTF!!!! CTF!!!! CTF!!!! MyFirst MyFirst CTF!!!! MyFirst CTF!!!! MyFirst MyFirst MyFirst CTF!!!! CTF!!!! MyFirst MyFirst CTF!!!! CTF!!!! MyFirst CTF!!!! MyFirst MyFirst CTF!!!! MyFirst CTF!!!! CTF!!!! CTF!!!! MyFirst MyFirst CTF!!!! MyFirst MyFirst CTF!!!! CTF!!!! CTF!!!! MyFirst MyFirst CTF!!!! CTF!!!! MyFirst CTF!!!! CTF!!!! CTF!!!! MyFirst CTF!!!! MyFirst MyFirst MyFirst CTF!!!! MyFirst MyFirst MyFirst MyFirst CTF!!!! CTF!!!! MyFirst CTF!!!! MyFirst CTF!!!! MyFirst CTF!!!! MyFirst MyFirst MyFirst CTF!!!! MyFirst MyFirst MyFirst CTF!!!! CTF!!!! MyFirst MyFirst CTF!!!! CTF!!!! CTF!!!! CTF!!!! MyFirst CTF!!!! CTF!!!! MyFirst CTF!!!! CTF!!!! MyFirst MyFirst MyFirst CTF!!!! MyFirst MyFirst MyFirst CTF!!!! CTF!!!! MyFirst CTF!!!! MyFirst MyFirst MyFirst CTF!!!! CTF!!!! MyFirst MyFirst MyFirst CTF!!!! CTF!!!! MyFirst MyFirst CTF!!!! CTF!!!! MyFirst MyFirst MyFirst MyFirst MyFirst CTF!!!! MyFirst MyFirst CTF!!!! CTF!!!! CTF!!!! MyFirst MyFirst CTF!!!! MyFirst CTF!!!! CTF!!!! CTF!!!! CTF!!!! CTF!!!! MyFirst CTF!!!! CTF!!!! MyFirst CTF!!!! MyFirst MyFirst CTF!!!! MyFirst MyFirst CTF!!!! CTF!!!! MyFirst CTF!!!! MyFirst CTF!!!! MyFirst CTF!!!! MyFirst CTF!!!! CTF!!!! CTF!!!! CTF!!!! CTF!!!! MyFirst CTF!!!! CTF!!!! MyFirst MyFirst MyFirst CTF!!!! MyFirst MyFirst CTF!!!! MyFirst MyFirst CTF!!!! CTF!!!! CTF!!!! CTF!!!! MyFirst CTF!!!! CTF!!!! CTF!!!! MyFirst MyFirst CTF!!!! MyFirst MyFirst MyFirst CTF!!!! CTF!!!! MyFirst MyFirst CTF!!!! CTF!!!! MyFirst CTF!!!! CTF!!!! MyFirst MyFirst CTF!!!! MyFirst MyFirst MyFirst MyFirst CTF!!!! MyFirst MyFirst CTF!!!! CTF!!!! MyFirst MyFirst CTF!!!! MyFirst MyFirst MyFirst CTF!!!! MyFirst CTF!!!! MyFirst CTF!!!! CTF!!!! CTF!!!! CTF!!!! MyFirst CTF!!!! MyFirst MyFirst CTF!!!! CTF!!!! CTF!!!! CTF!!!! CTF!!!! MyFirst CTF!!!!`

通靈：轉換成2進位
通靈：`MyFirst`換成0，`CTF!!!!`換成1。

接下來提供兩種作法：
1. 把二進位每8個換成ascii字
2. 把二進位換成整數再`long_to_bytes()`

得到flag為`MyFirstCTF{b4c0N_i5_bOr3d&Ez}`。
