#수 찾기
import sys
si = sys.stdin.readline

N = int(si())
A = list(map(int, si().split()))
A.sort()

M = int(si())
B = list(map(int, si().split()))

def binary_search(start, end, target):

    while start <= end:
        mid = (start + end) // 2

        if (A[mid] == target):
            print(1)
            return
        
        elif (A[mid] > target):
            end = mid - 1
        else:
            start = mid + 1
        
    print(0)
    return

for target in B:
    binary_search(0, len(A) - 1, target)