# #N-Queen
# #N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
# #N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.
import sys

N = int(input())
cnt = 0
graph = [[0] * N for _ in range(N)] 



def isPromising(depth,y):
    for i in range(depth):
        for j in range(N):
            if graph[i][j] == 1:
                if j == y or (abs(depth - i) == abs(j - y)):
                    graph[depth][y] = 0 # 초기화
                    return False
    return True

def dfs(depth):
    global graph
    global cnt
    if depth == N:
        cnt += 1
        graph = [[0] * N for _ in range(N)] # 초기화
        return
    else:# 값을 저장해서 풀어야됨. -> 어떻게 solve 할까?????
        for y in range(N):
            
            graph[depth][y] = 1 # 미리 참조?? 왜죠??

            if isPromising(depth,y):
                dfs(depth+1)
 
dfs(0)
print(cnt)


# n = int(sys.stdin.readline().rstrip())

# ans = 0
# row = [0] * n

# def is_promising(x):
#     for i in range(x):
#         if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
#             return False
#     return True

# def n_queens(x):
#     global ans
#     if x == n:
#         print(row)
#         ans += 1

#     else:
#         for i in range(n):
#             # [x, i]에 퀸을 놓겠다.
#             row[x] = i
#             if is_promising(x):
#                 n_queens(x+1)

# n_queens(0)
# print(ans)