# 드래곤 커브
import sys
from collections import deque
si = sys.stdin.readline

N = int(si())
dragon_curve = deque(list(map(int, si().split())) for _ in range(N))
graph = [[0 for _ in range(101)] for _ in range(101)]

while dragon_curve:
    y, x, d, g = dragon_curve.popleft() # 기존 그래프 탐색처럼하기 위해 x,y 반대로
    

    arr = [[x, y]]
    # 0 세대는 미리 초기화
    if d == 0:
        arr.append([x, y+1])
    elif d == 1:
        arr.append([x-1, y])
    elif d == 2:
        arr.append([x, y-1])
    else:
        arr.append([x+1, y])

    # 1세대 부터 탐색 시작
    for i in range(1, g+1):
        arr2 = []
        arr2.extend(arr) # arr2 초기화

        # arr을 역순으로 탐색 시작
        arr_x, arr_y = arr.pop() # arr의 기준점
        while arr:
            check_x, check_y = arr.pop() # 기준점의 직전을 탐색
            diff_x, diff_y = arr_x - check_x, arr_y - check_y
            
            if diff_y > 0 or diff_y < 0:
                diff_y = diff_y * (-1)
            elif diff_x > 0 or diff_x < 0:
                pass # 바뀌지 않음
            
            # 90도 회전이므로 x, y 좌표 바꾸기
            diff_x, diff_y = diff_y, diff_x
            new_x, new_y = arr2[-1][0] + diff_x, arr2[-1][1] + diff_y
            arr2.append([new_x, new_y])

            # arr의 기준점 바꿔주기
            arr_x, arr_y = check_x, check_y 
        # arr2가 이제 arr로 기준세대로 바뀐다.
        arr.extend(arr2) 

    # 하나의 dragon_curve 탐색 끝
    while arr:
        x, y = arr.pop()
        graph[x][y] = 1 # dragon_curve가 있는 위치를 1로 저장한다.

# 오른쪽, 아래, 대각선 오른쪽 아래
dir = [[0,1], [1,0], [1,1]]
answer = 0
# 사각형이고 이중 for문으로 탐색하는 것이므로 범위를 100까지만
for i in range(100):
    for j in range(100):
        if graph[i][j] == 1: # 1이라면 탐색해볼 가치가 있으므로
            cnt = 1 
            for idx in range(3):
                nx, ny = i + dir[idx][0], j + dir[idx][1]
                if graph[nx][ny] == 1:
                    cnt += 1
            # cnt == 4로 사각형을 만족하는 경우
            if cnt == 4:
                answer += 1 
print(answer)
