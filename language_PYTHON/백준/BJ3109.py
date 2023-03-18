# 빵집
# 복습 횟수:0, 01:00:00, 복습필요O
import sys
si = sys.stdin.readline
R, C = map(int, si().split())
graph = [list(map(str, si().rstrip())) for _ in range(R)]
answer = 0
visited = [[0 for _ in range(C)] for __ in range(R)]

def dfs(x, y):
    global flag
    visited[x][y] = 1 # 방문 처리

    if y == C-1:
        return True
    
    for d in [-1, 0, 1]:
        nx = x + d
        ny = y + 1
        if not (0 <= nx < R and 0 <= ny < C): continue
        
        if visited[nx][ny] == 0 and graph[nx][ny] == '.':
            if dfs(nx, ny):
                return True

    return False

for i in range(R):
    flag = 0
    if dfs(i, 0):
        answer += 1

print(answer)