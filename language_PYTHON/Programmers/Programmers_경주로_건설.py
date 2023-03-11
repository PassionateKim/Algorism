# 복습 횟수:0, 02:30:00, 복습필요O
from collections import deque
import math
dx,dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def solution(board):
    def bfs(x, y, cost, direction):
        n = len(board)
        result = [[math.inf for i in range(n)] for i in range(n)]

        q = deque()
        q.append([x, y, cost, direction])
        result[x][y] = 0
        while q:
            x, y, cost, direction = q.popleft()
            for idx in range(4):
                nx, ny = x + dx[idx], y + dy[idx]
                if not (0 <= nx < n and 0 <= ny < n): continue

                if direction == idx:
                    new_cost = cost + 100
                else: # 방향이 다르다면
                    new_cost = cost + 600

                if new_cost < result[nx][ny] and board[nx][ny] == 0: # 이때만 가능함.
                    q.append([nx, ny, new_cost, idx])
                    result[nx][ny] = new_cost
        
        return result[-1][-1]
    
    return min(bfs(0, 0, 0, 1), bfs(0, 0, 0, 3)) 