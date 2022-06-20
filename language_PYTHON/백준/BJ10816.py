# 숫자카드2
import sys
si = sys.stdin.readline

N = int(si())
A = sorted(list(map(int, si().split())))
M = int(si())
B = list(map(int, si().split()))

# target보다 작거나 같은 것 중 가장 큰 것의 인덱스
def lower_bound(array, start, end, target):
    res = 0
    while start<=end:
        mid = (start+end)//2
        if array[mid] <= target:
            res = mid + 1
            start = mid + 1
        else:
            end = mid - 1 
    return res
# target보다 작은 것 중 가장 큰 것의 인덱스
def upper_bound(array, start, end, target):
    res = 0
    while start<=end:
        mid = (start+end)//2
        if array[mid] < target:
            res = mid + 1
            start = mid + 1
        else:
            end = mid - 1 
    return res

for item in B:
    print(lower_bound(A, 0, len(A)-1, item) - upper_bound(A, 0, len(A)-1, item), end=' ')

