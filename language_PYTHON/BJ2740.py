#행렬 곱셈
import sys
N,M = map(int,input().split())
A = []
B = []
for i in range(N):
    A.append(list(map(int,sys.stdin.readline().rstrip().split())))

M,K = map(int,input().split())

for i in range(M):
    B.append(list(map(int,sys.stdin.readline().rstrip().split())))

# 행렬 곱셈

C = [[0 for _ in range(K)] for _ in range(N)]

for n in range(N):
    for k in range(K):
        for m in range(M):
            C[n][k] += A[n][m] * B[m][k]

for i in C:
    for j in i:
        print(j,end=" ")
    print()