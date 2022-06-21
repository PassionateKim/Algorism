# 이상한 술집
import sys
si = sys.stdin.readline
N, K = map(int, si().split())
drinks = []

for i in range(N):
    drinks.append(int(si()))

def determination(array, mid, target):
    res = 0
    for i in array:
        res += i//mid
    # 예를들어 200일 때 target보다 크다면 가능한 경우이다.
    return res >= target

def Binary(array, start, end, target):
    ans = 0
    while start<=end:
        mid = (start+end)//2

        if determination(array, mid, target):
            ans = mid
            start = mid + 1
        else:
            end = mid - 1

    return ans

print(Binary(drinks, 1, max(drinks), K))