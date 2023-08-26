# 월드컵
# 복습 횟수:2, 01:30:00, 복습필요2
import sys
from itertools import combinations

si = sys.stdin.readline 

# A B C D E F
country_list = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
def dfs(depth):
    global flag
    if depth == 15:
        if result_list == country_list:
            flag = 1
        return
    
    home_index, away_index = match_list[depth]
    
    home = result_list[home_index]
    away = result_list[away_index]

    # 내가 이기는 경우
    if home[0] >= 1 and away[2] >= 1:
        home[0] -= 1
        away[2] -= 1
        dfs(depth + 1)
        home[0] += 1
        away[2] += 1

    # 무승부
    if home[1] >= 1 and away[1] >= 1: 
        home[1] -= 1
        away[1] -= 1
        dfs(depth + 1)
        home[1] += 1
        away[1] += 1
        
    # 내가 지는 경우
    if home[2] >= 1 and away[0] >= 1:
    
        home[2] -= 1
        away[0] -= 1
        dfs(depth + 1)
        home[2] += 1
        away[0] += 1
    
    return

match_list = []

visited = [0 for i in range(6)]
def make_combi(idx, arr: list):
    if len(arr) == 2:
        match_list.append(arr[:])
        return
    
    for i in range(idx + 1, 6):
        if visited[i] == 0: 
            arr.append(i)
            visited[i] = 1 
            make_combi(i, arr)
            visited[i] = 0
            arr.pop()



make_combi(-1, [])

for i in range(4):
    tmp = list(map(int, si().split()))
    flag = 0
    result_list = [[tmp[3*j], tmp[3*j + 1], tmp[3*j + 2]] for j in range(6)]
    dfs(0)
    print(flag, end = " ")