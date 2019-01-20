題目給了一個檔案：`classic_rop`

用gdb實際跑過之後，程式邏輯大概長這樣：
```c=
#include <stdio.h>

int main(){
    char buffer[?];
    puts("ROP ROP ROP 💩");
    gets(buffer);
    return 0;
}
```

基本的rop題目，使用工具ROPgadget來取得gadgets，設計讓程式return to shell。

`rop.py`中提供兩種方式來讀取`/bin/sh`的字串：
1. 自己寫一個read，使用rax=0的syscall
2. 使用main裡面的gets，可以讓payload少一點(不過在這題沒差)
