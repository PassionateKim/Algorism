# 2022-09-01
# 다리를 지나는 트럭
from collections import deque
def solution(bridge_length, weight, truck_weights):
    truck_stack = deque()
    answer = 0
    truck_weights = deque(truck_weights)
    
    while truck_weights:
        answer += 1
        sumi = 0
        for truck in truck_stack:
            sumi += truck[0]

        if sumi + truck_weights[0] <= weight:
            truck_stack.append([truck_weights.popleft(), bridge_length])
        
        for truck in truck_stack:
            truck[1] -= 1
            
        if truck_stack[0][1] == 0:
            truck_stack.popleft()
        
    while truck_stack:
        answer += 1
        for truck in truck_stack:
            truck[1] -= 1
        
        if truck_stack[0][1] == 0:
            truck_stack.popleft()
    
    print(answer)
    return answer

solution(2, 10, [7,4,5,6])