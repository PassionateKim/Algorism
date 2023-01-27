#나무 자르기
# 복습 횟수:3, 00:45:00, 복습필요X
import sys
si = sys.stdin.readline
N, M = map(int, si().split())
tree_list = list(map(int, si().split()))
answer = 0
def binary(start, end, target):
    global answer
    while start <= end:
        mid = (start + end) // 2
        sumi = 0
        for tree in tree_list:
            if tree >= mid:
                sumi += (tree - mid) # diff 
        
        if sumi >= target:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
    return

binary(1, max(tree_list), M)
print(answer)