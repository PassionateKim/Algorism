# 색종이 만들기
# 복습 횟수:3, 00:30:00, 복습필요X
import sys
si = sys.stdin.readline
N = int(si())
graph = [list(map(int, si().split())) for i in range(N)]

white = 0
blue = 0


def dfs(x, y, n):
    global white
    global blue

    check = graph[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if graph[i][j] != check: # 다른 경우
                dfs(x, y, n//2)
                dfs(x, y + n//2, n//2)
                dfs(x + n//2, y, n//2)
                dfs(x + n//2, y + n//2, n//2)
                return
    
    if check == 0:
        white += 1
    else:
        blue += 1

dfs(0, 0, N)

print(white)
print(blue)