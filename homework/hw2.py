import random

# HW0002：

# 1. 產生五個亂數，並將其輸出。

x1 = []                                 # 宣告 list
for idx in range(5):
    x1.append(random.random())          # 產生隨機變數，附加到list後面
print(x1)

# 2. 產生N個介於-1與1之間的亂數，計算其平均值與標準差並輸出，每個亂數的值則不用輸出。N=10^1, 10^2, 10^3, 10^4, 10^5。

x2 = []
for idx in range(5):
    x2.append(random.uniform(-1, 1))     # 產生uniform分布的隨機變數，附加到list後面
print(x2)


# 3. 做基本題2時，一併輸出產生每N個亂數前後的系統時間，並計算所需的時間。

def func():                               #宣告函數
    x2 = []
    for idx in range(1000000):
        x2.append(random.uniform(-1, 1))

import time                                #引入time
start_time = time.time()
func()                                     #執行函數
print("--- %s seconds ---" % (time.time() - start_time))


# 4. 自己寫一個亂數產生器。
