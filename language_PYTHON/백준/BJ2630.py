# 색종이 만들기
import sys
si = sys.stdin.readline

N = int(si())

graph = []
# graph 생성하기
for i in range(N):
    tmp = list(map(int, si().split()))
    graph.append(tmp)
white, blue = 0, 0

def dfs(x, y, n):
    global white, blue

    check_point = graph[x][y]
    
    for i in range(x, x + n):
        for j in range(y, y + n):
            # 다르면 분할 정복
            if graph[i][j] != check_point:
                dfs(x, y, n//2)
                dfs(x, y + n//2, n//2)
                dfs(x + n//2, y, n//2)
                dfs(x + n//2, y + n//2, n//2)
                return

    if check_point == 0:
        white += 1
    else:
        blue += 1

dfs(0, 0, N)

print(white)
print(blue)