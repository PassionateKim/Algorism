# 2022-09-01
# 2022-09-02
# 다리를 지나는 트럭
from collections import deque
def solution(bridge_length, weight, truck_weights):
    truck_stack = deque()
    answer = 0
    truck_weights = deque(truck_weights)
    
    while truck_weights:
        answer += 1
        sumi = 0
        # 트럭의 무게 
        for truck in truck_stack:
            sumi += truck[0]
        # 트럭의 무게 체크해서 올리기
        if sumi + truck_weights[0] <= weight:
            truck_stack.append([truck_weights.popleft(), bridge_length]) 
        # answer +=1 을 한 상태이니 -1 해준다
        for truck in truck_stack:
            truck[1] -= 1
        
        # 트럭이 다리를 건넌다면 뺀다
        if truck_stack[0][1] == 0:
            truck_stack.popleft()
    
    while truck_stack:
        answer += 1
        
        if truck_stack[0][1] == 0:
            truck_stack.popleft()
        for truck in truck_stack:
            truck[1] -= 1
    print(answer)
    return answer

solution(2, 10, [7,4,5,6])