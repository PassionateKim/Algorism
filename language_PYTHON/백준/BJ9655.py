# 돌게임
import sys
si = sys.stdin.readline

N = int(si())
dp = [0] * (N+1)
dp[1] = 1
if N >=2:
    dp[2] = 2
if N>= 3:
    dp[3] = 1

for i in range(3, N+1):
    dp[i] = min(dp[i-1], dp[i-3]) + 1

if (dp[N] % 2):
    print("SK")
else:
    print("CY")