#색종이 만들기
import sys
N = int(sys.stdin.readline())

paper = []
paper2 = []
for i in range(N):
    paper.append(list(map(int,sys.stdin.readline().split())))

for i in range(N):
    a = list(map(int,sys.stdin.readline().split()))
    paper2.append(a)





paper[0][1] = 1
paper2[0][1] = 1

for i in paper:
    print(i)

print("-------------")
for i in paper2:
    print(i)