# 영역 구하기 
import sys
from collections import deque
input = sys.stdin.readline
M, N, K = map(int, input().split())
graph = [[0] * N for _ in range(M)]
visited = [[0] * N for _ in range(M)]
answer = []

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 직사각형인 부분에 1 값을 넣어 구분하기
for i in range(K): 
    # 왼쪽 아래:x1, y1 오른쪽 위:x2, y2
    x1, y1, x2, y2 = map(int, input().split())
    y_differ = y2 - y1 
    x_differ = x2 - x1
    # 직사각형 좌표와 graph의 좌표가 대응하게 조정
    x1, adjusted_x2, adjusted_y1, adjusted_y2 = x1, x2-1, M-y1-1, M-y2
    
    for y in range(adjusted_y2, adjusted_y2 + y_differ):
        for x in range(x1, x1 + x_differ):
            graph[y][x] = 1 # 1로 구분
            

def bfs(i,j):
    global cnt
    cnt += 1 
    q = deque()
    q.append((i,j))
    visited[i][j] = 1 # 방문처리
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < M and 0 <= ny < N) and visited[nx][ny] == 0 and graph[nx][ny] == 0:
                q.append((nx,ny))
                visited[nx][ny] = 1 # 방문처리
                cnt += 1 # 영역 개수 체크  
    answer.append(cnt)          
    return

for i in range(M):
    for j in range(N):
        if graph[i][j] == 0 and visited[i][j] == 0:
            cnt = 0 
            bfs(i,j)


answer.sort()
print(len(answer))
print(*answer)

