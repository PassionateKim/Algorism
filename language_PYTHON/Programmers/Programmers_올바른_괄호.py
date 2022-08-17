# 2022-08-18
# 올바른 괄호
def solution(s):
    stack = []
    answer = True
    for ss in s:
        if ss == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
        else:
            stack.append(ss)

    if stack:
        return False
    return True

print(solution("(())()"))