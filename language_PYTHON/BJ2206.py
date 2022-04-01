#벽 부수고 이동하기
N,M = map(int,input().split())
import sys
from collections import deque

visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

maze = []


#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(N):
    maze.append(list(map(int,sys.stdin.readline().rstrip())))



def BFS():
    queue = deque()
    queue.append([0,0,1])
    visited[0][0][1] = 1 #벽을 한번 부술 수 있는 상태에서 시작.
    
    print("visited 시작---")
    for i in visited:
        print(i)

    while queue:
        x,y,w = queue.popleft()
        
        if x == N-1 and y == M-1:
            return visited[x][y][w]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if(0<=nx<N and 0<=ny<M):
                if maze[nx][ny] == 1 and w == 1: #벽을 만나서 처음으로 부수는 경우
                    visited[nx][ny][0] = visited[x][y][w] + 1
                    queue.append([nx,ny,0])
                elif maze[nx][ny] == 0 and visited[nx][ny][w] == 0: 
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    queue.append([nx,ny,w])
        
        
    return -1


print(BFS())


print("--------")       
for i in visited:
    print(i)

