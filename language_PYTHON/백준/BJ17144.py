# 미세먼지 안녕
# 복습 횟수:3, 01:00:00, 복습필요X
import sys
from collections import deque
si = sys.stdin.readline 
N, M , T = map(int, si().split())

graph = []
for i in range(N):
    tmp = list(map(int, si().split()))
    graph.append(tmp)


cleaner_location_list = []

for i in range(N):
    for j in range(M):
        if graph[i][j] == -1:
            cleaner_location_list.append([i, j])

up_cleaner = cleaner_location_list[0]
down_cleaner = cleaner_location_list[1]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def spread():
    tmp = [[0 for i in range(M)] for i in range(N)]

    for x in range(N):
        for y in range(M):
            # 5 미만이면 확산되지 않음
            if graph[x][y] < 5: continue
            
            spread_dust_amount = graph[x][y] // 5
            
            for idx in range(4):
                nx, ny = x + dx[idx], y + dy[idx]
                if not (0 <= nx < N and 0 <= ny < M): continue
                if graph[nx][ny] == -1: continue # 공기청정기라면 

                tmp[nx][ny] += spread_dust_amount
                graph[x][y] -= spread_dust_amount 
     
   
    # 초기화
    for x in range(N):
        for y in range(M):
            graph[x][y] += tmp[x][y]

def changeLocation(graph, cleaner_x, cleaner_y, q: deque):
    q.append(graph[cleaner_x][cleaner_y])
    if len(q) == 2:
        val = q.popleft()
        graph[cleaner_x][cleaner_y] = val

for t in range(T):
    # 확산
    spread()
    
    up_cleaner_x, up_cleaner_y = up_cleaner
    q = deque()
    remember_cleaner_x, remember_cleaner_y = up_cleaner 
    # 좌 -> 우
    for i in range(M-1):
        up_cleaner_y += 1
        
        changeLocation(graph, up_cleaner_x, up_cleaner_y, q)

    # 우 -> 상
    for i in range(up_cleaner_x):
        up_cleaner_x -= 1

        changeLocation(graph, up_cleaner_x, up_cleaner_y, q)

    # 상 -> 좌
    for i in range(M-1):
        up_cleaner_y -= 1

        changeLocation(graph, up_cleaner_x, up_cleaner_y, q)

    
    # 좌 -> 하
    for i in range(remember_cleaner_x - 1):
        up_cleaner_x += 1

        changeLocation(graph, up_cleaner_x, up_cleaner_y, q)
    
    
    graph[remember_cleaner_x][remember_cleaner_y + 1] = 0
    
    # 아래
    down_cleaner_x, down_cleaner_y = down_cleaner
    q = deque()
    remember_cleaner_x, remember_cleaner_y = down_cleaner

    # 좌 -> 우
    for i in range(M-1):
        down_cleaner_y += 1

        changeLocation(graph, down_cleaner_x, down_cleaner_y, q)
    
    # 우 -> 하
    for i in range(N-1 - remember_cleaner_x):
        down_cleaner_x += 1

        changeLocation(graph, down_cleaner_x, down_cleaner_y, q)
    
    # 하 -> 좌
    for i in range(M-1):
        down_cleaner_y -= 1

        changeLocation(graph, down_cleaner_x, down_cleaner_y, q)
    
    # 좌 -> 상
    for i in range(N-1 - remember_cleaner_x - 1):
        down_cleaner_x -= 1

        changeLocation(graph, down_cleaner_x, down_cleaner_y, q)
    
    graph[remember_cleaner_x][remember_cleaner_y +1] = 0
    
answer = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == -1: continue
        
        answer += graph[i][j]

print(answer)