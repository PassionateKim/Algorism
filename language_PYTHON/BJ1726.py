#로봇
import sys
from collections import deque

M,N = map(int,input().split())
factory_graph = []
visited = [[0 for _ in range(N)] for _ in range(M)]
#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]


for i in range(M):
    factory_graph.append(list(map(int,sys.stdin.readline().split())))

start_point = list(map(int,sys.stdin.readline().split()))
end_point = list(map(int,sys.stdin.readline().split()))

def way(a,b):
    #방향이 같은 경우
    if a == b:
        return 0
    #a가 북쪽인 경우
    elif a == 4:
        # b가 동,서쪽인 경우
        if b == 1 or b == 2:
            return 1
        #남쪽인 경우
        else:
            return 2
    #a가 남쪽인 경우
    elif a == 3:
        #b가 동,서쪽인 경우
        if b == 1 or b == 2:
            return 1
        #북쪽인 경우
        else:
            return 2
    #a가 서쪽인 경우
    elif a == 2:
        #b가 북쪽,남쪽인 경우
        if b == 4 or b == 3:
            return 1
        #b가 서쪽인 경우
        else:
            return 2
    #a가 동쪽인 경우
    else:
        #b가 북쪽,남쪽인 경우
        if b == 4 or b == 3:
            return 1
        #b가 서쪽인 경우
        else:
            return 2        


     

def BFS(x,y,direction):
    q = deque()
    q.append([x,y,direction])
    #시작점 방문
    visited[x][y] = 1
    #start 지점과 end 지점이 똑같은 경우
    if x == end_point[0] - 1 and y == end_point[1] - 1:
        value = way(end_point[2], start_point[2])
        print(value)
        return 
    
    while q:
        print(q)
        x,y,direction = q.popleft()
        if x == end_point[0] - 1 and y == end_point[1] - 1:
            print(visited[x][y] - 1)
            return
        print("왜 return 했는데 밑의 코드가 읽히냐?")
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #사이즈 안쪽으로
            if (0<= nx <M and 0<= ny <N):
                #길이 뚫려있다 && 방문하지 않았다.
                if factory_graph[nx][ny] == 0 and visited[nx][ny] == 0:
                    #뚫려 있는 것이 북쪽인 경우
                    if nx == x - 1:
                        differ = way(4, direction)
                        visited[nx][ny] = visited[x][y] + 1 + differ
                        q.append([nx,ny,4])
                    #뚫려 있는 것이 남쪽인 경우
                    elif nx == x + 1:
                        differ = way(3, direction)
                        visited[nx][ny] = visited[x][y] + 1 + differ
                        q.append([nx,ny,3])
                    #뚫려 있는 것이 서쪽인 경우
                    elif ny == y - 1:
                        differ = way(2, direction)
                        visited[nx][ny] = visited[x][y] + 1 + differ
                        q.append([nx,ny,2])
                    #뚫려 있는 것이 동쪽인 경우
                    else:
                        differ = way(1, direction)
                        visited[nx][ny] = visited[x][y] + 1 + differ
                        q.append([nx,ny,1])
            
                
                    
#index 이므로                 
BFS(start_point[0] - 1, start_point[1] - 1, start_point[2])


                    


                      

                    

            
                







#index 는 0으로 시작하므로 - 1
BFS(start_point[0] - 1,start_point[1] - 1,start_point[2])