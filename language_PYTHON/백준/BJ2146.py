# 복습 횟수:0, 02:30:00, 복습필요2
from collections import deque
import sys
si = sys.stdin.readline 
N = int(si())
graph = []
for i in range(N):
    tmp = list(map(int, si().split()))
    graph.append(tmp)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

check_island = 1
island_graph = [[0 for i in range(N)] for i in range(N)]
def bfs(x, y, check_island):
    q = deque()
    q.append([x, y])
    island_graph[x][y] = check_island

    while q:
        x, y = q.popleft()
        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]
            if not (0 <= nx < N and 0 <= ny < N): continue

            if graph[nx][ny] == 1 and island_graph[nx][ny] == 0: # 옆이 땅인 경우
                q.append([nx, ny])
                island_graph[nx][ny] = check_island

    return

# 구분하기
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and island_graph[i][j] == 0:# 섬이고 방문 안한 경우
            bfs(i, j, check_island)
            check_island += 1

# 쌍 찾기
answer = sys.maxsize

def bfs_close(home):
    visited = [[0 for i in range(N)] for i in range(N)]
    q = deque()
    
    for i in range(N):
        for j in range(N):
            if island_graph[i][j] == home:
                q.append([i, j, 0])
                visited[i][j] = 1 # 방문처리
    
    while q:
        x, y, candidate = q.popleft()
        
        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]
            if not (0 <= nx < N and 0 <= ny < N): continue
            if visited[nx][ny] != 0: continue
            
            if island_graph[nx][ny] > 0 and island_graph[x][y] != home:
                return candidate
            
            if island_graph[nx][ny] == 0:
                q.append([nx, ny, candidate + 1])
                visited[nx][ny] = 1 # 방문처리

    # 안되는 경우는 그냥 최댓값을 뱉어낸다.
    return sys.maxsize

for i in range(1, check_island):
    candidate = bfs_close(i)
    answer = min(candidate, answer)

print(answer)