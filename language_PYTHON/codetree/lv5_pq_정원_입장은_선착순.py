# 복습 횟수:1, 01:00:00, 복습필요:***
import heapq
import sys

si = sys.stdin.readline 

N = int(si())
arr = []
for i in range(N):
    arrive, wait = map(int, si().split())
    arr.append([arrive, wait, i+1])

arr.append([sys.maxsize, 1, N+1])
waiting_q = []
finish_time = 0

answer = -1
arr.sort(key=lambda x:[x[0], x[2]])

for human in arr:
    arrive, wait, index = human

    while arrive >= finish_time and waiting_q:
        next_index, next_arrive, next_wait = heapq.heappop(waiting_q)

        answer = max(answer, finish_time - next_arrive)
        finish_time = finish_time + next_wait

    if arrive >= finish_time:
        finish_time = arrive + wait
    else: # 기다려야함
        heapq.heappush(waiting_q, [index, arrive, wait])
        # waiting_q.append([index, arrive, wait])

print(answer)