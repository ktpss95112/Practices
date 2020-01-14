這題的前半段是@soyccan解的，他發現了`DuRaRaRa.exe`的裡面包了另外一個exe檔，然後他把那個抓出來變成`ora-new.exe`，我只有逆向`ora-new.exe`而已。

`ora-new.exe`執行起來，會有一個視窗要你輸入flag，然後他會告訴你你輸入的是不是flag。reverse完之後發現他的行為就是把flag(總長16)拆成4段，每段4個byte，然後去算rolling hash，還要檢查每段的第0和第1個字元是不是指定的字元，通過這些檢查的就是flag。

因為一段的所有可能有大約 100^4 = 1e8 種可能，所以這次用C來寫解題腳本而不是python。

爆搜出來之後，還是有超過一種的可能，這時就用人眼來辨識了。

flag: `FLAG{D-Day:2020/01/14}`
