# 선발 명단
# 복습 횟수:0, 00:45:00
import sys
si = sys.stdin.readline

N = int(si())

def dfs(hang, choice, visited):
    global answer
    # 탈출 조건
    if hang == 11:
        if 0 in choice:
            return
        
        # 전체의 값
        tmp = 0
        for i in range(len(choice)):
            tmp += choice[i][1]
        
        answer = max(answer, tmp)
        return
    
    for i in range(11):
        if visited[i] != 0: continue
        if graph[hang][i] == 0: continue

        choice[i] = [hang, graph[hang][i]]
        visited[i] = 1 # 방문처리
        dfs(hang+1, choice, visited)
        visited[i] = 0 # 초기화
        choice[i] = 0

    return

for i in range(N):
    # 초기화 
    
    answer = 0
    visited = [0 for i in range(11)]  
    graph = []
    for i in range(11):
        tmp = list(map(int, si().split()))
        graph.append(tmp)
    
    dfs(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], visited)
    print(answer)