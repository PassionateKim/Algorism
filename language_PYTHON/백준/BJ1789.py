# 수들의 합
# 복습 횟수:0, 00:45:00, 복습필요O
import sys
si = sys.stdin.readline
answer = 0
sumi = 0
N = int(si())

def binary(start, end):
    global answer
    while start <= end:
        mid = (start + end) // 2
        target = ((mid) * (mid + 1)) // 2 # n(n+1) // 2 = 총합 공식

        if target <= N:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1

    return

binary(1, N)
print(answer)