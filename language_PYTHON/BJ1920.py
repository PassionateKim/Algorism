#수 찾기
import sys
input = sys.stdin.readline

N = int(input())
A_array = list(map(int, input().split()))
M = int(input())
B_array = list(map(int, input().split()))

# 이분탐색을 위해서는 반드시 정렬이 필요하다.
A_array.sort()

def Binary(start, end, target):
    while start <= end:
        mid = (start + end) // 2
        # 이분 탐색 탈출 조건
        if A_array[mid] == target:
            print(1)
            return
        
        # 이분 탐색 비즈니스 로직
        if A_array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    print(0)
    return


for item_B in B_array:
    Binary(0, len(A_array)-1, item_B)


