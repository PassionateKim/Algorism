# 쿼드트리
# 복습 횟수:1, 00:30:00, 복습필요X
import sys
si = sys.stdin.readline
N = int(si())
graph = [list(map(int, si().rstrip())) for _ in range(N)]
answer = []
def dfs(x, y, n):
    global answer

    check = graph[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != graph[i][j]:
                answer.append('(')
                dfs(x, y, n//2)
                dfs(x, y + n//2, n//2)
                dfs(x + n//2, y, n//2)
                dfs(x + n//2, y + n//2, n//2)
                answer.append(')')
                return

    if check == 0:
        answer.append(str(0))
    else:
        answer.append(str(1))

dfs(0, 0, N)
print("".join(answer))