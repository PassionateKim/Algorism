# 봄버맨
# 복습 횟수:0, 00:30:00, 복습필요X
import sys
si = sys.stdin.readline
R, C, N = map(int, si().split())
graph = [list(map(str, si().rstrip())) for i in range(R)]
dx = [-1, 1,0 , 0]
dy = [0, 0, -1, 1]

for i in range(R):
    for j in range(C):
        if( graph[i][j] == '.'):
            graph[i][j] = -1
        else:
            graph[i][j] = 3
            
for t in range(N):
    
    for i in range(R):
        for j in range(C):
            if graph[i][j] != -1:
                graph[i][j] -= 1 # 시간이 지나 timer가 -1
    
    # 봄버맨은 다음 1초 동안 아무것도 하지 않는다.
    if(t == 0):
        pass
    else:
        for i in range(R):
            for j in range(C):
                if graph[i][j] == -1:
                    graph[i][j] = 3 # 폭탄을 설치한다.


    # 폭팔할 폭탄 체크
    bomb_list = []
    for i in range(R):
        for j in range(C):
            if graph[i][j] == 0:
                bomb_list.append([i, j])

    for bomb in bomb_list:
        x, y = bomb
        graph[x][y] = -1
        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]
            if not (0 <= nx < R and 0 <= ny < C): continue
            graph[nx][ny] = -1

for i in range(R):
    for j in range(C):
        if(graph[i][j]) == -1:
            graph[i][j] = '.'
        else:
            graph[i][j] = 'O'

for i in graph:
    print(''.join(i))