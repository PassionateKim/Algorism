# 인구 이동
import sys
from collections import deque
si = sys.stdin.readline

N, L, R = map(int, si().split())
# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

graph = [] # 이차원 배열 사용

# 인구 넣기
for i in range(N):
    tmp = list(map(int, si().split()))
    graph.append(tmp)
    
def bfs(i,j):
    global total, flag
    q = deque()
    q.append((i,j))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if not (0<= nx <N and 0<= ny <N): continue
            if visited[nx][ny] == 1: continue

            if L<= abs(graph[x][y] - graph[nx][ny]) <=R:
                visited[nx][ny] = 1 # 방문처리
                flag = 1
                arr.append((nx, ny))
                q.append((nx, ny))
                total += graph[nx][ny]
    return


day = 0
arr = []
while True:
    visited = [[0 for _ in range(N)] for _ in range(N)] 
    flag = 0

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0: # 방문하지 않은 경우만
                visited[i][j] = 1 # 방문처리
                # 초기화
                total = graph[i][j]
                arr = [(i, j)]
                bfs(i,j)

                # 연합의 값 초기화 하기
                if len(arr) > 1: # 연합이 있는 경우
                    averi = total // len(arr)
                    while arr:
                        x, y = arr.pop()
                        graph[x][y] = averi
    
    if flag == 0:
        break
    else:
        day += 1

print(day)

