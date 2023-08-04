# 행복 유치원
# 복습 횟수:1, 01:00:00, 복습필요3
import sys
si = sys.stdin.readline
N, K = map(int, si().split())
arr = list(map(int, si().split()))

diff_list = []

for i in range(1, N):
    diff = arr[i] - arr[i-1]
    diff_list.append(diff)

diff_list.sort()
print(sum(diff_list[:N-K]))