# 나무 재테크
# 복습 횟수:0, 01:45:00, 복습필요O
import sys
import copy
from collections import deque
si = sys.stdin.readline
N, M, K = map(int, si().split())
dir = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
sd = []
for i in range(N):
    sd.append(list(map(int, si().split())))
tree_list = [[deque() for i in range(N)] for i in range(N)]

for i in range(M):
    x, y, age = list(map(int, si().split())) 
    tree_list[x-1][y-1].append(age)

graph = [[5 for i in range(N)] for i in range(N)] # 초기엔 양분이 5

for year in range(K):
    # 봄
    for i in range(N):
        for j in range(N):
            tmp = deque()
            for k in range(len(tree_list[i][j])):
                if graph[i][j] >= tree_list[i][j][k]:
                    graph[i][j] -= tree_list[i][j][k]
                    tree_list[i][j][k] += 1
                else: #여름
                    for _ in range(k, len(tree_list[i][j])):
                        graph[i][j] += tree_list[i][j].pop() // 2
                    break

    # 가을
    for x in range(N):
        for y in range(N):
            for tree in tree_list[x][y]:
                if (tree % 5) == 0:
                    for idx in range(8):
                        nx, ny = x + dir[idx][0], y + dir[idx][1]
                        if not (0 <= nx < N and 0 <= ny < N): continue

                        tree_list[nx][ny].appendleft(1)
            # 겨울
            graph[x][y] += sd[x][y]
    
answer = 0
for i in range(N):
    for j in range(N):
        answer += len(tree[i][j])
print(answer)