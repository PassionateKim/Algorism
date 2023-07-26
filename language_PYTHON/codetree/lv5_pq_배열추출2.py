# 복습 횟수:0, 01:00:00, 복습필요X
import heapq
import sys

si = sys.stdin.readline 

N = int(si())

minus_pq = []
plus_pq = []

for i in range(N):
    input = int(si())

    if input < 0:
        heapq.heappush(minus_pq, -input)
    elif input > 0:
        heapq.heappush(plus_pq, input)
    else: # input == 0 인 경우
        if len(minus_pq) + len(plus_pq) == 0:
            print(0)
        else:
            if len(minus_pq) == 0:
                print(heapq.heappop(plus_pq))
            elif len(plus_pq) == 0:
                print(-heapq.heappop(minus_pq))
            else:
                plus = plus_pq[0]
                minus = -minus_pq[0]

                if abs(plus) >= abs(minus):
                    print(minus)
                    heapq.heappop(minus_pq)
                else:
                    print(plus)
                    heapq.heappop(plus_pq)