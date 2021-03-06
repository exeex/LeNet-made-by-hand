import random
import statistics
# HW0002：
# 1. 產生五個亂數，並將其輸出。

x1 = [random.random() for idx in range(5)]

print(x1)

# 2. 產生N個介於-1與1之間的亂數，計算其平均值與標準差並輸出，每個亂數的值則不用輸出。N=10^1, 10^2, 10^3, 10^4, 10^5。

for N in range(5):
    x2 = [random.uniform(-1,1) for idx in range(10**(N+1))]
    y1=statistics.stdev(x2)
    y2=statistics.mean(x2)


# 3. 做基本題2時，一併輸出產生每N個亂數前後的系統時間，並計算所需的時間。



def func(N):                               #宣告函數
    return [random.uniform(-1,1) for idx in range(10**N)]

import time                                 #引入time

for N in range(5):
    start_time = time.time()
    x2=func(N+1)
    y1=statistics.stdev(x2)
    y2=statistics.mean(x2)
    print("--- %s seconds ---" % round(time.time() - start_time,5))

                                            #執行函數



# 4. 自己寫一個亂數產生器。
