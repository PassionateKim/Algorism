# 마법사 상어와 파이어볼
import sys
si = sys.stdin.readline
dir = [[-1,0], [-1,1], [0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1]]
fire_ball = []
N, M, K = map(int, si().split())
graph = [[[] for _ in range(N)] for _ in range(N)]

for i in range(M):
    fire_ball.append(list(map(int, si().split())))

for fb in fire_ball:
    r, c, m, s, d = fb
    graph[r-1][c-1].append([m, s, d]) 

# 파이어볼 시작
for i in range(K):
    tmp = [[[] for _  in range(N)] for _ in range(N)]

    # 파이어볼 이동시키기
    for i in range(N):
        for j in range(N):
            if len(graph[i][j]) >= 1: # 하나라도 있는 경우는 체크해야지
                while graph[i][j]:
                    m, s, d = graph[i][j].pop()
                    
                    nx, ny = (i + dir[d][0]*s) % N, (j + dir[d][1]*s) % N
                    tmp[nx][ny].append([m, s, d])
    # 파이어볼 이동시키기

    # 2. 파이어볼 2개 이상인지 체크 후 로직
    for i in range(N):
        for j in range(N):
            if len(tmp[i][j]) >= 2:
                amount = 0
                speed = 0
                cnt = len(tmp[i][j])
                Odd = True
                Even = True
                # 2.1 탐색하며 질량, 속력, 짝홀 체크하기
                while tmp[i][j]:
                    m, s, d = tmp[i][j].pop()
                    amount += m
                    speed += s
                    if d % 2 == 0:
                        Even = False # False means found Even
                    else:
                        Odd = False
                # 2.1 end
                # 질량이 0인 파이어볼은 소멸한다.
                if amount // 5 == 0: continue

                # 2.2 파이어볼 나눠서 초기화
                if Even or Odd: # 모두 홀수거나 짝수이면
                    for q in [0,2,4,6]:
                        tmp[i][j].append([amount//5, speed//cnt, q])
                else:
                    for q in [1,3,5,7]:
                        tmp[i][j].append([amount//5, speed//cnt, q])
                # 2.2 end
    
    # 2.3 graph로 초기화
    for i in range(N):
        for j in range(N):
            graph[i][j] = tmp[i][j]
    
    # 2 end

# 질량의 합 구하기
answer = 0
for i in range(N):
    for j in range(N):
        for k in graph[i][j]:
            answer += k[0]
print(answer)

                
    
              

                





    