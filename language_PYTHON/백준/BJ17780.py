# 새로운 게임
# 복습 횟수:2, 01:00:00, 복습필요X
import sys
si = sys.stdin.readline 

N, K = map(int, si().split()) # chess판 크기, 말의 개수
graph_info = [list(map(int, si().split())) for i in range(N)]

horse_list = [[[] for i in range(N)] for i in range(N)]

for i in range(K):
    x, y, dir = map(int, si().split())

    horse_list[x-1][y-1].append([i+1, dir]) # 말번호, dir


answer = 0


def convertLocation(x, y, dir):
    if dir == 1:
        return x, y+1
    if dir == 2:
        return x, y-1
    if dir == 3:
        return x-1, y
    else:
        return x+1, y

def convertDir(dir):
    if dir == 1:
        return 2
    if dir == 2:
        return 1
    if dir == 3:
        return 4
    else:
        return 3
    
def check_horse(horse_number):
    for x in range(N):
        for y in range(N):
            if not horse_list[x][y]: continue

            bottom_horse = horse_list[x][y][0]
            if bottom_horse[0] == horse_number: # 아래에 있다면
                dir = bottom_horse[1]
                nx, ny = convertLocation(x, y, dir)
                # 흰, 빨, 파, 밖 구분
                if (not (0<= nx< N and 0 <= ny < N)) or graph_info[nx][ny] == 2: # 밖이거나 파란색인 경우
                    converted_dir = convertDir(dir)
                    bottom_horse[1] = converted_dir
                    # logic 다시 수행
                    nx, ny = convertLocation(x, y, converted_dir)
                    if (not (0<= nx< N and 0 <= ny < N)) or graph_info[nx][ny] == 2:
                        return

                    elif graph_info[nx][ny] == 0: # 흰색인 경우
                        horse_list[nx][ny].extend(horse_list[x][y])
                        horse_list[x][y] = []
                        return
                    
                    elif graph_info[nx][ny] == 1: # 빨간색인 경우
                        horse_list[x][y].reverse()
                        horse_list[nx][ny].extend(horse_list[x][y])
                        horse_list[x][y] = []
                        return
                    
                elif graph_info[nx][ny] == 0: # 흰색인 경우
                        horse_list[nx][ny].extend(horse_list[x][y])
                        horse_list[x][y] = []
                        return
                
                elif graph_info[nx][ny] == 1: # 빨간색인 경우
                    horse_list[x][y].reverse()
                    horse_list[nx][ny].extend(horse_list[x][y])
                    horse_list[x][y] = []
                    return

while True:
    # 탈출 조건
    if answer > 1000:
        print(-1)
        break

    flag = False
    for i in range(N):
        for j in range(N):
            if len(horse_list[i][j]) >= 4:
                print(answer)
                flag = True

    if flag:
        break
    
    for horse_number in range(1, K+1):
        # 있는지 체크
        flag = False
        check_horse(horse_number)

    answer += 1
