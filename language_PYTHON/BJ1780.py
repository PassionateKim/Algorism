#종이의 개수
import sys
N = int(input())
paper = []
result = []
for i in range(N):
    paper.append(list(map(int,sys.stdin.readline().rstrip().split())))


def solution(x,y,N):
    a = paper[x][y]
    for i in range(x,x+N):
        for j in range(y,y+N):
            if a != paper[i][j]:
                solution(x,y,N//3)
                solution(x,y+N//3,N//3)
                solution(x,y+N//3*2,N//3)

                solution(x+N//3,y,N//3)
                solution(x+N//3,y+N//3,N//3)
                solution(x+N//3,y+N//3*2,N//3)

                solution(x+N//3*2,y,N//3)
                solution(x+N//3*2,y+N//3,N//3)
                solution(x+N//3*2,y+N//3*2,N//3)
                return
    

    if a == -1:
        result.append(-1)
    elif a == 0:
        result.append(0)
    else:
        result.append(1)




solution(0,0,N)
print(result.count(-1))
print(result.count(0))
print(result.count(1))