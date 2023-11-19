# 쿼드 트리
import sys
si = sys.stdin.readline 
N = int(si())

graph = []

for i in range(N):
    tmp = list(map(str, si().rstrip()))
    graph.append(tmp)

answer = ""
def divide_q(x, y, length):
    global answer 
    start = graph[x][y]
    for i in range(x, x + length):
        for j in range(y, y + length):
            if graph[i][j] != start:
                answer = answer + "("
                divide_q(x, y, length // 2)
                divide_q(x, y + length // 2, length // 2)
                divide_q(x + length // 2, y, length // 2)
                divide_q(x + length // 2, y + length // 2, length // 2)
                answer = answer + ")"
                return
            
    answer = answer + start
    return

divide_q(0, 0, N)
print(answer)