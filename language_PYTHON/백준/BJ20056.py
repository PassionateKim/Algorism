# 마법사 상어와 파이어볼
import sys
si = sys.stdin.readline
#크기 # 개수 # 명령 수
N, M, K = map(int, si().split())
graph = [[[] for _ in range(N)] for _ in range(N)] # 원소로 배열을 담을 것이다. 
dir = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

# 파이어볼 위치 처음 초기화
for i in range(M):
    r, c, m, s, d = map(int, si().split())
    graph[r-1][c-1].append([m, s, d])


for i in range(K):
    # 1. 파이어볼 위치 체크 반드시 계속 초기화 해주어야함
    tmp_list = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if len(graph[i][j]) >= 1: # 하나이상 있는지 확인하기
                # 원소를 완전탐색하고, 이동시키기
                for fireball in graph[i][j]:
                    m, s, d = fireball[0], fireball[1], fireball[2]
                    nx, ny = (i + dir[d][0]*s)%N, (j + dir[d][1]*s)%N
                    tmp_list[nx][ny].append([m, s, d]) 
    
    # for i in tmp_list:
    #     print(i)
    #2. 이동이 끝 난뒤~ 
    for i in range(N):
        for j in range(N):
            # 2개 이상에서는 다음과 같은 일이 일어난다.
            if len(tmp_list[i][j])>= 2:  
                isEven, isOdd = True, True
                amount, speed, count = 0, 0, len(tmp_list[i][j])

                while tmp_list[i][j]: # 원소에 있는거 완전탐색
                    m, s, d = tmp_list[i][j].pop()
                    # 질량, 속력 더하기
                    amount += m 
                    speed += s
                    # 홀짝 구분
                    if d%2 == 0: # 짝
                        isOdd = False
                    else: # 홀
                        isEven = False
                # 질량이 0인 파이어볼은 소멸되어 없어진다.
                if amount//5 == 0: continue
                
                if isOdd or isEven: #모두 홀수이거나 모두 짝수이면
                    for ddd in [0, 2, 4, 6]:
                        tmp_list[i][j].append([amount//5, speed//count, ddd])
                else:
                    for ddd in [1, 3, 5, 7]:
                        tmp_list[i][j].append([amount//5, speed//count, ddd])

    
    for i in range(N):
        for j in range(N):
            graph[i][j] = tmp_list[i][j]
answer = 0
for i in graph:
    for j in i:
        for k in j:
            answer += k[0]
print(answer)                            
                    
                    


                    