# 2022-08-10
# 프린터
from collections import deque
def solution(priorities, location):
    answer = 0
    # 편의를 위해 deque
    priorites = deque(priorities)
    # 위치 저장
    l = deque([0] * len(priorities))
    l[location] = 1 

    while priorites:
        tmp = priorites[0]
        # tmp가 가장 큰지 체크
        flag = 0
        for i in range(1, len(priorites)):
            # 맨 앞보다 큰것이 존재한다면
            if priorites[i] > tmp:
                flag = 1
        
        # 맨 앞보다 큰 것이 존재한다면
        if flag == 1:
            priorites.append(priorites.popleft())
            l.append(l.popleft())
        else:
            if l[0] == 1:
                answer += 1
                # print("l: ", l)
                # print("priorites: ", priorites)
                # print("answer: ", answer)
                return answer
            
            priorites.popleft()
            l.popleft()
            answer += 1

        # print("l: ", l)
        # print("priorities: ", priorites)
        # print("answer: ", answer)
        # print("===========")


    return answer

solution([2, 1, 3, 2], 2)