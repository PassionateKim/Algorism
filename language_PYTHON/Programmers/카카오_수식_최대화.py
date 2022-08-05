# 2022-08-03
# 2022-08-05
# 카카오 수식 최대화
from itertools import permutations
from collections import deque
import re
def solution(expression):
    answer = 0
    # 1. 쪼개기
    expression = re.split(r'(\+|\-|\*)', expression)
    expression = deque(expression)
    # 2. 우선순위
    priority_list = list(permutations(["*","-","+"], 3))
    
    tmp_expression = deque()
    tmp_expression.extend(expression)
    
    for priority in priority_list:
        tmp_expression = deque()
        tmp_expression.extend(expression)
    
        for op in priority: # * -> - -> + 
            tmp = []
            while tmp_expression:
                s = tmp_expression.popleft()
                if s == op:
                    left_val = tmp.pop()
                    right_val = tmp_expression.popleft()
                    val = eval(left_val + op + right_val)
                    tmp.append(str(val))
                else:
                    tmp.append(s)
            #/op
            tmp_expression.extend(tmp)
        #/priority
        print(abs(int(tmp_expression[0])))
        answer = max(answer, abs(int(tmp_expression[0])))
    # print(answer)


            

    return answer

solution("100-200*300-500+20")