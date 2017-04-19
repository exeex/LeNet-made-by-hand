import random

# HW0002：
# ◎ 基本題
# 1. 產生五個亂數，並將其輸出。

x1 = []
for idx in range(5):
    x1.append(random.random())
print(x1)

# 2. 產生N個介於-1與1之間的亂數，計算其平均值與標準差並輸出，每個亂數的值則不用輸出。N=10^1, 10^2, 10^3, 10^4, 10^5。

x2 = []
for idx in range(5):
    x2.append(random.uniform(-1, 1))
print(x2)

# ◎ 進階題
# 3. 做基本題2時，一併輸出產生每N個亂數前後的系統時間，並計算所需的時間。


def func():
    x2 = []
    for idx in range(1000000):
        x2.append(random.uniform(-1, 1))

import time
start_time = time.time()
func()
print("--- %s seconds ---" % (round(time.time() - start_time, 2)))



# 4. 自己寫一個亂數產生器。