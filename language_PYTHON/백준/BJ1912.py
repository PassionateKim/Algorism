# 연속합
# 00:45:00
import sys
si = sys.stdin.readline

N = int(si())
suyeol = list(map(int, si().split()))
dp = [0] * (N)

dp[0] = suyeol[0]
# 로직
for i in range(1, N):
    dp[i] = max(dp[i-1] + suyeol[i], suyeol[i])
 
print(max(dp))