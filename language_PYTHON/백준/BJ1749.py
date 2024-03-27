import sys
si = sys.stdin.readline 

N, M = map(int, si().split())

graph = []
prefix_sum = [[0 for i in range(M + 1)] for i in range(N + 1)]

for i in range(N):
    graph.append(list(map(int, si().split())))


for i in range(1, N + 1):
    for j in range(1, M + 1):
        prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + graph[i-1][j - 1]

answer = sys.maxsize * (-1)

for i in range(1, N + 1):
    for j in range(1, M + 1):

        for x in range(i):
            for y in range(j):
                sub_val = prefix_sum[i][j] - prefix_sum[x][j] - prefix_sum[i][y] + prefix_sum[x][y]
                answer = max(sub_val, answer)
    
print(answer)