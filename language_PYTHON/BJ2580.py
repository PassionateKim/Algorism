#스도쿠
import sys
sdoku = []
blank = []
for i in range(9):
    sdoku.append(list(map(int,sys.stdin.readline().rstrip().split())))

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
print(sdoku)
print(sdoku[1][2])