# 맥주 마시면서 걸어가기
# 복습 횟수:2, 00:30:00, 복습필요:3
import sys
from collections import deque
si = sys.stdin.readline 
T = int(si())

def bfs():
    visited = [0 for i in range(len(store_list))]

    q = deque()
    q.append([home[0], home[1], 20])
    
    while q:
        home_x, home_y, beer_sum = q.popleft()
        real_diff = abs(home_x - festival[0]) + abs(home_y - festival[1])
        if real_diff <= 1000:
            return "happy"

        for i in range(len(store_list)):
            store_x, store_y = store_list[i]

            diff = abs(home_x - store_x) + abs(home_y - store_y)

            if visited[i] != 0: continue
            if diff <= beer_sum * 50:
                visited[i] = 1 
                q.append([store_x, store_y, 20])

    return "sad"
for i in range(T):
    N = int(si())
    home = list(map(int, si().split()))

    store_list = []
    for j in range(N):
        x, y = map(int, si().split())
        store_list.append([x, y])

    festival = list(map(int, si().split()))

    print(bfs())