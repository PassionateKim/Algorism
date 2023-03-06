# 복습 횟수:0, 00:30:00, 복습필요O
import heapq
def solution(works: list, n):
    answer = 0
    works = [-w for w in works]
    heapq.heapify(works)

    for i in range(n):
        val = heapq.heappop(works)

        if val != 0:
            val = val + 1
        heapq.heappush(works, val)

    
    for val in works:
        answer += val ** 2

    print(answer)
    return answer


solution([1, 1], 3)