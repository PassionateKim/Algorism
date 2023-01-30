# 수들의 합
# 복습 횟수:1, 00:30:00, 복습필요O
import sys
si = sys.stdin.readline
answer = 0
N = int(si())

def binary(start, end, target):
    global answer
    while start <= end:
        mid = (start + end) // 2

        if (mid)*(mid + 1) // 2 > target:
            answer = mid - 1
            end = mid - 1
        else:
            start = mid + 1

    return

binary(1, 4294967295, N)
print(answer)