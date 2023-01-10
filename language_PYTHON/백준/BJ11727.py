# 2x n 타일링 2
# 00:15:00
import sys
si = sys.stdin.readline
N = int(si())
dp = [0] * (N+1)

dp[1] = 1
if N > 1:
    dp[2] = 3

for i in range(3, N+1):
    dp[i] = dp[i-1] + 2 * dp[i-2]

print(dp[N] % 10007)