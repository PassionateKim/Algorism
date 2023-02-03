# 제곱수 찾기
# 복숩 횟수:0, 01:00:00, 복습필요O
import sys
si = sys.stdin.readline
N, M = map(int, si().split())

graph = []
for i in range(N):
    tmp = list(map(str, si().rstrip()))
    graph.append(tmp)

answer = -1
def sqr(S):
    S = int(S)
    return int(S ** 0.5) ** 2 == S

for i in range(N): # 시작 x 좌표
    for j in range(M): # 시작 y 좌표
        for row_d in range(-N, N):
            for col_d in range(-M, M):
                S = ""
                x, y = i, j
                if row_d == 0 and col_d == 0: continue

                while 0 <= x < N and 0 <= y < M:
                    S += graph[x][y]
                    if sqr(S):
                        answer = max(answer, int(S))
                    x += row_d
                    y += col_d
print(answer)