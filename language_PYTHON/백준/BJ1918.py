# 후위 표기식
import sys
si = sys.stdin.readline

strs = si().strip()

# 연산자 스택
op_stack = []

# 정답
answer = ""

for char in strs:
    # 알파벳이면 바로 정답 문자열에 추가
    if char.isalpha():
        answer += char
    # 연산자 계산
    else: 
        # 왼쪽 괄호는 바로 연산자 스택에 추가
        if char == '(':
            op_stack.append(char)
        
        # 곱셈과 나눗셈은 같은 우선순위 연산자를 연산자 스택에서 정답 문자열로 옮긴 후 추가
        elif char == '*' or char == '/':
            while len(op_stack) != 0 and op_stack[-1] in ['*','/']:
                answer += op_stack.pop()
            
            op_stack.append(char)
        
        # 덧셈 뺼셈은 왼쪽 괄호를 만나거나 스택이 빌 때까지 모두 정답 문자열로 옮긴 후 추가
        elif char == '+' or char == '-':
            # 무슨 연산자든 앞에있는 것이 먼저
            while len(op_stack) != 0 and op_stack[-1] != '(':
                answer += op_stack.pop()

            op_stack.append(char)

        # 오른쪽 괄호는 왼쪽 괄호를 만날 때까지 정답 문자열로 옮긴 후 왼쪽 괄호 제거
        else:
            while op_stack[-1] != '(':
                answer += op_stack.pop()
            
            op_stack.pop()

while len(op_stack) != 0:
    answer += op_stack.pop()

print(answer)