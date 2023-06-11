# 게리맨더링
# 복습 횟수:0, 01:00:00, 복습필요O
import sys
from collections import deque
from itertools import combinations
si = sys.stdin.readline
N = int(si())
population = [0] + list(map(int, si().split()))
graph = [[] for _ in range(N+1)]

# 그래프 연관관계 초기화
for i in range(1, N + 1):
    tmp = list(map(int, si().split()))
    
    for j in range(1, len(tmp)):
        graph[i].append(tmp[j])


def bfs(home, away):
    visited = [0 for i in range(N+1)]
    # home check
    q = deque()
    q.append(home[0])
    visited[home[0]] = 1 # home 방문처리
    while q:
        idx = q.popleft()
        for val in graph[idx]:
            if visited[val] != 0: continue
            if val in away: continue

            q.append(val)
            visited[val] = 1 # home 방문처리

    q = deque()
    q.append(away[0])
    visited[away[0]] = 2 # away 방문처리
    while q:
        idx = q.popleft()
        for val in graph[idx]:
            if visited[val] != 0: continue
            if val in home: continue

            q.append(val)
            visited[val] = 2 # away 방문처리

    return visited

answer = sys.maxsize
# 모든 케이스에 대해 최대: 2**10 - 2 
for i in range(1, N):
    case_list = list(combinations(range(1, N+1), i))

    for home in case_list:
        away = [i for i in range(1, N+1) if i not in home]
        # 1. 이대로 나뉠 수 있는지 체크
        visited = bfs(home, away)

        # 2. visited를 체크해 가능한지 안가능한지 판별하기
        isTrue = True
        for val in home:
            if visited[val] == 0:
                isTrue = False
                break
        
        for val in away:
            if visited[val] == 0:
                isTrue = False
                break
        
        if isTrue: # 가능한 조합이라면
            home_sum = 0
            for idx in home:
                home_sum += population[idx]
            
            away_sum = 0
            for idx in away:
                away_sum += population[idx]
            
            answer = min(answer, abs(home_sum - away_sum))

if answer == sys.maxsize:
    answer = -1

print(answer)