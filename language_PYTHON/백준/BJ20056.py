# 마법사 상어와 파이어볼
# 복습 횟수:3, 01:15:00, 복습필요O
import sys
si = sys.stdin.readline
N, M, K = map(int, si().split())
dir = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

graph = [[[] for i in range(N)] for i in range(N)]

for i in range(M):
    r, c, m, s, d = list(map(int, si().split()))
    graph[r-1][c-1].append([m, s, d])

def converter(x, y, s, d):
    new_x, new_y = x + dir[d][0] * s, y + dir[d][1] * s

    while new_x >= N:
        new_x = new_x - N
    while new_y >= N:
        new_y = new_y - N
    while new_x < 0:
        new_x = new_x + N
    while new_y < 0:
        new_y = new_y + N

    return new_x, new_y

for i in range(K):
    # 1. 이동하기
    new_graph = [[[] for _ in range(N)] for __ in range(N)]
    for x in range(N):
        for y in range(N):
            # 탐색 시작
            while graph[x][y]:
                m, s, d = graph[x][y].pop()
                new_x, new_y = converter(x, y, s, d)
                new_graph[new_x][new_y].append([m , s, d])
    
    # 2. 나누기
    for x in range(N):
        for y in range(N):
            # 탐색 시작
            if len(new_graph[x][y]) >= 2:
                total_m = 0
                total_s = 0
                divider = len(new_graph[x][y])
                hol = 0
                jjak = 0
                while new_graph[x][y]:
                    m, s, d = new_graph[x][y].pop()
                    total_m = total_m + m
                    total_s = total_s + s
                    
                    # 방향 설정을 위한 direction 체크
                    if (d % 2) == 1:
                        hol = 1
                    elif (d % 2) == 0:
                        jjak = 1

                # 질량이 0인 파이어볼은 소멸 된다.
                if total_m//5 <= 0: continue 

                # 모두 홀인 경우 & 모두 짝인 경우
                if (hol + jjak) == 1: 
                    # 0, 2, 4, 6
                    for ddd in range(0, 8, 2):
                        graph[x][y].append([total_m//5, total_s//divider, ddd])
                else:
                    for ddd in range(1, 8, 2):
                        graph[x][y].append([total_m//5, total_s//divider, ddd])
            # 아닌 경우
            else:
                graph[x][y] = new_graph[x][y]

answer = 0
for i in range(N):
    for j in range(N):
        while graph[i][j]:
            m, s, d = graph[i][j].pop()
            answer += m
print(answer)