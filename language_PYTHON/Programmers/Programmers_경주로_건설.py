# 복습 횟수:2, 00:30:00, 복습필요O

from collections import deque
import math
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(board):
    
    N = len(board)
    M = len(board[0])

    def bfs(x, y, dir, price):
        visited = [[math.inf for _ in range(M)] for __ in range(N)]
        visited[x][y] = 0 # 처음부분은 0으로 초기화

        q = deque()
        q.append([x, y, dir, price])

        while q:
            x, y, dir, price = q.popleft()
        
            # new_price가 더 작을 때만 갈 수 있도록 하기
            for idx in range(4):
                nx, ny = x + dx[idx], y + dy[idx]

                if not (0 <= nx < N and 0 <= ny < M): continue # 범위밖 X
                if board[nx][ny] == 1: continue # 벽이기 때문에 갈 수 없으므로
                # 방향이 같은 경우
                if idx == dir:
                    new_price = price + 100
                else: # 방향이 달라서 꺾어야 하는 경우
                    new_price = price + 600
                
                if new_price < visited[nx][ny]: # 가격이 더 작을 때에만
                    q.append([nx, ny, idx, new_price])
                    visited[nx][ny] = new_price

        return visited[-1][-1]

    return min(bfs(0, 0, 1, 0), bfs(0, 0, 3, 0))
    
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))