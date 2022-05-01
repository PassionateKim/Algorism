##로봇 청소기

n, m = map(int, input().split())
d = [[0] * m for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y]  = 1
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
dx = [-1,0,1,0]
dy = [0,1,0,-1]

#0 위 1 오른쪽 2 아래 3 왼쪽

def turn_left():
    global direction
    direction = direction - 1
    if direction == -1:
        direction = 3
count = 1 # 현재 위치를 청소 했으므로
turn_time = 0 #회전횟수 계산 4인 경우 다른 조건 실행
flag = 0
while True:
    print("-----------")
    for i in d:
        print(i)
    flag += 1
    if flag == 60:
        break
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    
    else:
        turn_time += 1
    
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
    
    


# from collections import deque
# N, M = map(int, input().split())
# r, c, dir = map(int, input().split())
# cnt = 1

# miro = [list(map(int, input().split())) for _ in range(N)]
# visited = [[0] * M for _ in range(N)]

# def checkLeft(s_dir):
#     if s_dir == 0:
#         return 3
#     elif s_dir == 1:
#         return 0
#     elif s_dir == 2:
#         return 1
#     else:
#         return 2

# def checkBack(r,c,s_dir):
#     if s_dir == 0:
#         return r+1,c
#     elif s_dir == 1:
#         return r,c-1
#     elif s_dir == 2:
#         return r-1,c
#     else:
#         return r,c+1

# flag = 0

# def BFS(r, c, dir, continuity):
#     global cnt
#     q = deque()
#     q.append([r,c,dir,0]) #2a 연속성
#     visited[r][c] = 1 # 첫 장소 방문 체크

#     while q:
#         global flag
#         flag += 1
#         if flag == 60:
#             return
#         print(q)
        
#         r, c, s_dir, continuity = q.pop()
        
#         # 다 벽이라서 상관없음
#         if continuity == 4: # 2a가 연속으로 네 번 실행되었을 경우
#             x,y = checkBack(r,c,s_dir)
#             if miro[x][y] == 1:
#                 return
#             else:
#                 q.append([x,y,s_dir,0])
#                 # r, c, s_dir, continuity = q.pop() # 초기화
#                 continue
                

#         r_dir = checkLeft(s_dir) # 왼쪽 방향 return
        
#         if r_dir == 0: # 방향이 북쪽인 경우
#             if visited[r-1][c] == 0 and miro[r-1][c] == 0: # 방문 X 벽 X
#                 cnt += 1 # 청소했으니까
#                 visited[r-1][c] = 1  #방문처리
#                 q.append([r-1, c, r_dir, 0])
#             else:
#                 continuity += 1
#                 q.append([r, c, r_dir, continuity])

#         elif r_dir == 1: # 방향이 동쪽인 경우
#             if visited[r][c+1] == 0 and miro[r][c+1] == 0: # 방문 X 벽 X
#                 cnt += 1 # 청소했으니까
#                 visited[r][c+1] = 1  #방문처리
#                 q.append([r, c+1, r_dir, 0])
#             else:
#                 continuity += 1
#                 q.append([r, c, r_dir, continuity])

#         elif r_dir == 2: # 방향이 남쪽인 경우
#             if visited[r+1][c] == 0 and miro[r+1][c] == 0: # 방문 X 벽 X
#                 cnt += 1 # 청소했으니까
#                 visited[r+1][c] = 1  #방문처리
#                 q.append([r+1, c, r_dir, 0])
#             else:
#                 continuity += 1
#                 q.append([r, c, r_dir, continuity])   

#         else: #방향이 서쪽인 경우
#             if visited[r][c-1] == 0 and miro[r][c-1] == 0: # 방문 X 벽 X
#                 cnt += 1 # 청소했으니까
#                 visited[r][c-1] = 1  #방문처리
#                 q.append([r, c-1, r_dir, 0])
#             else:
#                 continuity += 1
#                 q.append([r, c, r_dir, continuity])
#         for i in visited:
#             print(i)
#         print("-----")


# BFS(r-1, c-1, dir, 0)
# print(cnt)