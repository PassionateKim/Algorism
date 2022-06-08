import heapq
# 더 멥게
def solution(scoville, K):
    heapq.heapify(scoville)
    flag = 0
    answer = 0
    while True:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        c = a + (2 * b)
        heapq.heappush(scoville, c)
        
        answer += 1
        if scoville[0] >= K:
            break
        
        if len(scoville) == 1:
            flag = 1
    if flag == 1:
        answer = -1
    print(answer)
    return answer

solution([1, 2, 3, 9, 10, 12], 10000)