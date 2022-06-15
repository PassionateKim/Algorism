#나무 자르기
import sys
si = sys.stdin.readline
N, M = map(int, si().split())
tree_list = list(map(int, si().split()))
def Binary(start, end, target):
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        sum = 0
        for tree in tree_list:
            if tree > mid:
                sum += (tree - mid)
        if sum >= target:            
            answer = mid
            start = mid + 1
        else:
            end = mid - 1 
    print(answer)
Binary(0, max(tree_list), M)