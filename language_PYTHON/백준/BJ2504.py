# 괄호의 값
import sys
si = sys.stdin.readline

stack = []
answer = 0
tmp = 1
char_list = list(si().strip()) 

for i in range(len(char_list)):
    char = char_list[i]

    if char == '(':
        stack.append(char)
        tmp *= 2 # 2배로 올린다.
    elif char == '[':
        stack.append(char)
        tmp *= 3

    elif char == ')':
        if not stack or stack[-1] == '[':
            answer = 0
            break
        if char_list[i-1] == '(':
            answer += tmp
        tmp = tmp // 2
        stack.pop()
    else: # char == ']'
        if not stack or stack[-1] == '(':
            answer = 0
            break
        if char_list[i-1] == '[':
            answer += tmp
        tmp = tmp // 3
        stack.pop()
        
if stack:
    answer = 0
    
print(answer)