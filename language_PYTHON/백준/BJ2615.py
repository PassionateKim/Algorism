# 오목
import sys
si = sys.stdin.readline

graph = []
for i in range(19):
    graph.append(list(map(int, si().split())))
# <-
dir = [(0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1)]
answer = 0
omok = []

def checkWhite(x, y):
    global answer
    
    for i in range(8):
        cnt = 1
        omok.append((x, y))
        nx, ny = x, y
        while True:
            nx += dir[i][0]
            ny += dir[i][1]
            if not (0<=nx<19 and 0<=ny<19): break

            if graph[nx][ny] == 1: # 흰 오목이라면
                omok.append((nx, ny))
                cnt += 1
            else:
                omok.clear()
                break

            # 탈출 조건 딱 5개라면
            if cnt == 5:
                fnx, fny = nx + dir[i][0], ny + dir[i][1] 
                bnx, bny = x - dir[i][0], y - dir[i][1] 

                if (0<= fnx <19 and 0<= fny <19) and graph[fnx][fny] != 1:
                    if ((0<=bnx<19 and 0<=bny<19) and graph[bnx][bny] != 1) or not (0<=bnx<19 and 0<=bny<19):
                        answer = 1 # 1로 지정
                        return  
                elif not (0<= fnx <19 and 0<= fny < 19): # 앞에 인덱스 아웃인 경우
                    if ((0<=bnx<19 and 0<=bny<19) and graph[bnx][bny] != 1) or not (0<=bnx<19 and 0<=bny<19):
                        answer = 1 # 1로 지정
                        return
                else:
                    omok.clear()
                    break
                
    return

def checkBlack(x, y):
    global answer
    
    for i in range(8):
        cnt = 1
        omok.append((x, y))
        nx, ny = x, y
        while True:
            nx += dir[i][0]
            ny += dir[i][1]
            if not (0<=nx<19 and 0<=ny<19): break

            if graph[nx][ny] == 2: # 검은 오목이라면
                omok.append((nx, ny))
                cnt += 1
            else:
                omok.clear()
                break

            # 탈출 조건 딱 5개라면
            if cnt == 5:
                fnx, fny = nx + dir[i][0], ny + dir[i][1] 
                bnx, bny = x - dir[i][0], y - dir[i][1] 

                if (0<= fnx <19 and 0<= fny <19) and graph[fnx][fny] != 2:
                    if ((0<=bnx<19 and 0<=bny<19) and graph[bnx][bny] != 2) or not (0<=bnx<19 and 0<=bny<19):
                        answer = 2 # 2로 지정
                        return  
                elif not (0<= fnx <19 and 0<= fny < 19): # 앞에 인덱스 아웃인 경우
                    if ((0<=bnx<19 and 0<=bny<19) and graph[bnx][bny] != 2) or not (0<=bnx<19 and 0<=bny<19):
                        answer = 2 # 2로 지정
                        return
                else:
                    omok.clear()
                    break
                
    return

# 완전 탐색
def check():
    global answer
    for i in range(19):
        for j in range(19):
            
            if graph[i][j] == 1: # 흰색
                checkWhite(i, j)
            elif graph[i][j] == 2: # 검은색
                checkBlack(i, j)
            
            if answer != 0:
                return
    return

check()
print(answer)
omok.sort(key=lambda x: (x[1], x[0]))
# 만약 승부가 결정된 경우
if answer != 0:
    print(omok[0][0] + 1, omok[0][1] + 1)