#유기농 배추
import sys
sys.setrecursionlimit(10**7)
T = int(input())
warm = []
bae_chu = 0

#상하좌우
dx = [0,0,-1,1]
dy = [-1,1,0,0]

#행과 열을 직관적으로 판단하기 위해 각각 y , x 로 맵핑한다.
def DFS(y,x):
    global bae_chu
    #방문체크
    visited[y][x] = 1
    bae_chu += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if(0 <= ny < N and 0 <= nx < M):
            if(visited[ny][nx] != 1 and farm[ny][nx] == 1):
                DFS(ny,nx)

for i in range(T):
    #입력
    M,N,K = map(int,sys.stdin.readline().rstrip().split())
    
    #농장 초기화
    farm = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    #배추 위치 넣기
    #문제에서 요구하는 x좌표 y좌표가 컴퓨터에서의 이중배열과 반대라
    #x,y -> y,x로 바꿔서 넣어줌
    for j in range(K):
        x,y = map(int,sys.stdin.readline().rstrip().split())
        farm[y][x] = 1

    #배추밭 출력해보기 
    # for i in farm:
    #     print(i)
    
    for i in range(N):
        for j in range(M):
            if(farm[i][j] == 1 and visited[i][j] == 0):
                DFS(i,j)
                warm.append(bae_chu)
                bae_chu = 0
    print(len(warm))
    warm.clear()