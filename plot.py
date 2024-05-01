import time
import MCC
import random
import matplotlib.pyplot as plt
import math

n = 500

cList = [[1, 3, 4, 5],[1, 2, 3, 5, 8, 13, 21, 34],[1, 2, 3, 5, 7, 10, 12, 13, 15, 17, 18, 20],[1, 2, 3, 5, 6, 8, 9, 10, 12, 13, 15, 16, 18, 19, 20, 25]]
for p in cList:
    running_times_MCC_BF = []
    running_times_MCC_memoize = []
    running_times_MCC_bottom_up = []
    running_times_MCC_greedy = []
    for i in range(1, n+1):
        if i < 20:
            start_time = time.time()
            MCC.min_coins_rec_BF(p, i)
            end_time = time.time()
            running_times_MCC_BF.append(end_time - start_time)

        start_time = time.time()
        MCC.min_coins_TD(p, i)
        end_time = time.time()
        running_times_MCC_memoize.append(end_time - start_time)

        start_time = time.time()
        MCC.min_coins_DP(p, i)
        end_time = time.time()
        running_times_MCC_bottom_up.append(end_time - start_time)

        start_time = time.time()
        MCC.min_coins_greedy(p, i)
        end_time = time.time()
        running_times_MCC_greedy.append(end_time - start_time)
        print(i)

    plt.plot(range(1, 20), running_times_MCC_BF, label='Minimum Coin Change Brute Force')
    plt.plot(range(1, n+1), running_times_MCC_memoize, label='Minimum Coin Change Top Down')
    plt.plot(range(1, n+1), running_times_MCC_bottom_up, label='Minimum Coin Change Bottom Up')
    plt.plot(range(1, n+1), running_times_MCC_greedy, label='Minimum Coin Change Greedy')
    plt.xlabel('n (Amount)')
    plt.ylabel('Running Time (seconds)')
    plt.title('Running Time of Minimum Coin Change Algorithms')
    plt.legend()
    plt.show()
