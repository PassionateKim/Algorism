# 222-풀링
# 복습 횟수:0, 00:45:00, 복습필요X
import sys
si = sys.stdin.readline
N = int(si())
graph = [list(map(int, si().split())) for _ in range(N)]

def dfs(graph, n):
    if n == 1:
        print(graph[0][0])
        return

    new = []
    new_graph = []
    for i in range(0, n, 2):
        for j in range(0, n, 2):
            tmp = []
            for x in range(i, i+2):
                for y in range(j, j+2):
                    tmp.append(graph[x][y])
            tmp.sort()
            new.append(tmp[-2])
    
    cnt = 0
    check = n // 2
    tmp = []
    for val in new:
        if cnt == check:
            new_graph.append(tmp)
            tmp = []
            tmp.append(val)
            cnt = 1
        else:
            tmp.append(val)
            cnt += 1

    new_graph.append(tmp)

    dfs(new_graph, n//2)

dfs(graph, N)