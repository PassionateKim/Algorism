# 2022-09-01
# 2022-09-02
# 2022-09-04
# 2022-09-08
# 다리를 지나는 트럭
from collections import deque
def solution(bridge_length, weight, truck_weights):
    q=[0]*bridge_length
    q = deque(q)
    sec=0
    while q:
        sec+=1
        q.popleft()
        if truck_weights:
            if sum(q)+truck_weights[0]<=weight:
                q.append(truck_weights.popleft())
            else:
                q.append(0)

    return sec
solution(4, 10, [7,4,5,6])