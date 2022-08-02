# 2022-06-09
# 2022-08-02
# 짝지어 제거하기

def solution(s):
    tmp = []
    result = 0
    tmp.append(s[0])

    for i in range(1, len(s)):
        if tmp and tmp[-1] == s[i]:
            tmp.pop()
        else:
            tmp.append(s[i])
    
    if not tmp:
        result = 1
        
    return result

print(solution("bbbbbb"))