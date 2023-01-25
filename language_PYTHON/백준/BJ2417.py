# 정수 제곱근
# 복습 횟수:0, 00:15:00, 복습필요O
import sys
import math
si = sys.stdin.readline
N = int(si())

answer = 0
def binary(start, end, target):
    global answer
    while start <= end:
        mid = (start + end) // 2
        if (mid ** 2) >= target:
            answer = mid
            end = mid - 1 
        else:
            start = mid + 1
    return

binary(0, N, N)
print(answer)