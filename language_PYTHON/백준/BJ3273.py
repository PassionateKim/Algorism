# 두 수의 합
# a1 + a2 = x
import sys
si = sys.stdin.readline

N = int(si())
A = sorted(list(map(int, si().split())))
X = int(si())

answer = 0

def Binary(array, start, end, target):
    global answer
    while start<=end:
        mid = (start + end) // 2
        if (array[mid] + target) == X:
            answer += 1
            return
        if (array[mid] + target) > X:
            end = mid - 1
        else:
            start = mid + 1
    return

for i in range(len(A)-1):
    Binary(A, i+1, len(A)-1, A[i])
print(answer)

