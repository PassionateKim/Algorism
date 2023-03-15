# 새로운 게임
# 복습 횟수:1, 00:45:00, 복습필요O
import sys
from collections import deque
si = sys.stdin.readline
N, K = map(int, si().split())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
graph = [list(map(int, si().split())) for _ in range(N)]

horse_graph = [[deque() for _ in range(N)] for _ in range(N)]

for i in range(K):
    x, y, d = list(map(int, si().split()))
    x, y, d = x - 1, y - 1, d - 1
    horse_graph[x][y].append([i, d]) # 체스 번호, 방향

def changeDir(dir):
    if dir == 0:
        return 1
    if dir == 1:
        return 0
    if dir == 2:
        return 3
    
    return 2
answer = 0
def check():
    global answer
    while True:
        if answer > 1000:
            answer = -1
            return
        
        for i in range(N):
            for j in range(N):
                if len(horse_graph[i][j]) >= 4:
                    return

        answer += 1
        

        # 체스 번호    
        for chess in range(K):
            flag = 0
            for x in range(N):
                for y in range(N):
                    horse_list = horse_graph[x][y]
                    # 맨 아래에 있는 경우에만 움직일 수 있다.
                    if len(horse_list) != 0 and horse_list[0][0] == chess:
                        dir = horse_list[0][1]
                        nx, ny = x + dx[dir], y + dy[dir]
                        # 파란색 or 밖
                        if not (0 <= nx < N and 0 <= ny < N) or graph[nx][ny] == 2:
                            horse_list[0][1] = changeDir(horse_list[0][1])
                            dir = horse_list[0][1]
                            nx, ny = x + dx[dir], y + dy[dir]
                            # 파란색인 경우
                            if not (0 <= nx < N and 0 <= ny < N) or graph[nx][ny] == 2:
                                flag = 1
                                break 
                            # 빨간색인 경우
                            if graph[nx][ny] == 1:
                                while horse_graph[x][y]:
                                    horse = horse_graph[x][y].pop()
                                    horse_graph[nx][ny].append(horse)
                                flag = 1
                                break
                            # 흰색인 경우
                            if graph[nx][ny] == 0:
                                while horse_graph[x][y]:
                                    horse = horse_graph[x][y].popleft()
                                    horse_graph[nx][ny].append(horse)
                                flag = 1
                                break

                        # 빨간색인 경우
                        if graph[nx][ny] == 1:
                            while horse_graph[x][y]:
                                horse = horse_graph[x][y].pop()
                                horse_graph[nx][ny].append(horse)
                            flag = 1
                            break
                        # 흰색인 경우
                        if graph[nx][ny] == 0:
                            while horse_graph[x][y]:
                                horse = horse_graph[x][y].popleft()
                                horse_graph[nx][ny].append(horse)
                            flag = 1
                            break
                if flag:
                    break

check()
print(answer)