# 게리맨더링 2
# 복습 횟수:0, 02:30:00, 복습필요O
import sys
si = sys.stdin.readline
N = int(si())
graph = []
for i in range(N):
    graph.append(list(map(int, si().split())))

case_list = []
answer = sys.maxsize
# case 구하기
for d1 in range(1, N-1):
    for d2 in range(1, N-1):
        if d1+d2 >= N: continue
        for x in range(1, N - (d1+d2) + 1):
            x = x -1 # index 0부터 시작이므로
            for y in range(1+d1, N - d2 + 1):
                y = y - 1 # index 0부터 시작이므로
                case_list.append([d1, d2, x, y])

for d1, d2, x, y in case_list:
    visited = [[0 for i in range(N)] for i in range(N)]

    # 경계선 먼저 지정하기
    # 1.
    j = y
    for i in range(x, x+d1+1):
        visited[i][j] = 5
        j = j - 1
    # 2.
    j = y
    for i in range(x, x+d2+1):
        visited[i][j] = 5
        j = j + 1
    # 3.
    j = y-d1
    for i in range(x+d1, x+d1+d2+1):
        visited[i][j] = 5
        j = j + 1 
    # 4.
    j = y+d2
    for i in range(x+d2, x+d2+d1+1):
        visited[i][j] = 5
        j = j - 1
    
    # 구역 나누기
    # 1번 선거구
    for r in range(0, x+d1):
        for c in range(0, y+1):
            if visited[r][c] == 5: break

            visited[r][c] = 1
    # 2번 선거구
    for r in range(0, x+d2+1):
        for c in range(N-1, y, -1):
            if visited[r][c] == 5: break

            visited[r][c] = 2
    # 3번 선거구
    for r in range(x+d1, N):
        for c in range(y-d1+d2):
            if visited[r][c] == 5: break

            visited[r][c] = 3 
    # 4번 선거구
    for r in range(x+d2+1, N):
        for c in range(N-1, y-d1+d2-1, -1):
            if visited[r][c] == 5: break

            visited[r][c] = 4

    sumi1, sumi2, sumi3, sumi4, sumi5 = 0, 0, 0, 0, 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1:
                sumi1 += graph[i][j]
            elif visited[i][j] == 2:
                sumi2 += graph[i][j]
            elif visited[i][j] == 3:
                sumi3 += graph[i][j]
            elif visited[i][j] == 4:
                sumi4 += graph[i][j]
            else: 
                sumi5 += graph[i][j]
    maxi = max(sumi1, sumi2, sumi3, sumi4, sumi5)
    mini = min(sumi1, sumi2, sumi3, sumi4, sumi5)

    answer = min(answer, maxi - mini)

print(answer)