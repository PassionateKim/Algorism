# 2022-08-03
# 2022-08-05
# 2022-08-11
# 2023-10-31
# 카카오 수식 최대화

from itertools import permutations
import re

def solution(expression):
    answer = 0
    # 1. 나누기
    expression = re.split(r'(\+|\*|\-)', expression)

    operation_list = list(permutations(["*", "-", "+"])) 
    
    for operations in operation_list:
        tmp_expression_list = expression[:]
        
        # - + * 등으로 순서 체크 하면서 바꾸기
        for oper in operations:
            combine_list = []
            for index, val in enumerate(tmp_expression_list):

                if(val == oper):
                    combine_list.append(index)
            
            
            # 초기화
            new_expression_list = []
            
            cursor = 0
            while cursor < len(tmp_expression_list):
                if cursor in combine_list:
                    left = new_expression_list.pop()                     
                    right = tmp_expression_list[cursor + 1]

                    new_val = str(eval(left + oper + right))
                    
                    new_expression_list.append(str(new_val))
                    cursor += 2
                else:
                    new_expression_list.append(tmp_expression_list[cursor])
                    cursor += 1

            tmp_expression_list = new_expression_list[:]

        answer = max(answer, abs(int(tmp_expression_list[0])))

    
    return answer


print(solution("100-200*300-500+20"))
