# 예산
# 복습 횟수:2, 00:30:00, 복습필요:X
import sys
si = sys.stdin.readline 
N = int(si())

arr = list(map(int, si().split()))
budget = int(si())

def  binary_search():
    answer = 0

    start = 0
    end = max(arr)

    while start <= end:
        mid = (start + end) // 2

        candidate_sum = 0
        for val in arr:
            if mid >= val:
                candidate_sum += val
            else:
                candidate_sum += mid
        
        if candidate_sum <= budget:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1

    return answer

print(binary_search())