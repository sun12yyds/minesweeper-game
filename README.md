# minesweeper-game
这次我们基于 pygame 来做一个扫雷，上次有园友问我代码的 python 版本，我说明一下，我所有的代码都是基于 python 3.6 的。
先看截图，仿照 XP 上的扫雷做的，感觉 XP 上的样式比 win7 上的好看多了。
原谅我手残，扫雷基本就没赢过，测试的时候我是偷偷的把雷的数量从99改到50才赢了。。。
下面将一下我的实现逻辑。


# 首先，如何表示雷和非雷，一开始想的是，建立一个二维数组表示整个区域，0表示非地雷，1表示地雷。后来一想不对，还有标记为地雷，标记为问号，还有表示周边雷数的数字，好多状态，干脆就做个类吧
# 代码1见1.py
