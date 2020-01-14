把zip解開來之後，發現有一堆資料夾，看起來每個資料夾都對應到一個flag的byte。
![](https://i.imgur.com/hsHtevK.png)

用tree指令簡單瞄一下，果然長得很像tree。
![](https://i.imgur.com/svneBXW.png)

在一點點靈力的加持下，通出來了！

每個資料夾都會是`n_o`的形式，其中`o`代表的是要用什麼運算符號來操作當前資料夾下的兩個數字，而`n`代表的則是這樣運算完之後，他自己會代表什麼數字。

或者換另外一種說法，每個資料夾代表的就是一個帶有加法或乘法的節點，每個`0_number`或`1_number`代表的是一個包含數字的節點。建立起來的樹就會是一顆運算樹，舉例如下圖：
![](https://i.imgur.com/IJk5dEe.png)

所以就寫一個python3 script來DFS，把每個資料夾的結果都算出來，就得到flag了~

flag: `BAMBOOFOX{Dir_3xpres5i0n_tre3e33eeee}`
