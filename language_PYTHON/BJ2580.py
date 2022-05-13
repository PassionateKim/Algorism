#스도쿠
import sys
sdoku = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
blank_list = []

# 빈칸 체크
for x in range(9):
    for y in range(9):
        if sdoku[x][y] == 0:
            blank_list.append((x,y))

# Promising한지? 가로 체크 한번이라도 같으면 안된다.
def isRowPossible(x,value):
    for i in range(9):
        if sdoku[x][i] == value:
            return False
    return True

def isColPossible(y,value):
    for i in range(9):
        if sdoku[i][y] == value:
            return False
    return True



def isRecPossible(x,y,value):
    nx = (x // 3) * 3
    ny = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if sdoku[nx+i][ny+j] == value:
                return False
    return True



def dfs(depth):
    if depth == len(blank_list):
        for item in sdoku:
            print(*item)
        exit()

    for blank in blank_list:
        if blank in sdoku:
            continue
        
        x,y = blank[0], blank[1] 
        
        for i in range(1, 9+1):
            if isRowPossible(x,i) and isColPossible(y,i) and isRecPossible(x,y,i):
                sdoku[x][y] = i
                dfs(depth+1)
                sdoku[x][y] = 0

    # for i in range(1, 9+1): # 접근법 복습 필요
    #     x, y = blank_list[depth][0], blank_list[depth][1]
    #     if isRowPossible(x,i) and isColPossible(y,i) and isRecPossible(x,y,i):
    #         sdoku[x][y] = i
    #         dfs(depth+1)
    #         sdoku[x][y] = 0 # 초기화 for 다음턴

dfs(0)





# # 행 -> 열
# for row in range(9):
#     for col in range(9):
#         if(sdoku[row][col] == 0):
#             blank.append((row,col))

# print(blank)

# def isRowPromising(x,a):
#     for i in range(9):
#         if a == sdoku[x][i]:
#             return False
#     return True

# def isColPromising(y,a):
#     for i in range(9):
#         if a == sdoku[i][y]:
#             return False
#     return True

# def isRectanglePromising(x,y,a):
#     nx = x//3 * 3
#     ny = y//3 * 3
#     for i in range(3):
#         for j in range(3):
#             if a == sdoku[nx+i][ny+j]:
#                 return False
#     return True

# def dfs(depth):
#     if depth == len(blank):
#         for i in range(9):
#             print(*sdoku[i])
#         return

#     for i in range(1,10):
#         x = blank[depth][0]
#         y = blank[depth][1]

#         if isRowPromising(x,i) and isColPromising(y,i) and isRectanglePromising(x,y,i):
#             sdoku[x][y] = i
#             dfs(depth+1)
#             sdoku[x][y] = 0

# dfs(0)
# print(sdoku)
# print(sdoku[1][2])