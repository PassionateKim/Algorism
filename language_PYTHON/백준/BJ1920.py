#수 찾기
import sys
si = sys.stdin.readline

N = int(si())
A = sorted(list(map(int, si().split())))
M = int(si())
B = list(map(int, si().split()))

def lower_bound(start, end, target):
    while start<=end:
        mid = (start + end) // 2
        if A[mid] == target:
            return 1
        if A[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    # 찾을 수 없는 경우
    return 0

for i in B:
    print(lower_bound(0, len(A)-1, i)) 
