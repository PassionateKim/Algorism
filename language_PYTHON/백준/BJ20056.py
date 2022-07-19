# 마법사 상어와 파이어볼
import sys
import copy
si = sys.stdin.readline

N, M, K = map(int, si().split())
# 그래프 생성
graph = [[[] for _ in range(N)] for _ in range(N)]
dir = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
# 처음 파이어볼 넣기 초기화
for i in range(M):
    r, c, m, s, d = map(int, si().split())
    graph[r-1][c-1].append([m, s, d])

# 시작
for i in range(K):
    tmp_list = [[[] for _ in range(N)] for _ in range(N)]
    # 1. 그래프 돌기
    for i in range(N):
        for j in range(N):
            # 하나 이상이면 탐색하면서, 이동시키기
            if len(graph[i][j]) >= 1:
                while graph[i][j]: 
                    m, s, d = graph[i][j].pop()
                    nx, ny = (i + dir[d][0]*s) % N, (j + dir[d][1]*s) % N # 열, 행이 연결되어 있으므로
                    # graph에 하면 영향을 줘서 안된다.
                    tmp_list[nx][ny].append([m, s, d]) # 위치 이동
    
    #2. 이동 후 2개 이상의 파이어볼이 있는지 체크
    for i in range(N):
        for j in range(N):
            amount = 0
            speed = 0
            num = len(tmp_list[i][j])
            a_odd, a_even = True, True
            if len(tmp_list[i][j]) >= 2:
                for p in tmp_list[i][j]:
                    m, s, d = p
                    # 홀짝 체크
                    if d%2 == 1:
                        a_even = False
                    else:
                        a_odd = False
                    # 질량 합, 속력 합
                    amount += m
                    speed += s
                
                tmp_list[i][j] = [] # 초기화
                
                if amount // 5 == 0: continue # 질량이 0인 파이어볼은 소멸된다.
                
                # 방향
                if a_odd or a_even:
                    for q in [0, 2, 4, 6]:
                        tmp_list[i][j].append([amount//5, speed//num, q])
                else:
                    for q in [1, 3, 5, 7]:
                        tmp_list[i][j].append([amount//5, speed//num, q])
    
    # 그래프 초기화
    for i in range(N):
        for j in range(N):
            graph[i][j] = copy.deepcopy(tmp_list[i][j])
    
answer = 0                
for hang in graph: # 3 
    for i in hang: # 2 
        for j in i: # 1
            answer += j[0]
print(answer)