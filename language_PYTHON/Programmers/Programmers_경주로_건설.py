# 복습 횟수:3, 00:30:00, 복습필요X
dx = [-1, 1, 0, 0] # 상 하 좌 우 
dy = [0, 0, -1, 1]
import sys
from collections import deque
def solution(board):
    inf = sys.maxsize
    candidate = []
    # 가로 시작
    visited = [[inf for i in range(len(board[0]))] for i in range(len(board))]
    q = deque()
    q.append([0, 0, 0, 1]) # x y price dir
    while q:
        x, y, price, dir = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not (0 <= nx < len(board) and 0 <= ny < len(board[0])): continue
            if board[nx][ny] == 1: continue

            if dir == 1: # 가로인 경우
                if i in [0, 1]:
                    new_price = price + 500 + 100
                    new_dir = -1
                else:
                    new_price = price + 100
                    new_dir = 1 
            else: # 세로인 경우
                if i in [0, 1]:
                    new_price = price + 100
                    new_dir = -1
                else:
                    new_price = price + 500 + 100
                    new_dir = 1
            

            if new_price <= visited[nx][ny]:
                q.append([nx, ny, new_price, new_dir])
                visited[nx][ny] = new_price
    
    candidate.append(visited[len(board)-1][len(board[0])-1])


    # 세로 시작
    visited = [[inf for i in range(len(board[0]))] for i in range(len(board))]
    q = deque()
    q.append([0, 0, 0, -1])
    while q:
        x, y, price, dir = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not (0 <= nx < len(board) and 0 <= ny < len(board[0])): continue
            if board[nx][ny] == 1: continue

            if dir == 1: # 가로인 경우
                if i in [0, 1]:
                    new_price = price + 500 + 100
                    new_dir = -1
                else:
                    new_price = price + 100
                    new_dir = 1 
            else: # 세로인 경우
                if i in [0, 1]:
                    new_price = price + 100
                    new_dir = -1
                else:
                    new_price = price + 500 + 100
                    new_dir = 1
            

            if new_price <= visited[nx][ny]:
                q.append([nx, ny, new_price, new_dir])
                visited[nx][ny] = new_price

    candidate.append(visited[len(board)-1][len(board[0])-1])

    return min(candidate)


print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))