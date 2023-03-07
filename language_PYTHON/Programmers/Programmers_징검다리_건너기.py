# 복습 횟수:1, 00:30:00, 복습필요O
def solution(stones, k):
    answer = 0

    start = 1
    end = max(stones)

    while start <= end:
        mid = (start + end) // 2
        count = 0

        for s in stones:
            if s - mid <= 0:
                count += 1
            else:
                count = 0
            
            if count == k:
                break
                
        
        if count >= k:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer

print(solution([2, 4, 5, 3, 2, 2, 4, 2, 5, 11], 5))
