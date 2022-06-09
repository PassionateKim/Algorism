# 괄호변환
from collections import deque
# 올바른 문자열인지 체크하는 함수
def isCorrect(chars): 
    chars = deque(chars)
    tmp = []
    tmp.append(chars.popleft())

    if tmp[-1] == ")":
        return False
    while chars:
        a = chars.popleft()
        if a == '(':
            tmp.append(a)
        else:
            if len(tmp) == 0:
                return False
            else:
                tmp.pop()
    if tmp:
        return False
    return True

def method(chars):
    global answer

    # 1입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
    if len(chars) == 0:
        return ''
    if isCorrect(chars): # 올바른 문자열이면 그대로 return
        answer += "".join(chars)
        return chars

    chars = list(chars)
    
    # 2
    u = []
    for i in range(len(chars)):
        u.append(chars.pop(0))
        if u and u.count("(") == u.count(")"): # 균형잡힌 문자열
            if isCorrect(u):
                answer += "".join(u)
                method(chars)
            else:
                answer += "("  
                method(chars) 
                answer += ")"
                u.pop(0)
                u.pop()
                print(u)
                for i in range(len(u)):
                    if u[i] == '(':
                        u[i] = ')'
                    else:
                        u[i] = '('
                answer += "".join(u)
            break 
    
answer = ''
def solution(p):
    global answer
    method(p)
    print(answer)
    return answer

solution("))(()((((()))()))")