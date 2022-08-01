# 2022-07-25
# 2022-07-26
# 2022-07-28
# 2022-08-01
# 후위 표기식
import sys
si = sys.stdin.readline

op_stack = []
answer = ""

input = si().strip()

for s in input:
    if s == '(':
        op_stack.append(s)
    elif s.isalpha():
        answer += s
    elif s == '+' or  s == '-':
        while op_stack and op_stack[-1] != '(':
            answer += op_stack.pop()
        
        op_stack.append(s)
    elif s == '*' or s == '/':
        while op_stack and op_stack[-1] in ['*', '/']:
            answer += op_stack.pop()
        
        op_stack.append(s)
    else:
        while op_stack and op_stack[-1] != '(':
            answer += op_stack.pop()
        
        op_stack.pop()

while op_stack:
    answer += op_stack.pop()
print(answer)