Google搜尋了一下，找到了這篇：http://blog.terrynini.tw/en/2018-0CTF-Quals-g0g0g0/ ，作者還是出題者自己呢！看起來照著做就會過了的感覺，頓時安心了不少。

照著這篇blog所說的，先把log裡面所有看起來是library function的部份刪掉，log檔瞬間從快19000行變成只剩下490行。接著發現有很多重複的部份，猜測可能是有迴圈的結構，所以稍微整理一下，剩下大約130行左右的pseudo-code。

pseudo-code裡面驗證flag的部份大概長這樣：
```
flag[0] + flag[1] = 185;
flag[1] + flag[2] = 212;
...
flag[19] + flag[0] = 177;
```
發現只有19條線性獨立的方程式，卻有20個未知數，所以就暴力列舉囉。
![](https://i.imgur.com/6sqSU56.png)
肉眼確認答案的時候差點看不出來，這個flag也太鬧XD

flag: `FLAG{PikAPikApikaPikap1Ka}`
