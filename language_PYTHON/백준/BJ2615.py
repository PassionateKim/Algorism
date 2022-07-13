# 오목
from calendar import c
import sys
si = sys.stdin.readline

graph = []
for i in range(19):
    graph.append(list(map(int, si().split())))
# <-
dir = [(0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1)]
answer = 0
omok = []

def checkOmok(x, y):
    global answer
    color = graph[x][y]
    for i in range(8):
        cnt = 1
        omok.append((x, y))
        nx, ny = x, y
        while True:
            nx += dir[i][0]
            ny += dir[i][1]
            if not (0<=nx<19 and 0<=ny<19): 
                omok.clear()
                break

            if graph[nx][ny] == color: # 흰 오목이라면
                omok.append((nx, ny))
                cnt += 1
            else:
                omok.clear()
                break

            # 탈출 조건 딱 5개라면
            if cnt == 5:
                fnx, fny = nx + dir[i][0], ny + dir[i][1] 
                bnx, bny = x - dir[i][0], y - dir[i][1] 
                if (0<=fnx<19 and 0<=fny<19 and graph[fnx][fny] == color):
                    break
                if (0<=bnx<19 and 0<=bny<19 and graph[bnx][bny] == color):
                    break
                answer = color
                print(answer)
                omok.sort(key=lambda x: (x[1], x[0]))
                print(omok[0][0]+1, omok[0][1]+1)
                sys.exit(0)          
                # else:
                #     omok.clear()
                #     break
                
    return

# 완전 탐색
def check():
    global answer
    for i in range(19):
        for j in range(19):
            if graph[i][j] != 0: 
                checkOmok(i, j)
            
    return
check()
print(0)