#절대값 힙
import heapq
import sys

heap = []
N = int(input())

for _ in range(N):
    a = int(sys.stdin.readline())
    
    if a == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    
    
    else:
        if a < 0:
            heapq.heappush(heap,(-a,a))
        else:
            heapq.heappush(heap,(a,a))
            
