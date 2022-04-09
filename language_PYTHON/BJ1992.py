#쿼드트리
import sys

N = int(input())
quad_tree = []
result = []
for i in range(N):
    quad_tree.append(list(map(int,sys.stdin.readline().rstrip())))

def solution(x,y,N):
    quad = quad_tree[x][y]

    for i in range(x,x+N):
        for j in range(y,y+N):
            if quad != quad_tree[i][j]:
                result.append("(")
                solution(x,y,N//2)
                solution(x,y+N//2,N//2)
                solution(x+N//2,y,N//2)
                solution(x+N//2,y+N//2,N//2)
                result.append(")")
                return
    result.append(quad)


solution(0,0,N)

for i in result:
    print(i,end="")