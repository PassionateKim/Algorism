#최소 힙
import sys
import heapq
N = int(input())
heap = []

for _ in range(N):
    m = int(sys.stdin.readline())
    if m == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap,m)

