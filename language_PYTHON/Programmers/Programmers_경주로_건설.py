# 복습 횟수:1, 00:30:00, 복습필요O
from collections import deque
import math

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(board):

    def bfs(x, y, direction, cost):
        q = deque()
        q.append([x, y, direction, cost])
        n = len(board)
        result = [[math.inf for _ in range(n)] for _ in range(n)]
        result[x][y] = 0 

        while q:
            x, y, direction, cost = q.popleft()
            for idx in range(4):
                nx, ny = x + dx[idx], y + dy[idx]

                if not (0 <= nx < n and 0 <= ny < n): continue
                if board[nx][ny] == 1: continue

                if direction != idx:
                    new_cost = cost + 600
                else:
                    new_cost = cost + 100
                
                if new_cost < result[nx][ny]:
                    q.append([nx, ny, idx, new_cost])
                    result[nx][ny] = new_cost

        return result[-1][-1]
    
    return min(bfs(0, 0, 1, 0), bfs(0, 0, 3, 0))
    
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))