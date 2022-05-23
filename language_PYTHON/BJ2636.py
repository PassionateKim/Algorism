from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def find_air():
    visited = [[False] * M for _ in range(N)]
    q = deque()
    q.append((0,0))
    visited[0][0] = True
    cnt = 0 
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == False:
                if graph[nx][ny] == 0: # 0 이면 체크
                    visited[nx][ny] = True # 방문처리
                    q.append((nx, ny))
                elif graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    cnt += 1
                    visited[nx][ny] = True
    cheese.append(cnt)
    return cnt

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
cheese = []
time = 0
while True:
    time += 1
    cnt = find_air()
    if cnt == 0:
        break

print(time - 1)
print(cheese)