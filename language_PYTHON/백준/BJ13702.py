# 이상한 술집
import sys
si = sys.stdin.readline
N, K = map(int, si().split())
drinks = []
for i in range(N):
    drinks.append(int(si()))

def determination(drinks, mg, num):
    sum = 0
    for dr in drinks:
        sum += dr // mg

    return sum >= num

def Binary(array, start, end, target):
    ans = 0
    while start<=end:
        mid = (start + end) // 2
        if determination(array, mid, target):
            ans = mid
            start = mid + 1
        else:
            end = mid - 1

    return ans

print(Binary(drinks, 1, max(drinks), K))