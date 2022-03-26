#미로 탐색

from collections import deque



N,M = map(int,input().split())

#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

maze =list()
for i in range(N):
    maze.append(list(map(int,input())))

#미로
# for i in maze:
#     print(i)

#BFS 정의하기
def BFS(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #미로 범위 N * M 을 넘지 않는다는 조건
            if(0 <= nx < N and 0 <= ny < M):
                #0이면 탐색을 하지 않는다는 조건
                if(maze[nx][ny] == 1):
                    maze[nx][ny] = maze[x][y] + 1
                    queue.append((nx,ny))



        


    

BFS(0,0)
print(maze[N-1][M-1])