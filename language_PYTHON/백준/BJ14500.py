# 테트로미노
# 1. 각각의 모양을 모두 체크해보기
import sys
si = sys.stdin.readline
N, M = map(int, si().split())
graph = []
for i in range(N):
    tmp = list(map(int, si().split()))
    graph.append(tmp)
answer = 0

# 1-1 가로 테크로미노
for i in range(N):
    for j in range(M):
        tmp = 0
        if not (0 <= j+3 < M): continue
        tmp = tmp + graph[i][j] + graph[i][j+1] + graph[i][j+2] + graph[i][j+3]
        answer = max(answer, tmp)


# 1-2 세로 테크로미노
for i in range(N):
    for j in range(M):
        tmp = 0
        if not (0 <= i+3 < N): continue
        tmp = tmp + graph[i][j] + graph[i+1][j] + graph[i+2][j] + graph[i+3][j]
        answer = max(answer, tmp)

# 2 정사각형 테크로미노
for i in range(N):
    for j in range(M):
        tmp = 0
        if not (0 <= i+1 < N): continue
        if not (0 <= j+1 < M): continue
        tmp = tmp + graph[i][j] + graph[i+1][j] + graph[i][j+1] + graph[i+1][j+1]
        answer = max(answer, tmp)

# 3-1 주황 테크로미노 기본
for i in range(N):
    for j in range(M):
        tmp = 0
        if not (0 <= i+2 < N): continue
        if not (0 <= j+1 < M): continue

        tmp = tmp + graph[i][j] + graph[i+1][j] + graph[i+2][j] + graph[i+2][j+1]
        answer = max(answer, tmp)

# 3-2 주황 테크로미노 시계방향 90도
for i in range(N):
    for j in range(M):
        tmp = 0
        if not (0 <= i+1 < N): continue
        if not (0 <= j+2 < M): continue

        tmp = tmp + graph[i][j] + graph[i][j+1] + graph[i][j+2] + graph[i+1][j]
        answer = max(answer, tmp)

# 3-3 주황 테크로미노 시계방향 180도
for i in range(N):
    for j in range(M):
        tmp = 0
        if not (0 <= i+2 < N): continue
        if not (0 <= j+1 < M): continue

        tmp = tmp + graph[i][j] + graph[i][j+1] + graph[i+1][j+1] + graph[i+2][j+1]
        answer = max(answer, tmp)

# 3-4 주황 테크로미노 시계방향 270도
for i in range(N):
    for j in range(M):
        tmp = 0
        if not (0 <= i+1 < N): continue
        if not (0 <= j+2 < M): continue

        tmp = tmp + graph[i][j+2] + graph[i+1][j] + graph[i+1][j+1] + graph[i+1][j+2]
        answer = max(answer, tmp)

# 3-5 주황 테크로미노 반전
for i in range(N):
    for j in range(M):
        tmp = 0
        if not (0 <= i+2 < N): continue
        if not (0 <= j+1 < M): continue

        tmp = tmp + graph[i][j+1] + graph[i+1][j+1] + graph[i+2][j] + graph[i+2][j+1]
        answer = max(answer, tmp)

# 3-6 주황 테크로미노 반전2
for i in range(N):
    for j in range(M):
        tmp = 0
        if not (0 <= i+1 < N): continue
        if not (0 <= j+2 < M): continue

        tmp = tmp + graph[i][j] + graph[i][j+1] + graph[i][j+2] + graph[i+1][j+2]
        answer = max(answer, tmp)

# 3-7 주황 테크로미노 반전3
for i in range(N):
    for j in range(M):
        tmp = 0
        if not (0 <= i+2 < N): continue
        if not (0 <= j+1 < M): continue

        tmp = tmp + graph[i][j] + graph[i][j+1] + graph[i+1][j] + graph[i+2][j]
        answer = max(answer, tmp)

# 3-8 주황 테크로미노 반전4
for i in range(N):
    for j in range(M):
        tmp = 0
        if not (0 <= i+1 < N): continue
        if not (0 <= j+2 < M): continue

        tmp = tmp + graph[i][j] + graph[i+1][j] + graph[i+1][j+1] + graph[i+1][j+2]
        answer = max(answer, tmp)

# 4-1 초록 테크로미노 기본
for i in range(N):
    for j in range(M):
        tmp = 0
        if not (0 <= i+2 < N): continue
        if not (0 <= j+1 < M): continue
        
        tmp = tmp + graph[i][j] + graph[i+1][j] + graph[i+1][j+1] + graph[i+2][j+1]
        answer = max(answer ,tmp)
        
# 4-1 초록 테크로미노 90
for i in range(N):
    for j in range(M):
        tmp = 0
        if not (0 <= i+1 < N): continue
        if not (0 <= j+2 < M): continue
        
        tmp = tmp + graph[i][j+1] + graph[i][j+2] + graph[i+1][j] + graph[i+1][j+1]
        answer = max(answer ,tmp)

# 4-2 초록 테크로미노 반전1
for i in range(N):
    for j in range(M):
        tmp = 0
        if not (0 <= i+2 < N): continue
        if not (0 <= j+1 < M): continue
        
        tmp = tmp + graph[i][j+1] + graph[i+1][j] + graph[i+1][j+1] + graph[i+2][j]
        answer = max(answer ,tmp)

# 4-3 초록 테크로미노 반전2
for i in range(N):
    for j in range(M):
        tmp = 0
        if not (0 <= i+1 < N): continue
        if not (0 <= j+2 < M): continue
        
        tmp = tmp + graph[i][j] + graph[i][j+1] + graph[i+1][j+1] + graph[i+1][j+2]
        answer = max(answer ,tmp)

# 5 보라 테크로미노
for i in range(N):
    for j in range(M):
        tmp = 0
        if not (0 <= i+1 < N): continue
        if not (0 <= j+2 < M): continue
        
        tmp = tmp + graph[i][j] + graph[i][j+1] + graph[i][j+2] + graph[i+1][j+1]
        answer = max(answer ,tmp)

# 5-1 보라 테크로미노 90
for i in range(N):
    for j in range(M):
        tmp = 0
        if not (0 <= i+2 < N): continue
        if not (0 <= j+1 < M): continue
        
        tmp = tmp + graph[i][j+1] + graph[i+1][j] + graph[i+1][j+1] + graph[i+2][j+1]
        answer = max(answer ,tmp)

# 5-2 보라 테크로미노 180
for i in range(N):
    for j in range(M):
        tmp = 0
        if not (0 <= i+1 < N): continue
        if not (0 <= j+2 < M): continue
        
        tmp = tmp + graph[i][j+1] + graph[i+1][j] + graph[i+1][j+1] + graph[i+1][j+2]
        answer = max(answer ,tmp)

# 5-3 보라 테크로미노 270
for i in range(N):
    for j in range(M):
        tmp = 0
        if not (0 <= i+2 < N): continue
        if not (0 <= j+1 < M): continue
        
        tmp = tmp + graph[i][j] + graph[i+1][j] + graph[i+1][j+1] + graph[i+2][j]
        answer = max(answer ,tmp)

print(answer)