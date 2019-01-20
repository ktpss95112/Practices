題目給了一個執行檔：`luckyboys`

這題還滿好玩的，實際用gdb跑過，原始碼的邏輯大概長這樣：
```c=
#include <stdlib.h>
#include <time.h>
#include <stdlib.h>

int main(){
    puts("Welcome! Are you Wackyboys, Luckyboys or Hacker😎?");
    puts("Guess right 100 random number to prove yourself!");
    srand(time(0));
    for(int i=0; i<100; i++){
        printf("guess %d", i);
        int n;
        scanf("%d", &n);
        if(n != rand()){
            puts("Go away Wackyboys!");
            exit(0);
        }
    }
    system("sh");
    
    return 0;
}
```

查了time()的用法，發現回傳的是從1970年1月1日00:00到當前的秒數，所以srand()的種子就是這個。

搜尋了python的random函式庫，發現python使用的rand跟C使用的rand是不同的，所以如果要生成和題目伺服器一樣的random number，就得要用C的rand來生成。

花了一些時間搜尋如何讓python來呼叫用C寫好的函數，找到這篇文章：
https://www.jianshu.com/p/edb8698d1374

參考文章，寫出`c_dll.c`，然後用`gcc c_dll.c -shared -o c_dll.so`編譯成`c_dll.so`，這樣就可以在python裡面用`my_func = cdll.LoadLibrary("./c_dll.so")`來使用C的rand()了。

最後，用pwntools寫連線的部份，得到flag。
