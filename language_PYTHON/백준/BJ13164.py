# 행복 유치원
# 복습 횟수:0, 01:00:00
import sys
si = sys.stdin.readline
N, K = map(int, si().split())
people_list = list(map(int, si().split()))

diff_list = []

for i in range(1, N):
    diff = people_list[i] - people_list[i-1]
    diff_list.append(diff)

diff_list.sort()
print(sum(diff_list[:N-K]))