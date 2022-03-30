#토마토 3D
import sys
from collections import deque
M,N,H = map(int,input().split())

tomato_grah = []

#상하좌위아래
dx = [-1,1,0,0,-N,N]
dy = [0,0,-1,1,0,0]


for i in range(N*H):
    tomato_grah.append(list(map(int,sys.stdin.readline().rstrip().split())))

#토마토 익기전
# for i in tomato_grah:
#     print(i)

#익은 토마토 체크
ripen_tomato_cnt = 0
no_tomato_cnt = 0

ripen_tomato_queue = deque()
for i in range(N*H):
    for j in range(M):
        if(tomato_grah[i][j] == 1):
            ripen_tomato_cnt += 1
            ripen_tomato_queue.append([i,j])

        elif(tomato_grah[i][j] == -1):
            no_tomato_cnt += 1
# print(ripen_tomato_queue)

def BFS():
    #저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력
    if(ripen_tomato_cnt + no_tomato_cnt == (N*H)*(M)):
        print(0)
        return 

    while ripen_tomato_queue:
        x, y = ripen_tomato_queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            

            if(0 <= nx < N*H and 0 <= ny < M):
                if (tomato_grah[nx][ny] == 0):
                    ripen_tomato_queue.append([nx,ny])
                    tomato_grah[nx][ny] = tomato_grah[x][y] + 1
                    for i in tomato_grah:
                        print(i)
                    print("------")
    #토마토밭 출력
    # for i in tomato_grah:
    #     print(i)
    #토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.
    for i in range(N*H):
        for j in range(M):
            if(tomato_grah[i][j] == 0):
                print(-1)
                return
                
    answer = max(map(max,tomato_grah)) - 1
    print(answer)
    return
    
BFS()
