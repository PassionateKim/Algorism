# 복습 횟수:0, 00:30:00, 복습필요X
import sys
import heapq
si = sys.stdin.readline

N = int(si())

arr = list(map(int, si().split()))
pq = []
for i in range(len(arr)):
    heapq.heappush(pq, arr[i])
    if i <= 1:
        print(-1)
    else:
        tmp = 1
        tmp_list = []
        for i in range(3):
            val = heapq.heappop(pq)
            tmp_list.append(val)
            tmp = val * tmp
            
        for i in range(3):
            heapq.heappush(pq, tmp_list[i])
        
        print(tmp)