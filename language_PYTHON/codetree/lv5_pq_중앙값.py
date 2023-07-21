# 2023-07-19
# 복습 횟수:1, 01:00:00, 복습필요:***
import heapq
import sys
si = sys.stdin.readline 
T = int(si())


def find_mid():
    mid = arr[0]
    max_pq, min_pq = [], []

    print(mid, end = " ")

    for i in range(1, N):
        if i % 2 == 1:
            if arr[i] > mid:
                heapq.heappush(min_pq, arr[i])
            else:
                heapq.heappush(max_pq, -arr[i])

        else:
            if len(max_pq) > len(min_pq):
                new = -heapq.heappop(max_pq)
            else:
                new = heapq.heappop(min_pq)
            
            l, m, r = sorted([new, arr[i], mid])

            heapq.heappush(min_pq, r)
            heapq.heappush(max_pq, -l)
            mid = m

            print(mid, end = " ")

    print()        
    return


for i in range(T):
    N = int(si())
    arr = list(map(int, si().split()))

    find_mid()