# 2024-04-10
# 2024-04-11

import heapq
def solution(n, k, enemy_list: list):

    if k >= len(enemy_list):
        return len(enemy_list)
    
    pq = []
    for index, enemy in enumerate(enemy_list):
        heapq.heappush(pq, enemy)

        if len(pq) > k:
            mini = heapq.heappop(pq)

            if n < mini:
                return index
            
            n = n - mini 
    
    return len(enemy_list)

print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))
