# 2022-07-19
# 2022-07-24
# 2022-07-26
# 마법사 상어와 파이어볼
import sys
si = sys.stdin.readline

N, M, K = map(int, si().split())
fire_ball = []
graph = [[[] for _ in range(N)] for _ in range(N)]
dir = [[-1,0], [-1,1], [0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1]]
for i in range(M):
    fire_ball.append(list(map(int, si().split())))

# fire볼 초기화
while fire_ball:
    r, c, m, s, d = fire_ball.pop()
    graph[r-1][c-1].append([m, s, d])

for i in range(K):
    # 1. 모든 파이어볼 이동
    tmp = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # 하나라도 있다면
            if len(graph[i][j]) >= 1:
                while graph[i][j]:
                    m, s, d = graph[i][j].pop()
                    nx, ny = (i + dir[d][0]*s)%N, (j + dir[d][1]*s)%N
                    tmp[nx][ny].append([m, s, d])
    # 1. 모든 파이어볼 이동

    # 2. 2개 이상이면 다음과 같은 일이 일어난다.
    # 같은 칸 모두 합침
    for i in range(N):
        for j in range(N):
            if len(tmp[i][j]) >= 2:
                amount = 0
                cnt = len(tmp[i][j])
                speed = 0
                isOdd = False
                isEven = False

                while tmp[i][j]:
                    m, s, d = tmp[i][j].pop()
                    
                    amount += m
                    speed += s
                    if d % 2 == 0:
                        isEven = True
                    else:
                        isOdd = True
                # 질량이 0인 파이어볼은 소멸 삭제
                if amount // 5 == 0: continue

                if isOdd and isEven:
                    # 파이어볼 4개 분할
                    for q in [1,3,5,7]:
                        tmp[i][j].append([amount//5, speed//cnt, q])
                else:
                    for q in [0,2,4,6]:
                        tmp[i][j].append([amount//5, speed//cnt, q])
    # 같은 칸 모두 합침
    # graph 에 옮기기
    for i in range(N):
        for j in range(N):
            graph[i][j] = tmp[i][j]
    
    # K
answer = 0
for i in range(N):
    for j in range(N):
        for fireball in graph[i][j]:
            answer += fireball[0]
print(answer)