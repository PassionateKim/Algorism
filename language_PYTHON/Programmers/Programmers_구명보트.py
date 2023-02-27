# 복습 횟수:0, 01:00:00, 복습필요O
from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    q = deque(people)

    while len(q) > 1:
        if q[0] + q[-1] <= limit:
            q.popleft()
        
        answer += 1
        q.pop()

    if q:
        answer += 1
    return answer

print(solution([10, 70, 50, 80, 50, 10, 20], 100))