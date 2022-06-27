# K번째 수
import sys
si = sys.stdin.readline

N = int(si())
k = int(si())

def determination(mid, num):
    sumi = 0
    for i in range(1, N+1): # 1,2...N
        tmp = mid // i
        if tmp > N:
            tmp = N
        sumi += tmp
    return sumi >= num

def Binary(start, end, target):
    ans = 0
    while start<=end:
        mid = (start + end) // 2
        if determination(mid, target): # 크거나 같아서 되는 범위
            ans = mid 
            end = mid - 1
        else: # 작아서 안되는 범위
            start = mid + 1

    return ans

print(Binary(1, N*N, k))