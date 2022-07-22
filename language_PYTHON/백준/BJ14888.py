#연산자 끼워넣기
import sys
si = sys.stdin.readline

N = int(si())
arr = list(map(int, si().split()))
plus, minus, mul, div = map(int, si().split())
sumi = arr[0]
maxi = -1e6
mini = 1e6

def dfs(plus, minus, mul, div, sumi, depth):
    global maxi, mini
    if plus + minus + mul + div == 0:
        maxi = max(maxi, sumi)
        mini = min(mini, sumi)

    if plus:
        dfs(plus-1, minus, mul, div, sumi+arr[depth+1], depth+1)
    if minus:
        dfs(plus, minus-1, mul, div, sumi-arr[depth+1], depth+1)
    if mul:
        dfs(plus, minus, mul-1, div, sumi*arr[depth+1], depth+1)
    if div:
        if sumi < 0:
            tmp = (-sumi // arr[depth+1]) * (-1)
        else:
            tmp = sumi//arr[depth+1]

        dfs(plus, minus, mul, div-1, tmp, depth+1)
            

dfs(plus, minus, mul, div, sumi, 0)
print(maxi)
print(mini)