# 스도쿠
# 복습 횟수:3, 01:00:00, 복습필요O
import sys
si = sys.stdin.readline

graph = [list(map(int, si().split())) for _ in range(9)]

blank_list = []
for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            blank_list.append([i, j])

def isGaro(x, y, val):
    for i in range(9):
        if graph[x][i] == val:
            return False
    
    return True

def isSero(x, y, val):
    for i in range(9):
        if graph[i][y] == val:
            return False
    
    return True

def isRec(x, y, val):
    hang = (x // 3) * 3
    yeol = (y // 3) * 3
    for i in range(hang, hang + 3):
        for j in range(yeol, yeol + 3):
            if graph[i][j] == val:
                return False

    return True

def dfs(index):
    if index == len(blank_list):
        for i in range(9):
            print(*graph[i])
        exit()
    
    for val in range(1, 10):
        x, y  = blank_list[index][0], blank_list[index][1]
        if isGaro(x, y, val) and isSero(x, y, val) and isRec(x, y, val):
            graph[x][y] = val
            dfs(index + 1)
            graph[x][y] = 0 # 초기화

    # for x, y in blank_list:
    #     if graph[x][y] == 0: # 0인 경우
    #         for val in range(1, 10):
    #             if isGaro(x, y, val) and isSero(x, y, val) and isRec(x, y, val):
    #                 graph[x][y] = val
    #                 dfs(index + 1)
    #                 graph[x][y] = 0 # 초기화
dfs(0)