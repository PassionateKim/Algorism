from itertools import combinations
from collections import deque
import sys
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

positions = [(i, j) for i in range(5) for j in range(5)]
combs = list(combinations(positions, 7))
answer = 0

for _ in range(5):
    graph.append(list(sys.stdin.readline().strip()))

def checkDasom(student_combi):
    isdasom = 0

    for x, y in student_combi:
        if graph[x][y] == 'S':
            isdasom += 1

    return True if isdasom >= 4 else False

def checkBfs(student_combi):
    visited = [0 for i in range(7)]

    q = deque()
    q.append(student_combi[0])   
    visited[0] = 1 # 방문 처리

    while q:
        x, y = q.popleft()

        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]
            if (nx, ny) in student_combi: 
                next_index = student_combi.index((nx, ny))  
                
                if visited[next_index] == 0:
                    visited[next_index] = 1 # 방문 처리
                    q.append((nx, ny))

    return True if False not in visited else False

answer = 0
for com in combs:
    if checkDasom(com) and checkBfs(com):
        answer += 1
print(answer)
# def checkAdjacent(givenComb):
#     visit = [False]*7
#     q = deque()
#     q.append(givenComb[0])
#     visit[0] = True

#     while q:
#         x, y = q.popleft()
#         for d in direction:
#             nx = x + d[0]
#             ny = y + d[1]
#             if (nx, ny) in givenComb:
#                 nextIdx = givenComb.index((nx, ny))
#                 if not visit[nextIdx]:
#                     q.append((nx, ny))
#                     visit[nextIdx] = True

#     return False if False in visit else True


# for comb in combs:
#     if checkDaSom(comb):
#         if checkAdjacent(comb):
#             answer += 1

# print(answer)

# 이 풀이는 메모리 초과 문제를 어떻게 해결했을까? -> 해결하지 않았음..