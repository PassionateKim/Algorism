# 1. 왜 O(N+G)인지?
# 2. 이 코드는 왜 오답인지?  -> 어떤 순서에 따라 멈춰버릴 수도 있기 때문 ex) 1 -> 2를 하면 없어지는 것이 생기는데 1 -> 3에서 끝나버릴 수 있으므로

# 복습 횟수:0, 02:00:00, 복습필요:***
from collections import deque
import sys
si = sys.stdin.readline

N, G = map(int, si().split())

graph = [{}]
visited = [0 for i in range(N+1)]

for i in range(G):
    inp = list(map(int, si().split()))
    people_list = inp[1:]
    people_set = set(people_list)
    graph.append(people_set)

def bfs():
    global answer
    q = deque()
    q.append(1)

    while q:
        target = q.popleft()
        answer += 1
        for i in range(1, len(graph)):
            if visited[i] == 1: continue # 방문했다면 pass

            candidate_set = graph[i]
            if target in candidate_set:
                candidate_set.remove(target)
                if (len(candidate_set) == 1):
                    q.append(list(candidate_set)[0])
                    visited[i] = 1 # 방문처리
                    candidate_set.remove(q[-1])
    return

answer = 0
bfs()
print(answer)