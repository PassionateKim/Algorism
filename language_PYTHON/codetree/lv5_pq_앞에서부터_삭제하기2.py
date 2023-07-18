# 복습 횟수:0, 01:00:00, 복습필요:***
import heapq
import sys

si = sys.stdin.readline
N = int(si())
arr = list(map(int, si().split()))

sum_val = 0
max_avg = 0
pq = []

heapq.heappush(pq, arr[N-1])
sum_val += arr[N-1]

for i in range(N-2, 0, -1):
    heapq.heappush(pq, arr[i])
    sum_val += arr[i]
    min_num = pq[0]

    avg = (sum_val - min_num) / (N-i-1)

    max_avg = max(max_avg, avg)


print(f"{max_avg:.2f}")