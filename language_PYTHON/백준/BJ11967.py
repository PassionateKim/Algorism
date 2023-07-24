# 복습 횟수:0, 03:00:00, 복습필요:***
import sys
from collections import deque, defaultdict
input = sys.stdin.readline 
N, M = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[0 for i in range(N+1)] for i in range(N+1)] # 방문한 칸
candidate = [[0 for i in range(N+1)] for i in range(N+1)] # 방문 가능한 칸
light = [[0 for i in range(N+1)] for i in range(N+1)] # 불 켜진 칸

dict = defaultdict(list)
q = deque()

def bfs():

    answer = 1
    q.append([1, 1])
    visited[1][1] = 1 # 방문처리
    light[1][1] = 1 # 방문처리
    candidate[1][1] = 1

    while q:
        x, y = q.popleft()
        for d in dict[(x, y)]:
            if not light[d[0]][d[1]]:
                light[d[0]][d[1]] = 1
                answer += 1
        
        # (x, y)칸 중에서 상하좌우 이동이 가능한 칸
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 1 <= nx <= N and 1 <= ny <= N:
                candidate[nx][ny] = 1
        
        for i in range(1, N+1):
            for j in range(1, N+1):
                if not visited[i][j] and light[i][j] and candidate[i][j]:
                    visited[i][j] = 1
                    q.append([i, j])
    
    return answer

for i in range(M):
    x, y, a, b = map(int, input().split())
    dict[(x, y)].append((a, b))

print(bfs())