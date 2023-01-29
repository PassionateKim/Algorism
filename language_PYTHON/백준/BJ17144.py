# 미세먼지 안녕
# 복습 횟수:2, 01:45:00, 복습필요O
import sys
from collections import deque
si = sys.stdin.readline

N, M, T = map(int, si().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    tmp = list(map(int, si().split()))
    graph.append(tmp)

for i in range(T):
    cleaner = deque()

    for i in range(N):
        for j in range(M):
            if graph[i][j] == -1:
                cleaner.append([i, j])

    # 1. 확산
    tmp_graph = [[0 for i in range(M)] for i in range(N)]
    # 예외 - 공기청정기 위치는 불가능
    for x in range(N):
        for y in range(M):
            if graph[x][y] < 5: continue # 어차피 확산되지 않으므로 continue
            val = graph[x][y] // 5  # Ar,c/5이고 소수점은 버린다.
            cnt = 0
            # 상하 좌우
            for idx in range(4):
                nx, ny = x + dx[idx], y + dy[idx]
                if not (0 <= nx < N and 0 <= ny < M): continue
                if graph[nx][ny] == -1: continue # 공기청정기라면

                cnt += 1
                tmp_graph[nx][ny] += val
            
            graph[x][y] = graph[x][y] - (cnt * val)
    # 초기화
    for i in range(N):
        for j in range(M):
            graph[i][j] = graph[i][j] + tmp_graph[i][j]
    
    # 2. 이동
    # 2-1 상부
    cleaner_x, cleaner_y = cleaner.popleft()
    q = deque()
    # 좌 -> 우
    for i in range(cleaner_y+1, M):
        q.append(graph[cleaner_x][i])

        if len(q) == 2:
            tmp = q.popleft()
            graph[cleaner_x][i] = tmp 

    # 우 -> 상
    for i in range(cleaner_x-1, -1, -1):
        q.append(graph[i][M-1])

        if len(q) == 2:
            tmp = q.popleft()
            graph[i][M-1] = tmp 

    # 상 -> 좌
    for i in range(M-2, -1, -1):
        q.append(graph[0][i])

        if len(q) == 2:
            tmp = q.popleft()
            graph[0][i] = tmp 

    #좌 -> 하
    for i in range(1, cleaner_x):
        q.append(graph[i][0])

        if len(q) == 2:
            tmp = q.popleft()
            graph[i][0] = tmp

    graph[cleaner_x][1] = 0

    # 2-2 하부
    cleaner_x, cleaner_y = cleaner.popleft()
    q = deque()
    # 좌 -> 우
    for i in range(cleaner_y+1, M):
        q.append(graph[cleaner_x][i])

        if len(q) == 2:
            tmp = q.popleft()
            graph[cleaner_x][i] = tmp 

    # 우 -> 하
    for i in range(cleaner_x+1, N):
        q.append(graph[i][M-1])

        if len(q) == 2:
            tmp = q.popleft()
            graph[i][M-1] = tmp 

    # 하 -> 좌
    for i in range(M-2, -1, -1):
        q.append(graph[N-1][i])

        if len(q) == 2:
            tmp = q.popleft()
            graph[N-1][i] = tmp 

    #좌 -> 상
    for i in range(N-2, cleaner_x, -1):
        q.append(graph[i][0])

        if len(q) == 2:
            tmp = q.popleft()
            graph[i][0] = tmp

    graph[cleaner_x][1] = 0

answer = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == -1: continue
        answer += graph[i][j]

print(answer)