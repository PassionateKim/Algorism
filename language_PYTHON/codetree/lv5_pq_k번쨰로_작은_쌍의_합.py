# 복습 횟수:1, 01:30:00, 복습필요:***
import heapq
import sys
si = sys.stdin.readline 

n, m, k = map(int, si().split())

arr1 = list(map(int, si().split()))
arr2 = list(map(int, si().split()))

pq = []
arr1.sort()
arr2.sort()

for i in range(len(arr1)):
    pq.append([arr1[i] + arr2[0], i, 0])

for i in range(k-1):
    sumi, index1, index2 = heapq.heappop(pq)

    index2 += 1
    if index2 < m:
        heapq.heappush(pq, [arr1[index1] + arr2[index2], index1, index2])


sumi, index1, index2 = heapq.heappop(pq)
print(sumi)