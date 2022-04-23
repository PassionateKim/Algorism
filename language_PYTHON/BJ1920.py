#수 찾기
import sys
input = sys.stdin.readline

n = int(input())
N = sorted(list(map(int,input().split())))
m = int(input())
M = list(map(int, input().split()))

def binary(l, N, start, end):
    if start > end:
        return 0
    m = (start + end) // 2
    if l == N[m]:
        return 1
    elif l < N[m]:
        return binary(l, N, start, m-1)
    else: #l > N[m]
        return binary(l, N, m+1, end)





for l in M:
    start = 0 #index의 시작
    end = len(N) - 1 #indext의 끝
    print(binary(l, N, start, end))