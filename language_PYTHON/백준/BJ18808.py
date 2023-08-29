# 스티커 붙이기
# 복습 횟수:2, 01:30:00, 복습필요X
import sys
si = sys.stdin.readline 
N, M, T = map(int, si().split())

graph = []

for i in range(N):
    tmp = [0 for i in range(M)]
    graph.append(tmp)

def attach_sticker_ok_and_attach(sticker):
    # 알맞은 위치 찾기
    for i in range(N):
        for j in range(M):
            isOk = True
            for x in range(len(sticker)):
                for y in range(len(sticker[0])):
                    # 1. 범위밖을 벗어나는 경우
                    if not (0 <= x + i < N and 0 <= y + j < M): 
                        isOk = False
                        continue
                    # 2. 이미 스티커가 붙어있는 경우
                    if sticker[x][y] == 1 and graph[x + i][y + j] == 1: 
                        isOk = False
            # 조건에 맞으면 붙인다.        
            if isOk:
                for x in range(len(sticker)):
                    for y in range(len(sticker[0])):
                        if graph[x + i][y + j] == 1: continue # 삭제되는 것 예방

                        graph[x + i][y + j] = sticker[x][y]

                return True

    return False

def lotate(sticker):
    tmp = [[0 for i in range(len(sticker))] for i in range(len(sticker[0]))] # ex) 2 x 5 -> 5 x 2

    for i in range(len(sticker[0])): # 0 -> 1 -> 2 -> 3 -> 4
        for j in range(len(sticker) - 1, -1, -1): # 1 -> 0
            tmp[i][len(sticker) - 1 - j] = sticker[j][i]

    return tmp

def init_shape(sticker):

    for i in range(4): # 0, 90, 180, 270
        # 스티커를 붙일 수 있는지 체크

        if attach_sticker_ok_and_attach(sticker):
            return
        # 붙이지 못한다면 lotate()
        else:
            sticker = lotate(sticker)

    return

for _ in range(T):
    height, width = map(int, si().split())
    sticker = []
    for i in range(height):
        tmp = list(map(int, si().split()))
        sticker.append(tmp)

    init_shape(sticker)

answer = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            answer += 1

print(answer)