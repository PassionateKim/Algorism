# 2022-08-03
# 2022-08-05
# 2022-08-11
# 카카오 수식 최대화
from collections import deque
from itertools import permutations
import re
def solution(expression):
    answer = 0
    # 1. 나누기
    expression = re.split(r'(\+|\-|\*)', expression)
    expression = deque(expression)
    tmp_expression = deque()
    # 2.우선순위 결정해 계산하기
    for p in permutations(["*","-","+"], 3):
        tmp_expression.extend(expression)
        for op in p: # *
            print("op", op)
            new_expression = deque()
            while tmp_expression:
                tmp = tmp_expression.popleft()
                if tmp != op:
                    new_expression.append(tmp)
                else:
                    left = new_expression.pop()
                    right = tmp_expression.popleft()

                    print("left: ",left,"right: ",right)
                
                    new_expression.append(str(eval(left+op+right)))
            # 초기화
            tmp_expression.extend(new_expression) 
        #/ 우선순위 계산 끝
        answer = max(answer, abs(int(tmp_expression.pop())))
        print(answer)
    
    return answer

solution("100-200*300-500+20")