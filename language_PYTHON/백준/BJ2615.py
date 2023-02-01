# 오목
# 복습 횟수:2, 
# 1. 바둑판 세팅
# 2. 가로 ->  , 대각 2개, 세로 아래
import sys
si = sys.stdin.readline
graph = []
for i in range(19):
    tmp = list(map(int, si().split()))
    graph.append(tmp)

for x in range(19):
    for y in range(19):
        check = graph[x][y]
        # black
        if check == 0: continue 
        # 가로 
        q = list()
        q.append([x, y]) # 좌표 저장
        rx, ry = x, y 
        lx, ly = x, y
        while 0 <= ly < 19:
            ly = ly - 1 # 좌측
            if 0 <= ly < 19 and graph[lx][ly] == check:
                q.append([lx, ly])
            else: break
        
        while 0 <= ry < 19:
            ry = ry + 1 # 우측
            if 0 <= ry < 19 and graph[rx][ry] == check:
                q.append([rx, ry])
            else: break
        
        if len(q) >= 6: continue #6알 이상인 경우는 이긴 것이 아니다
        elif len(q) == 5:
            q.sort(key=lambda x: (x[1], x[0]))
            print(check)
            print(q[0][0] + 1, q[0][1] + 1)
            exit()
        
        # 대각 위
        q = list()
        q.append([x, y])
        rx, ry = x, y
        lx, ly = x, y
        while 0 <= lx < 19 and 0 <= ly < 19: # 아래측
            lx = lx + 1
            ly = ly - 1
            if 0 <= lx < 19 and 0 <= ly < 19 and graph[lx][ly] == check:
                q.append([lx, ly])
            else: break

        while 0 <= rx < 19 and 0 <= ry < 19: # 위측
            rx = rx - 1
            ry = ry + 1 
            if 0 <= rx < 19 and 0 <= ry < 19 and graph[rx][ry] == check:
                q.append([rx, ry])       
            else: break
        
        if len(q) >= 6: continue #6알 이상인 경우는 이긴 것이 아니다
        elif len(q) == 5:
            q.sort(key=lambda x: (x[1], x[0]))
            print(check)
            print(q[0][0] + 1, q[0][1] + 1)
            exit()
        
        # 대각 아래
        q = list()
        q.append([x, y])
        rx, ry = x, y
        lx, ly = x, y

        while 0 <= lx < 19 and 0 <= ly < 19: # 아래측
            lx = lx + 1
            ly = ly + 1
            if 0 <= lx < 19 and 0 <= ly < 19 and graph[lx][ly] == check:
                q.append([lx, ly])
            else: break

        while 0 <= rx < 19 and 0 <= ry < 19: # 위측
            rx = rx - 1
            ry = ry - 1 
            if 0 <= rx < 19 and 0 <= ry < 19 and graph[rx][ry] == check:
                q.append([rx, ry])       
            else: break
        
        if len(q) >= 6: continue #6알 이상인 경우는 이긴 것이 아니다
        elif len(q) == 5:
            q.sort(key=lambda x: (x[1], x[0]))
            print(check)
            print(q[0][0] + 1, q[0][1] + 1)
            exit()
        
        # 세로
        q = list()
        q.append([x, y])
        rx, ry = x, y
        lx, ly = x, y

        while 0 <= lx < 19: # 아래측
            lx = lx + 1
            if 0 <= lx < 19 and graph[lx][ly] == check:
                q.append([lx, ly])
            else: break
        
        while 0 <= rx < 19: # 위측
            rx = rx - 1
            if 0 <= rx < 19 and graph[rx][ry] == check:
                q.append([rx, ry])
            else: break
        
        if len(q) >= 6: continue #6알 이상인 경우는 이긴 것이 아니다
        elif len(q) == 5:
            q.sort(key=lambda x: (x[1], x[0]))
            print(check)
            print(q[0][0] + 1, q[0][1] + 1)
            exit()