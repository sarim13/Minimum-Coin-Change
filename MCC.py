#minimum coin change recursive brute force
def min_coins_rec_BF(coins, amount):
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')
    res = float('inf')
    for i in range(len(coins)):
        res = min(res, 1 + min_coins_rec_BF(coins, amount - coins[i]))
    return res

# minimum coin change dp top down
def min_coins_TD(coins, amount):
    memo = [-1 for i in range(amount+1)]
    memo[0] = 0
    def min_coins_rec(coins, amount):
        if amount == 0:
            return 0
        if amount < 0:
            return float('inf')
        if memo[amount] != -1:
            return memo[amount]
        res = float('inf')
        for i in range(len(coins)):
            res = min(res, 1 + min_coins_rec(coins, amount - coins[i]))
        memo[amount] = res
        return res
    return min_coins_rec(coins, amount)

# minimum coin change dp Bottom up
def min_coins_DP(coins, amount):
    dp = [float('inf') for i in range(amount+1)]
    dp[0] = 0
    for i in range(1, amount+1):
        for j in range(len(coins)):
            if coins[j] <= i:
                dp[i] = min(dp[i], 1 + dp[i-coins[j]])
    return dp[amount]

# minimum coin change greedy
def min_coins_greedy(coins, amount):
    res = 0
    n = len(coins) - 1
    for i in range(len(coins)):
        if coins[n-i] <= amount:
            res += amount // coins[n-i]
            amount = amount % coins[n-i]
    return res
# coins = [1, 3,4,5]
# amount = 7
# print("Minimum number of coins required:", min_coins_greedy(coins, amount))