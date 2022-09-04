# 2022-09-01
# 2022-09-02
# 2022-09-04
# 다리를 지나는 트럭
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    stack = deque()
    truck_weights = deque(truck_weights)


    while truck_weights:
        sumi = 0
        answer += 1
        # 1. 현재 다리에 있는 트럭의 무게 체크
        for truck in stack:
            sumi += truck[0]
        # 1.1 트럭이 건널 수 있다면
        if sumi + truck_weights[0] <= weight:
            stack.append([truck_weights.popleft(), bridge_length])
        # 시간이 경과한 상태를 가정하므로
        for truck in stack:
            truck[1] -= 1
        
        # 트럭이 끝점에 도달했다면
        if stack[0][1] == 0:
            stack.popleft()

    print(answer)
    return answer

solution(2, 10, [7,4,5,6])