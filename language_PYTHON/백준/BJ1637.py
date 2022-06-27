import sys
si = sys.stdin.readline

N = int(si())
A = list()
for i in range(N):
    A.append(list(map(int, si().split())))

def determination(array, mid):

    sumi = 0 # mid 이하의 수의 개수 
    for i in array:
        a, c, b = i[0], i[1], i[2]
        checki = min(mid, c) # 최대
        if a > mid: # 최소가 기준값보다 크다면
            sumi += 0 # 기준값 이하의 수가 아무것도 없다.
        else:
            sumi += (checki - a) // b + 1 # 이하의 개수 버림 + 1 

    return sumi # 홀수인지 체크

def Binary(array, start, end):
    ans = -1
    while start<=end:
        mid = (start+end)//2
        if determination(array, mid) % 2:
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
    return ans

tmp = Binary(A, 1, 2147483637)
if tmp == -1:
    print("NOTHING")
else:
    print(tmp, determination(A, tmp) - determination(A, tmp-1))