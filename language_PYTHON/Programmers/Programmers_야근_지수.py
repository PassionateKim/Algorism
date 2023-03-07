# 복습 횟수:1, 00:30:00, 복습필요X
import heapq
def solution(n, works: list):
    answer = 0
    works = [-w for w in works]
    heapq.heapify(works)    
    
    for i in range(n):
        val = heapq.heappop(works)
        if val != 0:
            val = val + 1
        heapq.heappush(works, val)
    
    
    for w in works:
        answer += w ** 2

    return answer

solution([4, 3, 3], 4)

solution([2, 1, 2], 1)

solution([1, 1], 3)