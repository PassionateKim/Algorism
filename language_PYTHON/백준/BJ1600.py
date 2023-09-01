# 복습 횟수:0, 02:30:00 ,복습필요3
import sys
from collections import deque

si = sys.stdin.readline 
K = int(si())
M, N = map(int, si().split())

graph = []
for i in range(N):
    tmp = list(map(int, si().split()))
    graph.append(tmp)
horse_move_and_standard_move = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[[0]*(K + 1) for i in range(M)] for i in range(N)]


def bfs():
    q = deque()
    # x, y, count, k_left
    q.append([0, 0, 0, K])
    visited[0][0][0] = 1 # 방문 처리

    while q:
        x, y, count, k_left = q.popleft()
        if x == N - 1 and y == M - 1: 
            return visited[x][y][K- k_left] - 1

        for idx, move in enumerate(horse_move_and_standard_move):
            nx, ny = x + move[0], y + move[1]

            if not (0 <= nx < N and 0 <= ny < M): continue # 범위를 벗어난 경우 
            if graph[nx][ny] == 1: continue # 도착지가 장애물인 경우 
            
            if k_left >= 1: # 말 흉내가 남아있는 경우
                if 0 <= idx <= 7:
                    if visited[nx][ny][K - k_left + 1] != 0: continue

                    q.append([nx, ny, count + 1, k_left - 1])
                    visited[nx][ny][K - k_left + 1] = visited[x][y][K - k_left] + 1 # 방문 처리
                else:
                    if visited[nx][ny][K - k_left] != 0: continue

                    q.append([nx, ny, count + 1, k_left])
                    visited[nx][ny][K - k_left] = visited[x][y][K - k_left] + 1 # 방문 처리

            else: # 말 흉내가 남아있지 않은 경우
                if 0 <= idx <= 7: 
                    pass
                else:
                    if visited[nx][ny][K - k_left] != 0: continue
 
                    q.append([nx, ny, count + 1, k_left])
                    visited[nx][ny][K- k_left] = visited[x][y][K - k_left] + 1 # 방문 처리
                
    return -1

print(bfs())