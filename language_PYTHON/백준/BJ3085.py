# 사탕 게임
import sys
si = sys.stdin.readline
N = int(si())

# 아래, 오른쪽
dx = [1, 0]
dy = [0, 1]
graph = []
answer = 0

for i in range(N):
    tmp = list(map(str, si().rstrip()))
    graph.append(tmp)

# 완전 탐색
for x in range(N):
    for y in range(N):
        # 2가지 방향에 대해서
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < N and 0 <= ny < N): continue
            if graph[x][y] == graph[nx][ny]: continue

            # swap
            tmp = graph[x][y]
            graph[x][y] = graph[nx][ny]
            graph[nx][ny] = tmp

            # 행 체크
            for i2 in range(N):

                tmp, idx = 1, 1
                before = graph[i2][0]
                while True:
                    # 탈출 조건
                    if idx == (N):
                        break
                    # 같다면
                    if before == graph[i2][idx]:
                        tmp += 1
                    else:
                        answer = max(answer, tmp)
                        # 초기화
                        before = graph[i2][idx]
                        tmp = 1

                    idx = idx + 1
                
                answer = max(answer, tmp)

            # 열 체크
            for i3 in range(N):
                tmp, idx = 1, 1
                before = graph[0][i3]
                while True:
                    # 탈출 조건
                    if idx == (N):
                        break
                    # 같다면
                    if before == graph[idx][i3]:
                        tmp += 1
                    else:
                        answer = max(answer, tmp)
                        # 초기화
                        before = graph[idx][i3]
                        tmp = 1

                    idx = idx + 1
                
                answer = max(answer, tmp)

            # swap (원상 복귀)
            tmp = graph[x][y]
            graph[x][y] = graph[nx][ny]
            graph[nx][ny] = tmp
            
print(answer)