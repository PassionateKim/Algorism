# 복습 횟수:0, 01:30:00, 복습필요:***
import heapq
import sys
si = sys.stdin.readline 

n, m, k = map(int, si().split())

arr1 = list(map(int, si().split()))
arr2 = list(map(int, si().split()))

pq = []

arr1 = sorted(arr1)
arr2 = sorted(arr2)


for i in range(n):
    heapq.heappush(pq, (arr1[i] + arr2[0], i, 0))

for i in range(k-1):
    _, idx1, idx2 = heapq.heappop(pq)

    idx2 += 1
    if idx2 < m:
        heapq.heappush(pq, (arr1[idx1] + arr2[idx2], idx1, idx2))

pair_sum, _, _ = heapq.heappop(pq)

print(pair_sum)