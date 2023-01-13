# 퇴사 2
# 02:00:00
import sys
si = sys.stdin.readline

N = int(si())

T = []
P = [0]
dp = [0] * (N+1)

for i in range(N):
    x, y = map(int, si().split())
    T.append(x)
    P.append(y)

# dp 
k = 0
for i in range(N):
    k = max(k, dp[i])
    if (i + T[i]) <= N: 
        dp[i + T[i]] = max(k + P[i], dp[i+ T[i]])

print(dp)