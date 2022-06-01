# 주사위 굴리기
from collections import deque
import sys
input = sys.stdin.readline
# 상 뒤 동 서 앞 하 = 아래
dice = [0]+[0,0,0,0,0,0]
N, M, x , y, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
command_list = deque(map(int,input().split()))

nx, ny = x, y
while command_list:

    command = command_list.popleft()
    # 동쪽
    if command == 1:
        if 0 <= nx < N and 0 <= ny+1 < M:
            nx, ny = nx, ny+1
            tmp_bottom, tmp_east, tmp_top, tmp_west, tmp_front, tmp_back = dice[6], dice[3], dice[1], dice[4], dice[5], dice[2]
            
            dice[1] = tmp_west
            dice[2] = tmp_back
            dice[3] = tmp_top
            dice[4] = tmp_bottom
            dice[5] = tmp_front
            dice[6] = tmp_east
            #이동한 칸에 쓰여 있는 수가 0이면
            if graph[nx][ny] == 0:
                #  주사위의 바닥면에 쓰여 있는 수가 칸에 복사
                graph[nx][ny] = dice[6] 
            else:
                # 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사
                dice[6] = graph[nx][ny]
                graph[nx][ny] = 0 # 칸에 쓰여 있는 수는 0이 된다.
            print(dice[1])
    # 서쪽
    elif command == 2:
        if 0 <= nx < N and 0 <= ny-1 < M:
            nx, ny = nx, ny-1
            tmp_bottom, tmp_east, tmp_top, tmp_west, tmp_front, tmp_back = dice[6], dice[3], dice[1], dice[4], dice[5], dice[2]
            dice[1] = tmp_east
            dice[2] = tmp_back
            dice[3] = tmp_bottom
            dice[4] = tmp_top
            dice[5] = tmp_front
            dice[6] = tmp_west
             #이동한 칸에 쓰여 있는 수가 0이면
            if graph[nx][ny] == 0:
                #  주사위의 바닥면에 쓰여 있는 수가 칸에 복사
                graph[nx][ny] = dice[6]
            else:
                # 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사
                dice[6] = graph[nx][ny]
                graph[nx][ny] = 0 # 칸에 쓰여 있는 수는 0이 된다.
            print(dice[1])
    # 북쪽
    elif command == 3:
        if 0 <= nx-1 < N and 0 <= ny < M:
            nx, ny = nx-1, ny
            tmp_bottom, tmp_east, tmp_top, tmp_west, tmp_front, tmp_back = dice[6], dice[3], dice[1], dice[4], dice[5], dice[2]
            dice[1] = tmp_front
            dice[2] = tmp_top
            dice[3] = tmp_east
            dice[4] = tmp_west
            dice[5] = tmp_bottom
            dice[6] = tmp_back
            #이동한 칸에 쓰여 있는 수가 0이면
            if graph[nx][ny] == 0:
                #  주사위의 바닥면에 쓰여 있는 수가 칸에 복사
                graph[nx][ny] = dice[6]
            else:
                # 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사
                dice[6] = graph[nx][ny]
                graph[nx][ny] = 0 # 칸에 쓰여 있는 수는 0이 된다.
            print(dice[1])
    # 남쪽
    else:
        if 0 <= nx+1 < N and 0 <= ny < M:
            nx, ny = nx+1, ny
            tmp_bottom, tmp_east, tmp_top, tmp_west, tmp_front, tmp_back = dice[6], dice[3], dice[1], dice[4], dice[5], dice[2]
            dice[1] = tmp_back
            dice[2] = tmp_bottom
            dice[3] = tmp_east
            dice[4] = tmp_west
            dice[5] = tmp_top
            dice[6] = tmp_front 
            #이동한 칸에 쓰여 있는 수가 0이면
            if graph[nx][ny] == 0:
                #  주사위의 바닥면에 쓰여 있는 수가 칸에 복사
                graph[nx][ny] = dice[6]
            else:
                # 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사
                dice[6] = graph[nx][ny]
                graph[nx][ny] = 0 # 칸에 쓰여 있는 수는 0이 된다.
            print(dice[1])