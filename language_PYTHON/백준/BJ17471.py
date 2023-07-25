# 게리맨더링
# 복습 횟수:1, 01:00:00, 복습필요O
import sys
from itertools import combinations 
from collections import deque
si = sys.stdin.readline 

N = int(si())
population_list = [-1] + list(map(int, si().split()))
graph = [[] for i in range(N+1)]

for i in range(N):
    relation = list(map(int, si().split()))
    graph[i+1] = relation[1:]


answer = sys.maxsize

def bfs(home, away):
    start = home[0]
    visited[start] = 1
    q = deque()
    q.append(start)

    while q:
        start = q.popleft()
        for v in graph[start]:
            if visited[v] != 0:continue
            if v in home and v not in away:
                visited[v] = 1 # home 방문처리
                q.append(v)
        
    start = away[0]
    visited[start] = 2 
    q = deque()
    q.append(start)

    while q:
        start = q.popleft()
        for v in graph[start]:
            if visited[v] != 0:continue
            if v in away and v not in home:
                visited[v] = 2 # away 방문처리
                q.append(v)

    return

for i in range(1, N):
    combi_list = list(combinations(range(1, N+1), i))
    for combi in combi_list:
        home = list(combi)
        away = [i for i in range(1, N+1) if i not in home]
        
        visited = [0 for i in range(N+1)]
        bfs(home, away)

        if visited.count(0) < 2:
            home_sum = 0
            away_sum = 0
            for i in range(1, N+1):
                if visited[i] == 1:
                    home_sum += population_list[i]
                
                if visited[i] == 2:
                    away_sum += population_list[i]
        
            diff = abs(home_sum - away_sum)
            answer = min(diff, answer)

if answer == sys.maxsize:
    print(-1)
else:
    print(answer)