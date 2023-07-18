# 복습 횟수:0, 00:15:00,복습필요X
import heapq
import sys
si = sys.stdin.readline
N, M = map(int, si().split())

elem_list = list(map(int, si().split()))

candidate_list = []
for elem in elem_list:
    candidate_list.append(-elem)

heapq.heapify(candidate_list)
for i in range(M):
    maxi = candidate_list[0]
    input = maxi + 1
    heapq.heappop(candidate_list)
    heapq.heappush(candidate_list, input)

print(-candidate_list[0])