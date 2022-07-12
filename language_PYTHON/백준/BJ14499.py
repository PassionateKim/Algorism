# 주사위 굴리기
import sys
si = sys.stdin.readline

N, M, x, y, k = map(int, si().split())
# 위 뒤 동 서 앞 밑
dice = [0] + [0, 0, 0, 0, 0, 0]
dir = [(-1,0), (1,0), (0,-1), (0,1)]
graph = []
for i in range(N):
    graph.append(list(map(int , si().split())))
cmd_list = list(map(int, si().split()))

def move_init_dice(cmd):
    global x, y, flag
    
    top = dice[1]
    back = dice[2]
    east = dice[3]
    west = dice[4]
    front = dice[5]
    bottom = dice[6]
    
    if cmd == 1: # 동쪽
        x, y = x + dir[3][0], y + dir[3][1]
        
        if not (0<=x<N and 0<=y<M):
            x -= dir[3][0] # 원위치
            y -= dir[3][1] 
            flag = 1 # 해당 명령 무시를 위해 저장
            return  # 범위 밖은 동작 X
        # 초기화
        dice[1] = west
        dice[2] = back
        dice[3] = top
        dice[4] = bottom
        dice[5] = front
        dice[6] = east
        return
    

    elif cmd == 2: # 서쪽
        x, y = x + dir[2][0], y + dir[2][1]
        
        if not (0<=x<N and 0<=y<M):
            x -= dir[2][0] # 원위치
            y -= dir[2][1] 
            flag = 1 # 해당 명령 무시를 위해 저장
            return  # 범위 밖은 동작 X
        # 초기화
        dice[1] = east
        dice[2] = back
        dice[3] = bottom
        dice[4] = top
        dice[5] = front
        dice[6] = west
        return
    
    
    elif cmd == 3: # 북쪽
        x, y = x + dir[0][0], y + dir[0][1]
        
        if not (0<=x<N and 0<=y<M):
            x -= dir[0][0] # 원위치
            y -= dir[0][1] 
            flag = 1 # 해당 명령 무시를 위해 저장
            return  # 범위 밖은 동작 X
        # 초기화
        dice[1] = front
        dice[2] = top
        dice[3] = east
        dice[4] = west
        dice[5] = bottom
        dice[6] = back
        return
    
    
    else: # 남쪽
        x, y = x + dir[1][0], y + dir[1][1]
        
        if not (0<=x<N and 0<=y<M):
            x -= dir[1][0] # 원위치
            y -= dir[1][1] 
            flag = 1 # 해당 명령 무시를 위해 저장
            return  # 범위 밖은 동작 X
        # 초기화
        dice[1] = back
        dice[2] = bottom
        dice[3] = east
        dice[4] = west
        dice[5] = top
        dice[6] = front
        return

for cmd in cmd_list:
    flag = 0
    move_init_dice(cmd)
    
    if flag == 1: continue # 출력 무시

    if graph[x][y] == 0:
        graph[x][y] = dice[6]
    else:
        dice[6] = graph[x][y] # 칸에 쓰인 수가 바닥면으로 복사
        graph[x][y] = 0 # 칸에 쓰여 있는 수는 0이 된다.
    # 출력
    print(dice[1])

