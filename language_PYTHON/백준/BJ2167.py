import sys
si = sys.stdin.readline 

N, M = map(int, si().split())
graph = []

for i in range(N):
    graph.append(list(map(int, si().split())))

prefix_sum_list = [[0 for i in range(M + 1)] for i in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        prefix_sum_list[i][j] = graph[i-1][j-1] + prefix_sum_list[i-1][j] + prefix_sum_list[i][j-1] - prefix_sum_list[i-1][j-1]

K = int(si())
for idx in range(K):
    i, j, x, y = map(int, si().split())

    print(prefix_sum_list[x][y] - prefix_sum_list[x][j-1] - prefix_sum_list[i-1][y] + prefix_sum_list[i-1][j-1])