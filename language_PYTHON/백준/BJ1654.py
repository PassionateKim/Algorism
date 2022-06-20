# 랜선 자르기
import sys
si = sys.stdin.readline
K, N = map(int, si().split())
A = []
for i in range(K):
    A.append(int(si()))

A.sort()

def Binary(array, start, end, target):
    answer = 0
    while start<=end:
        mid = (start+end)//2
        cnt = 0
        for i in array:
            cnt += i//mid
        
        if cnt >= target:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1

    return answer

print(Binary(A, 0, max(A), N))