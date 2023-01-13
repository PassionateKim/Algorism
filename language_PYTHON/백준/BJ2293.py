# 동전 1
# 복습횟수:1, 00:30:00
import sys
si = sys.stdin.readline
N, K = map(int, si().split())

coins = []
for i in range(N):
    coins.append(int(si()))
dp = [0] * (K+1)
dp[0] = 1
for coin in coins:
    for i in range(coin, K+1):
        dp[i] = dp[i] + dp[i - coin]

print(dp[K])