import sys
si = sys.stdin.readline 
N = int(si())

graph = [[0 for i in range(101)] for i in range(101)]

for i in range(N):
    x, y = map(int, si().split())

    for z in range(x, x + 10):
        for k in range(y, y + 10):
            graph[z][k] = 1 # 색종이가 있는 부분

for i in range(100):
    for j in range(101):
        if graph[i][j] != 0 and graph[i+1][j] != 0:
            graph[i+1][j] = graph[i][j] + 1

answer = 0
for i in range(101):
    for j in range(101):
        h = 100
        for k in range(j, 101):
            h = min(h, graph[i][k])

            if h == 0:
                break

            answer = max(answer, h * (k - j + 1))

print(answer)