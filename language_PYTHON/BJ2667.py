import sys

n = int(input())

#그래프 생성하기
graph = []
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip())))

#들어왔는지 체크
visited = [[0] *(n) for _ in range(n)]

# for i in visited:
#     print(i)

#단지 배열
num = []
#아파트 수
count = 0
#상하좌우
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def DFS(x,y):
    global count
    count += 1
    visited[x][y] = 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]  

        if(0 <= nx < n and 0 <= ny < n):
            if(visited[nx][ny] == 0 and graph[nx][ny] == 1):
                DFS(nx,ny)
    



for i in range(n):
    for j in range(n):
        if(visited[i][j] == 0 and graph[i][j] == 1):
            # print(i,j)
            DFS(i,j)
            num.append(count)
            count = 0
# for i in visited:
#     print(i)

num.sort()

print(len(num))

for i in num:
    print(i)
