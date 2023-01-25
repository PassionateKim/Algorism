# 배열 합치기
# 복습 횟수:0, 00:30:00, 복습필요O
import sys
si = sys.stdin.readline
N, M = map(int, si().split())

A = list(map(int, si().split()))
B = list(map(int, si().split()))
answer = []
a = 0
b = 0

while a != len(A) or b != len(B):
    if a == len(A):
        answer.append(B[b])
        b += 1
    elif b == len(B):
        answer.append(A[a])
        a += 1
    else:
        if A[a] < B[b]:
            answer.append(A[a])
            a += 1
        else:
            answer.append(B[b])
            b += 1

print(*answer)
