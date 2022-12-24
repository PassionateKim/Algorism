# 쉽게 푸는 문제
import sys
si = sys.stdin.readline

# 1. dp 로 일단 피보나치 구하기
dp =  [0] * 46
for i in range(1, len(dp)):
    dp[i] = dp[i-1] + i

A, B = map(int, si().split())

print(dp)

# 2. for 문 돌리면서 위치 체크
for_A = 222222 # 임의의 값
for_B = 333333 # 임의의 값


# A 찾기
for i in range(len(dp)-1):
    if (dp[i] < A <= dp[i+1]):
        for_A = i + 1
        break

# B 찾기
for i in range(len(dp)-1):
    if (dp[i] < B <= dp[i+1]):
        for_B = i + 1
        break

diff_A = dp[for_A] - A
diff_B = dp[for_B] - B

# B_total 구하기
B_total = 0
for i in range(1, for_B + 1):
    B_total += i*i

B_total = B_total - (for_B * diff_B)

# A_total 구하기
A_total = 0

for i in range(1, for_A + 1):
    A_total += i*i

A_total = A_total - (for_A * diff_A)

print(B_total - A_total + for_A)