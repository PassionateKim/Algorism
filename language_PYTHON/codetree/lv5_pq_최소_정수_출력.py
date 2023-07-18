# 복습 횟수:0 00:10:00 복습필요X
import heapq
import sys
si = sys.stdin.readline 
N = int(si())

myList = list()
for i in range(N):
    input = int(si())

    if input == 0:
        if len(myList) == 0:
            print(0)
        else:
            print(myList[0])
            heapq.heappop(myList)
    else:
        heapq.heappush(myList, input)