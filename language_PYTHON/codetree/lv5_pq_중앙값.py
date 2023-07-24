# 2023-07-19
# 2023-07-24
# 복습 횟수:2, 01:00:00, 복습필요:***
import heapq
import sys
si = sys.stdin.readline 
T = int(si())

for _ in range(T):
    N = int(si())
    arr = list(map(int, si().split()))

    max_pq = []
    min_pq = []
    mid = arr[0]
    print(mid, end=' ')
    for i in range(1, N):
        if(i % 2 == 1):
            if arr[i] > mid:
                heapq.heappush(min_pq, arr[i])
            else:
                heapq.heappush(max_pq, -arr[i])

        else:
            if len(max_pq) > len(min_pq):
                p = -heapq.heappop(max_pq)
            else:
                p = heapq.heappop(min_pq)
            l, mid, r = sorted([mid, p, arr[i]])

            heapq.heappush(min_pq, r)
            heapq.heappush(max_pq, -l)

            print(mid, end= ' ')
    print()