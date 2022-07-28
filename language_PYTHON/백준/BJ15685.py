# 2022-07-22
# 2022-07-28
# 드래곤 커브
import sys
si = sys.stdin.readline

N = int(si())
graph = [[0 for _ in range(101)] for _ in range(101)]
dragon_li = [list(map(int, si().split())) for _ in range(N)]
dir = [(0,1), (-1,0), (0,-1), (1,0)]

while dragon_li:
    y, x, d, g = dragon_li.pop() # 기존 그래프문제처럼 x, y 좌표를 둔다
    arr = [[x,y]]
    # 0 세대
    if d == 0:
        arr.append([x, y+1])
    elif d == 1:
        arr.append([x-1,y])
    elif d == 2:
        arr.append([x, y-1])
    else:
        arr.append([x+1,y])
    
    # 1세대 ~ g세대
    for i in range(1, g+1):
        arr2 = []
        arr2.extend(arr) # arr 초기화

        end_x, end_y = arr.pop()
        
        while arr:
            cx, cy = arr.pop()
            dx, dy = end_x - cx, end_y - cy
            
            if dy != 0:
                dy = -dy
            if dx != 0:
                pass

            dx, dy = dy, dx # 바꾸기
            new_x, new_y = arr2[-1][0] + dx, arr2[-1][1] + dy
            arr2.append([new_x, new_y])
            # end_x, end_y 바꿔주기
            end_x, end_y = cx, cy
        #/arr
        arr.extend(arr2) # arr 초기화

    #/1세대 ~ g세대
    while arr:
        x, y = arr.pop()
        graph[x][y] = 1 # 체크

#/dragon_li
answer = 0
dir2 = [(0,1), (1,0), (1,1)]
for i in range(100):
    for j in range(100):
        if graph[i][j] == 1:
            cnt = 1
            for z in range(3):
                nx, ny = i + dir2[z][0], j + dir2[z][1]
                if graph[nx][ny] == 1:
                    cnt += 1
            if cnt == 4:
                answer += 1
print(answer)
            


