# 2024.06.04
# 복습 횟수:0, 복습필요X

import math
def solution(r1, r2):
    answer = 0
    
    for i in range(1, r2 + 1):
        y2 = math.sqrt(r2 ** 2 - i ** 2)
        if r1 < i:
            y1 = 0
        else:
            y1 = math.sqrt(r1 ** 2 - i ** 2)
        # print(f"i = {i} y2 = {y2} floor(y2) = {math.floor(y2)}")
        # print(f"i = {i} y1 = {y1} ceil(y1) = {math.ceil(y1)}")
        # print(f"count = {math.floor(y2) - math.ceil(y1) + 1}")
        answer = answer + math.floor(y2) - math.ceil(y1) + 1
    
    answer = answer * 4 
    # x 좌표 중복 한번 빼기
    # 둘의 값이 같으므로 pass
    
    # y 좌표 더하기
    # 둘의 값이 같으므로 pass
    return answer