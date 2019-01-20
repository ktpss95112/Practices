題目給了一個檔案：`baby_shellcode`

使用gdb跑過之後，得到程式邏輯大概長這樣：
```c=
char name[?];

int main(){
    puts("What's your name?");
    gets(name);
    printf("Hello %s! \nSay something", name);
    char something[?];
    gets(something);
    return 0;
}
```

在gdb-peda裡面使用`checksec`，看到保護機制：
* canary沒開，可以buffer overflow
* NX沒開，可以inject shellcode

所以第一個gets()可以在name裡面放shellcode，第二個gets用來buffer overflow，把return address蓋成name的位置來執行shellcode。
