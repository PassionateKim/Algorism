# 월드컵
# 복습 횟수:1, 00:30:00, 복습필요O
from itertools import combinations
import sys
si = sys.stdin.readline
answer = []
def dfs(index):
    global flag
    if index == 15:
        check = 0
        for val in graph:
            check += sum(val)
        if check == 0:
            flag = 1

        return

    me, you = match_list[index]
    
    # me 승
    if graph[me][0] > 0 and graph[you][2] > 0:
        graph[me][0] -= 1
        graph[you][2] -= 1
        dfs(index + 1)
        graph[me][0] += 1
        graph[you][2] += 1

    # me 무
    if graph[me][1] > 0 and graph[you][1] > 0:
        graph[me][1] -= 1
        graph[you][1] -= 1
        dfs(index + 1)    
        graph[me][1] += 1
        graph[you][1] += 1
        
    # me 패
    if graph[me][2] > 0 and graph[you][0] > 0:
        graph[me][2] -= 1
        graph[you][0] -= 1
        dfs(index + 1)
        graph[me][2] += 1
        graph[you][0] += 1

    return

for i in range(4):
    tmp = list(map(int, si().split()))
    graph = [[tmp[3*j], tmp[3*j + 1], tmp[3*j + 2]] for j in range(6)]
    
    match_list = list(combinations(range(6), 2))
    flag = 0
    dfs(0)
    if flag:
        answer.append(1)
    else:
        answer.append(0)

print(*answer)