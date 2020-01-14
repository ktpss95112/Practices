murmur: 我覺得這題很難搞，沒想到最後居然只剩229分，感覺他應該有300~400分的難度R……

Google搜尋了「gameboy ctf」，發現 [這篇writeup](https://github.com/VoidHack/write-ups/tree/master/Square%20CTF%202017/reverse/gameboy) ，於是就載了 [BGB](http://bgb.bircd.org/) ，在windows裡面跑起來了。
遊戲跑起來之後很單純，就只有一個輸入文字的介面，輸入完之後選取最右下角的打勾，程式就會驗證我們輸入的東西是不是flag。

本來在bgb上面下斷點，跑起來之後他不理我，完全不知道要怎麼操作，網路上面也都查不到教學文，是要放棄這題了。後來又回來解是因為分數實在變太低，覺得應該沒有那麼難，所以才回來繼續解。

心路歷程是這樣的：
先打開bgb cheat searcher，這裡跟cheat engine的功能有點像，可以找到符合某個值的位址，也可以根據值的變化來搜尋。我猜測應該有兩個變數記錄我們的游標位址，一個x軸一個y軸，所以就移動游標之後更新搜尋的值，反正就搜到了，`C7B2`這裡存的是x座標。
然後對著`C7B2`點右鍵，按「set access breakpoint」，然後點一下遊戲視窗，再移動一下游標，發現assembly的介面停在某個指令，而且遊戲畫面的游標也沒有更新，然後我一行一行執行assembly，發現在某個指令執行完的瞬間，遊戲畫面上的游標更新了！然後我好像就抓到了bgb要怎麼使用了。
接著，發現某個感覺應該像是負責判斷我們按了什麼按鍵的區域，經過一些實驗，發現這5個jp對應到5種我們的按鍵訊號(上下左右和s)，如下圖所示：
![](https://i.imgur.com/u2rvbWw.png)

在select那邊下斷點之後，到遊戲裡面選取打勾，一步一步執行下去就會發現有某一串感覺像是在準備一大長串stack上的值，有可能是作為後續比對的用途，用ida pro來看流程圖，也在底下發現了一個迴圈比對的結構，所以在`0E61`的函數真的就是用來驗證我們的flag正不正確。
![](https://i.imgur.com/UV8tCmt.png)

經過了一點點的小實驗，發現了我們輸入的字的encoding會是像下圖那樣：
![](https://i.imgur.com/UgappgD.png)

所以把用來比對的那些資料轉換成文字，就可以得到flag了~~

flag: `FLAG{OHMYGODY0UAREGAM3B0Y}`

附上一張痛苦的過程截圖：
![](https://i.imgur.com/GcePRfw.png)
