#로봇 청소기
import sys
si = sys.stdin.readline
N, M = map(int, si().split())
r, c, d = map(int, si().split())
# 북, 동, 남, 서
dir = [(-1,0), (0,1), (1,0), (0,-1)]
robot = [r-1,c-1,d]
graph = []
cnt = 0
answer = 0
for i in range(N):
    graph.append(list(map(int, si().split())))
visited = [[0 for _ in range(N)] for _ in range(N)]

def turnLeft(d):
    # 방향
    if d == 0: # 북 -> 서
        tmp = 3
    elif d == 1: # 동 -> 북
        tmp = 0
    elif d == 2: # 남 -> 동
        tmp = 1
    else:        # 서 -> 남
        tmp = 2

    return tmp
def checkBack(robot):
    if robot[2] == 0:
        return robot[0] + 1, robot[1]
    elif robot[2] == 1:
        return robot[0], robot[1] - 1
    elif robot[2] == 2:
        return robot[0] - 1, robot[1]
    else:
        return robot[0], robot[1] + 1

while True:
    # 현재 위치를 청소한다.
    answer += 1
    visited[robot[0]][robot[1]] = 1 # 방문처리
    cnt = 0
    while True:
        if cnt == 4:
            rx, ry = checkBack(robot)
            if graph[rx][ry] == 1:
                print(answer)
                
                exit()
            else:
                robot[0] = rx
                robot[1] = ry
                cnt = 0
                continue

        x, y = robot[0], robot[1]
        # 왼쪽
        d = turnLeft(robot[2])
        cnt += 1
        nx = x + dir[d][0]
        ny = y + dir[d][1]
        # 아직 청소하지 않은 공간이 존재한다면
        if visited[nx][ny] == 0 and graph[nx][ny] == 0:
            robot[0] = nx
            robot[1] = ny
            robot[2] = d
            # 1번으로 돌아간다.
            break
        else:
            robot[2] = d

