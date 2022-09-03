# 2022-05-17
# 2022-09-03
# 정수 삼각형
import sys
si = sys.stdin.readline
N = int(si())
dp = [0] * N
triangle = []
for i in range(N):
    triangle.append(list(map(int, si().split())))

dp[0] = triangle[0][0]
for i in range(1, len(triangle)):
    tmp = triangle[i]
    dp_ex = dp[:] # 직전 dp 저장
    #[3,8]
    for j in range(len(tmp)):
        if j == 0: # 왼쪽 끝인 경우
            dp[j] = dp_ex[j] + tmp[j]
        elif j == len(tmp)-1: # 오른쪽 끝인 경우
            dp[j] = dp_ex[j-1] + tmp[j]
        else: # 중간인 경우
            dp[j] = max(dp_ex[j-1], dp_ex[j]) + tmp[j]
print(max(dp))