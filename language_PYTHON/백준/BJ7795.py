# 먹을 것인가 먹힐 것인가
import sys
si = sys.stdin.readline
T = int(si())

def Binary(array, start, end, target):
    k = 0
    while start <= end:
        mid = (start + end) // 2

        if array[mid] < target:
            start = mid + 1
            k = mid + 1
        else:
            end = mid - 1
    return k 
            


for i in range(T):
    N, M = map(int, si().split())
    A = sorted(list(map(int, si().split())))
    B = sorted(list(map(int, si().split())))
    cnt = 0
    # A는 자기보다 크기가 작은 먹이만 먹을 수 있다.
    for a in A:
        k = Binary(B, 0, len(B)-1, a)
        cnt += k
    print(cnt)
