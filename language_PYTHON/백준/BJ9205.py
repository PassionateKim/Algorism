# 맥주 마시면서 걸어가기
# 복습 횟수:1, 00:30:00, 복습필요O

import sys
from collections import deque
si = sys.stdin.readline
T = int(si())

def bfs():
    visited = [0 for i in range(n)]
    q = deque()
    q.append([location_x, location_y])

    while q:
        x, y = q.popleft()
        if (abs(festival_x - x) + abs(festival_y - y) <= 1000):
            return "happy"
        
        for i in range(n):
            if visited[i] == 1: continue # 방문처리
            
            # 맨해튼 거리 계산
            if abs(store_list[i][0] - x) + abs(store_list[i][1] - y) > 1000: continue


            q.append([store_list[i][0], store_list[i][1]])
            visited[i] = 1 # 방문처리

    return "sad"

for i in range(T):
    n = int(si()) # 맥주를 파는 편의점 개수
    location_x, location_y = map(int, si().split())
    
    store_list = []
    for j in range(n):
        x, y = map(int, si().split())
        store_list.append([x, y])
    
    festival_x, festival_y = map(int, si().split())

    output = bfs()
    print(output)