# 복습 횟수:0, 00:10:00, 복습필요X
import heapq
import sys

si = sys.stdin.readline 
N = int(si())
myList = list(map(int, si().split()))
candidate_list = []

for l in myList:
    candidate_list.append(-l)

heapq.heapify(candidate_list)

while True:
    if len(candidate_list) == 0:
        print(-1)
        break

    if len(candidate_list) == 1:
        print(-candidate_list[0])
        break

    if len(candidate_list) >= 2:
        first = candidate_list[0]
        heapq.heappop(candidate_list)
        second = candidate_list[0]
        heapq.heappop(candidate_list)

        diff = first - second
        if(diff == 0): continue

        heapq.heappush(candidate_list, diff)