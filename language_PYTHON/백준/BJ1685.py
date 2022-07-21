# 드래곤 커브
import sys
from collections import deque
si = sys.stdin.readline

N = int(si())
graph = [[0 for _ in range(101)] for _ in range(101)]
dragon_curve = []

for i in range(N):
    dragon_curve.append(list(map(int, si().split())))

answer = list()
while dragon_curve:
    y, x, d, g = dragon_curve.pop() # x, y 반대로
    # y,x,d,g = 2, 7, 3, 4
    arr = deque([[x, y]]) 
    # 0 세대는 초기화
    if d == 0: # y좌표 증가
        arr.append([x, y+1]) 
    elif d == 1: # x좌표 감소
        arr.append([x-1, y])
    elif d == 2: # y좌표 감소
        arr.append([x, y-1])
    else:        # x좌표 증가
        arr.append([x+1, y])

    #end 찾아 넣기
    for i in range(1, g+1):  
        arr2 = deque()
        arr2.extend(arr) 
        end_x, end_y = arr.pop() #[1,3]
        while arr:
            rx, ry = arr[-1] #[1,4]
            
            df_x, df_y = end_x - rx, end_y - ry # 마지막 점과 차이
            
            if df_x < 0: # x가 감소하는 방향
                pass # 그대로
            elif df_x > 0: # x가 증가하는 방향
                pass # 그대로
            elif df_y < 0: # y가 감소하는 방향
                df_y = (-1) * df_y
            else: # y가 증가하는 방향
                df_y = (-1) * df_y
            
            df_x, df_y = df_y, df_x # 90도 회전
            
            new_x, new_y = arr2[-1][0] + df_x, arr2[-1][1] + df_y 


            arr2.append([new_x, new_y])
            end_x, end_y = arr.pop()
            
        
        arr.extend(arr2) # arr2 -> arr 배열 재사용

    while arr:
        answer.append(arr.pop())   
    

    for val in answer:
        x, y = val[0], val[1]
        graph[x][y] = 1
    
res = 0
dir = [(0, 1), (1, 0), (1,1)]

for i in range(100):
    for j in range(100):
        if graph[i][j] == 1:
            cnt = 1
            for k in range(3):
                nx, ny = i + dir[k][0], j + dir[k][1]
                if graph[nx][ny] == 1:
                    cnt += 1 # 개수 올리기
            
            if cnt == 4:
                res += 1


print(res)            