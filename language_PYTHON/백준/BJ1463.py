# 1로 만들기
import sys
si = sys.stdin.readline

dp = ['#', 0]
N = int(si())

for i in range(2, N+1):
    if i % 3 == 0 and i % 2 != 0:
        dp.append(min(dp[i//3], dp[i-1]) + 1)
    elif i % 2 == 0 and i %3 != 0:
        dp.append(min(dp[i//2], dp[i-1]) + 1)
    elif i % 2 == 0 and i % 3 == 0:
        dp.append(min(dp[i//3], dp[i//2], dp[i-1]) + 1)
    else:
        dp.append(dp[i-1] + 1)

print(dp)






