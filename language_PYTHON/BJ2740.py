#행렬 곱셈
import sys
# N,M = map(int,input().split())
# A = []
# B = []
# for i in range(N):
#     A.append(list(map(int,sys.stdin.readline().rstrip().split())))

# M,K = map(int,input().split())
# for i in range(M):
#     B.append(list(map(int,sys.stdin.readline().rstrip().split())))
 
# C = [[0 for _ in range(K)] for _ in range(N)]


# for n in range(N):
#     for k in range(K):
#         for m in range(M):
#             C[n][k] += A[n][m] * B[m][k]

# for i in C:
#     print(*i)

c = [0] * 4
C = []
for _ in range(5):
    C.append(c)

C[0][1] = 1

for i in C:
    print(i)
#-------------------------------------------
C = [[0]*4 for _ in range(5)]
C[0][1] = 1

for i in C:
    print(i)
