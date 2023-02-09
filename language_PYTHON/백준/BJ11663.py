# 선분 위의 점
# 복습 횟수:2, 01:00:00, 복습필요:O
import sys
si = sys.stdin.readline
N, M = map(int, si().split())
point_list = list(map(int, si().split()))
point_list.sort()

line_list = []
for i in range(M):
    tmp = list(map(int, si().split()))
    line_list.append(tmp)

def bisect_left(start, end, target):
    while start <= end:
        mid = (start + end) // 2

        if point_list[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1

    return start

def bisect_right(start, end, target):
    while start <= end:
        mid = (start + end) // 2

        if point_list[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    
    return end

for left, right in line_list:
    least = bisect_left(0, len(point_list)-1, left)
    largest = bisect_right(0, len(point_list)-1, right)
    print(largest - least + 1)
