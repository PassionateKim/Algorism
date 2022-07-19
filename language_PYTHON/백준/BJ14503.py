#로봇 청소기
import sys
si = sys.stdin.readline

# 북, 동, 남, 서
dir = [(-1,0), (0,1), (1,0), (0,-1)]
N, M = map(int, si().split())
r, c, d = map(int, si().split())
visited = [[0 for _ in range(M)] for _ in range(N)]
graph = [list(map(int, si().split())) for _ in range(N)]

def checkLeft():
    if d == 0:
        return 3
    elif d == 1:
        return 0
    elif d == 2:
        return 1
    else:
        return 2

def checkBehind():
    if d == 0:
        return r+1, c
    elif d == 1:
        return r, c-1
    elif d == 2:
        return r-1, c
    else:
        return r, c+1


answer = 0
while True:
    
    # 1. 현재 위치를 청소한다.
    answer += 1 # 추가
    visited[r][c] = 1 # 청소처리
    # 2. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례로 탐색
    cnt = 0
    while True:
        print(r, c)
        leftDir = checkLeft()
        nx,  ny = r + dir[leftDir][0], c + dir[leftDir][1] # 왼쪽
        if visited[nx][ny] == 0 and graph[nx][ny] == 0: # 청소가능하다면
            r, c, d = nx, ny, leftDir
            break # 1번부터 진행한다.
        else:
            cnt += 1 # 회전 개수 세주기
            d = leftDir # 회전만
        
        if cnt == 4:
            x, y = checkBehind()
            if graph[x][y] == 1: # 벽인 경우
                print(answer)
                exit()
            else:
                r, c = x, y # 한칸 후진
                cnt = 0
                continue # 2번으로 돌아간다.
        
        