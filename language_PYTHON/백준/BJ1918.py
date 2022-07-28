# 2022-07-25
# 2022-07-26
# 2022-07-28
# 후위 표기식
import sys
si = sys.stdin.readline
chars = list(map(str, si().strip()))
op_stack = []
answer = ""
for ch in chars:
    if ch.isalpha():
        answer += ch
    elif ch == '(':
        op_stack.append(ch)
    elif ch == '+' or ch == '-':
        while op_stack and op_stack[-1] != '(':
            answer += op_stack.pop()
        
        op_stack.append(ch)
    elif ch == '*' or ch == '/':
        while op_stack and op_stack[-1] in ['*', '/']:
            answer += op_stack.pop()
        
        op_stack.append(ch)
    else:
        while op_stack and op_stack[-1] != '(':
            answer += op_stack.pop()
        
        op_stack.pop()
        
while op_stack:
    answer += op_stack.pop()

print(answer)