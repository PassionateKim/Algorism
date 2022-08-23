# 2022-08-23
# 괄호 회전하기
from collections import deque

def solution(s):
    def isCorrect(q: deque):
        op_stack = []
        while q:
            val = q.popleft()
            if val in ['(', '[', '{']:
                op_stack.append(val)
            else: #[')', ']', '}']
                if val == ')':
                    if op_stack and op_stack[-1] == '(':
                        op_stack.pop()
                    else:
                        return False
                elif val == ']':
                    if op_stack and op_stack[-1] == '[':
                        op_stack.pop()
                    else:
                        return False
                else:
                    if op_stack and op_stack[-1] == '{':
                        op_stack.pop()
                    else:
                        return False
        
        if op_stack:
            return False
        else:
            return True
    # /isCorrect()
    answer = 0

    for i in range(len(s)):
        check = deque(s)
        # 1. i 횟수 동안 회전하기
        for j in range(i):
            check.append(check.popleft())
        # 2. 올바른 괄호인지 체크하기
        if isCorrect(check):
            answer += 1



    print(answer)
    return answer

solution("[](){}")