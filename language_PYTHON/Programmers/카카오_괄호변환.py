# 괄호변환
from collections import deque

def isCorrect(chars):
    count = 0
    for i in chars:
        if i == '(':
            count += 1
        else: # ')'
            count -= 1
        
        if count < 0:
            return False
    return True

def isBalancedString(str):
    return str.count('(') == str.count(')')

def splitUV(str):
    u, v = str, ""
    for i in range(2, len(str), 2):
        if isBalancedString(str[:i]):
            u = str[:i]
            v = str[i:]
            break
    return u, v

def method(chars):
    # 1 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
    if chars == '':
        return ''

    # 2 균형잡힌 괄호 문자열 u, v로 분리합니다.
    u, v = splitUV(chars)

    if isCorrect(u): #올바른 문자열 이라면
        # 문자열 v에 대해 1단계부터 다시 수행합니다.
        u += method(v)
        return u
    else:
        newStr = '('
        newStr += method(v)
        newStr += ')'
        # 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
        answer = ""
        for s in u:
            if s == '(':
                answer += ')'
            else:
                answer += '('

        newStr += answer[1:-1]
        return newStr

def solution(p):
    if isCorrect(p):
        return p
    
    return method(p)

print(solution("()))((()"))

# reverse != 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.