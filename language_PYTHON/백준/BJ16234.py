# 인구 이동
# 복습 횟수:2, 01:30:00
import sys
from collections import deque
si = sys.stdin.readline
N, L, R = map(int, si().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
graph = []
for i in range(N):
    graph.append(list(map(int, si().split())))

def bfs(x, y, cnt, visited :list, check):
    q = deque()
    q.append([x, y])
    visited[x][y] = cnt # 방문처리

    while q:
        x, y = q.popleft()
        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]
            if not (0 <= nx < N and 0 <= ny < N): continue 
            if visited[nx][ny] != 0: continue 

            if L <= abs(graph[nx][ny] - graph[x][y]) <= R:
                visited[nx][ny] = cnt
                q.append([nx, ny])
                check += 1

    if check == 0:
        return -1

    return 1
answer = 0
while True:
    visited = [[0 for i in range(N)] for i in range(N)]
    # 연합 구성하기
    cnt = 1
    for i in range(N):
        for j in range(N):
            if visited[i][j] != 0: continue # 방문한 곳은 패스
    
            flag = bfs(i, j, cnt, visited, 0)
            if flag == 1:
                cnt += 1
            else: 
                visited[i][j] = -1 # -1로 방문처리 
    flag = 1
    for i in range(N):
        for j in range(N):
            if visited[i][j] != -1:
                flag = 0
    if flag:
        print(answer)
        break
    else:
        answer += 1
    # 초기화 해주기
    for idx in range(1, cnt):
        team = []
        for i in range(N):
            for j in range(N):
                if visited[i][j] == idx:
                    team.append([i, j, graph[i][j]])
        divider = len(team)
        sumi = 0 
        for x, y, val in team:
            sumi += val
        
        init = sumi // divider
        # 초기화하기
        for x, y, val in team:
            graph[x][y] = init