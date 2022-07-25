# 2022-07-25
# 2022-07-26
# 후위 표기식
import sys
si = sys.stdin.readline

input = list(map(str, si().strip()))
op_stack = []
answer = ""
for str in input:
    if str.isalpha():
        answer += str
    else:
        # 왼괄호
        if str == '(':
            op_stack.append(str)
        # "+", "-"
        elif str == '+' or str == '-':
            while op_stack and op_stack[-1] != '(':
                answer += op_stack.pop()
            
            op_stack.append(str)
        # "*", "/"
        elif str == '*' or str == '/':
            while op_stack and op_stack[-1] in ["*", "/"]:
                answer += op_stack.pop()
            
            op_stack.append(str)
        # ")"
        else:
            while op_stack and op_stack[-1] != '(':
                answer += op_stack.pop()
            
            op_stack.pop()

while op_stack:
    answer += op_stack.pop()

print(answer)

