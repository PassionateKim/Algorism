# 예산
# 복습 횟수:1, 00:30:00, 복습필요:X
import sys
si = sys.stdin.readline
N = int(si())
request_list = list(map(int, si().split()))
budget = int(si())
answer = 0

def binary(start, end, target):
    global answer
    while start <= end:
        sumi = 0
        mid = (start + end) // 2
        for request in request_list:
            if mid >= request:
                sumi += request
            else:
                sumi += mid
        
        if sumi <= target:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1 
    return

binary(0, max(request_list), budget)
print(answer)