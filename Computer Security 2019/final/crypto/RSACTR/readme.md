這題的是RSA-CBC，CBC mode很有可能會出現像padding oracle的攻擊，這題的漏洞利用方式跟padding oracle也有異曲同工之妙。

觀察server.py與server回傳的東西，可以得到plain text有4個block，每個block有16 bytes；cipher text有5個block，每個block有128 bytes。
![](https://i.imgur.com/IizQVVU.png)

注意到在CBC mode下，如果我們只傳送了$c_1$和$c_2$，server還是可以解密，而且只會解出$m_2$。

我們要利用的是server.py裡面的use函數來作為一個oracle，洩漏出有關明文的資訊。可以利用的點在於第70行，如果plain裡面的`|`(後文用pipe來稱呼)只有一個的話，那麼這裡就會發生error，跳到except的部份去執行。
![](https://i.imgur.com/4YAOPfw.png)

例如我們想要洩漏$m_2$的最後一個byte，那麼我們就可以窮舉$c_2[-1]$（$c_1$的最後一個byte），然後只送$c_1+c_2$過去。大部分的情況，解出來的$m_2'[-1]$不會是pipe，所以整個$m_2'$只有一個pipe，server會輸出`Oops`；只有在$m_2'[-1]$是pipe的時候，第70行不會出錯，server會回傳`Wrong`，這個時候我們就可以推算出$m_2[-1]=124+c_2'[-1]-c_2[-1]$，其中124是pipe的ascii值。

利用同樣的原理，我們也可以leak出$c_3$的每一個byte，特別要注意的是$m_3$裡面沒有任何的pipe，所以我們需要自己構造一塊$c_4=RSA(c_3+pipe)$，這樣子解出來的plain才可以利用上面的手法來leak，否則pipe的數量會不夠，server永遠只會輸出`Oops`。

`solve_v2.py`執行起來有機率會出錯，雖然我也還沒搞清楚到底是為什麼。總之如果出錯的話就重跑一次就會好了。

flag: `FLAG{cBCNEVERGetSoLD}`
