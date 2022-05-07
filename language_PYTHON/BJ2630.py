#색종이 만들기
import sys
N = int(sys.stdin.readline())

paper_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cnt_one = 0
cnt_zero = 0

def dfs(x, y, n):
    global cnt_one
    global cnt_zero
    what_number = paper_list[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper_list[i][j] != what_number:
                dfs(x, y, n//2)
                dfs(x, y + n//2, n//2)
                dfs(x + n//2, y, n//2)
                dfs(x + n//2, y + n//2, n//2)
                return
    if what_number == 0:
        cnt_zero += 1
    elif what_number == 1:
        cnt_one += 1



dfs(0,0,N)
print(cnt_zero)
print(cnt_one)
























# paper = []
# paper2 = []
# for i in range(N):
#     paper.append(list(map(int,sys.stdin.readline().split())))

# for i in range(N):
#     a = list(map(int,sys.stdin.readline().split()))
#     paper2.append(a)





# paper[0][1] = 1
# paper2[0][1] = 1

# for i in paper:
#     print(i)

# print("-------------")
# for i in paper2:
#     print(i)