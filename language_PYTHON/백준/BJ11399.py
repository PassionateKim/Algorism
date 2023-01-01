# ATM
import sys
si = sys.stdin.readline

answer = 0
N = int(si())
dp = list(map(int, si().split()))

dp.sort()
for i in range(1, len(dp)):
    dp[i] = dp[i] + dp[i-1]

print(sum(dp))