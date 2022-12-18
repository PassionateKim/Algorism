import sys
si = sys.stdin.readline


N = int(si())
dp = [0, 1] + [0] * N

for i in range(2, N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N])