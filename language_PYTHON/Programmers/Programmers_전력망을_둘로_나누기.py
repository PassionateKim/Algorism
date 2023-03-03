# 복습 횟수:1, 00:45:00, 복습필요X
from copy import deepcopy
def dfs(start, graph, visited, cnt):
    visited[start] = cnt

    for val in graph[start]:
        if visited[val] == 0:
            dfs(val, graph, visited, cnt)

    return

def solution(n, wires):
    global answer
    answer = 1e10
    
    for i in range(len(wires)):
        tmp = deepcopy(wires[i])
        wires[i] = 0
        visited = [0 for _ in range(n + 1)]
        graph = [[] for i in range(n + 1)]
        
        for wire in wires:
            if wire == 0: continue

            x, y = wire
            graph[x].append(y)
            graph[y].append(x)

        cnt = 1
        for start in range(1, n+1):
            if visited[start] == 0:
                dfs(start, graph, visited, cnt)
                cnt += 1
    
        wires[i] = tmp

        if max(visited) == 2:
            diff = abs(visited.count(1) - visited.count(2))
            answer = min(answer, diff)

    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))