import sys 
si = sys.stdin.readline 

N = int(si())
color_paper_list = []

for i in range(N):
    color_paper_list.append(list(map(int, si().split())))

graph = [[0 for i in range(101)] for i in range(101)] # 이따가 101으로 바꿔야함

for i in range(len(graph)):
    for j in range(len(graph)):

        for x, y in color_paper_list:
            if (x <= i <= x + 10 - 1) and (y <= j <= y + 10 - 1):
                graph[i][j] = 1 
                break

for i in range(len(graph) - 1):
    for j in range(len(graph)):
        if graph[i][j] != 0 and graph[i+1][j] != 0: 
            graph[i+1][j] = graph[i][j] + 1

answer = 0
for i in range(len(graph)):
    for j in range(len(graph)):
        h = 100
        for k in range(j, len(graph)):
            h = min(graph[i][k], h)

            if h == 0:
                break

            answer = max(answer, h * (k - j + 1))

print(answer)