# 연속합
# 복습횟수:1, 00:45:00, 복습필요3
# dp로 풀어보자

import sys
si = sys.stdin.readline 
N = int(si())
arr = list(map(int, si().split()))


for i in range(1, N):
    arr[i] = max(arr[i], arr[i-1] + arr[i])

print(max(arr))