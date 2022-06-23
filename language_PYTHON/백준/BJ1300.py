# K번째 수
import sys
si = sys.stdin.readline

N = int(si())
k = int(si())

def determination(num, target):
    # num 보다 작거나 같은것의 개수 ex) num = 4
    sumi = 0
    # 1*1 1*2 1*3
    # 2*1 2*2 2*3
    # 3*1 3*2 3*3
    for i in range(1, N+1):
        tmp = num // i
        if tmp > N:
            tmp = N
        sumi += tmp  
    # sumi = 6
    return sumi >= target

def Binary(start, end, target):
    ans = 0
    while start<=end:
        mid = (start+end)//2
        if determination(mid, target):
            ans = mid
            end = mid - 1
        else:
            start = mid + 1   
    return ans

answer = Binary(1, N*N, k)
print(answer)