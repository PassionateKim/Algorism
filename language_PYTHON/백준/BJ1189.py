# 컴백홈
import sys
si = sys.stdin.readline

N, M, K = map(int, si().split())
graph = []
answer = 0

for i in range(N):
    tmp = list(map(str, si().rstrip()))
    graph.append(tmp)
visited = [[0 for i in range(M)]for i in range(N)]
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 현재 위치 [N-1][0]
# 도착 위치 [0][M-1]
visited[N-1][0] = 1 # 방문처리
def dfs(x, y, count):
    global answer
    # 도착한 경우
    if (x == 0 and y == M-1): 
        if (count == K):
            answer = answer + 1
        return
        
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0 <= nx < N and 0 <= ny < M): continue
        if visited[nx][ny] != 0: continue
        if graph[nx][ny] == 'T': continue

        visited[nx][ny] = 1 # 방문초리
        dfs(nx, ny, count + 1)
        visited[nx][ny] = 0 # 방문 초기화

dfs(N-1, 0, 1)

print(answer)