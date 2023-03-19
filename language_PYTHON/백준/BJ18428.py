# 감시 피하기
# 복습 횟수:0, 00:30:00, 복습필요X
import sys
from itertools import combinations
si = sys.stdin.readline
# 완탐인듯 3 <= N <= 6
N = int(si())
graph = [list(map(str, si().rstrip().split())) for _ in range(N)]

blank_list = []
teacher_list = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'X':
            blank_list.append([i, j])
        
        if graph[i][j] == 'T':
            teacher_list.append([i, j])

answer = "NO"

candidate_combi_list = list(combinations(blank_list, 3))

for candidate_combi in candidate_combi_list:
    x1, y1 = candidate_combi[0]
    x2, y2 = candidate_combi[1]
    x3, y3 = candidate_combi[2]
    
    # 장애물 설치하기
    graph[x1][y1] = 'O'
    graph[x2][y2] = 'O'
    graph[x3][y3] = 'O'

    studentFound = False
    for x, y in teacher_list:
        for idx in range(4):
            nx, ny = x, y
            while True:
                nx, ny = nx + dx[idx], ny + dy[idx]
                if not (0 <= nx < N and 0 <= ny < N): break
                if graph[nx][ny] == 'O': break # 장애물을 만나 더이상 탐색할 수 없으므로

                if graph[nx][ny] == 'S':
                    studentFound = True

    if studentFound == False:
        answer = "YES"
        break

    # 장애물 초기화
    graph[x1][y1] = 'X'
    graph[x2][y2] = 'X'
    graph[x3][y3] = 'X'

print(answer)