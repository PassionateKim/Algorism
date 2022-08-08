# 2022-07-25
# 2022-07-26
# 2022-07-28
# 2022-08-01
# 2022-08-08
# 후위 표기식
import sys
si = sys.stdin.readline

string = list(map(str, si().rstrip()))
op_stack = []
answer = ''

for s in string:
    if s.isalpha():
        answer += s
    elif s == '+' or s == '-':
        while op_stack and op_stack[-1] != '(':
            answer += op_stack.pop()
        
        op_stack.append(s)
    elif s == '*' or s == '/':
        while op_stack and op_stack[-1] in ['*','/']:
            answer += op_stack.pop()
        
        op_stack.append(s)
    elif s == '(':
        op_stack.append(s)
    else: # s == ')'
        while op_stack and op_stack[-1] != '(':
            answer += op_stack.pop()
        
        op_stack.pop()


while op_stack:
    answer += op_stack.pop()

print(answer)