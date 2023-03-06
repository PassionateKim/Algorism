# 복습 횟수:0, 01:00:00, 복습필요O
def solution(stones, k):
    answer = 0
    left = 1
    right = max(stones)
    
    while left <= right:
        mid = (left + right) // 2
        count = 0
        for stone in stones:
            if stone - mid <= 0:
                count += 1
            else:
                count = 0
            
            if count == k:
                break
        
        if count >= k:
            right = mid - 1
            answer = mid
        else:
            left = mid + 1

    return answer

print(solution([2, 4, 5, 3, 2, 2, 4, 2, 5, 11], 5))
