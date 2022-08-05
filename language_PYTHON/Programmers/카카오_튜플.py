# 2022-08-05
# 2022-08-06
# 튜플
import re
def solution(s):
    answer = []
    r = re.findall('{[\d,]+}', s)
    print(r)
    s = re.split(r'({[\d,]+})', s[1:-1])
    for i in s:
        if i == ',':
            s.remove(",")
        elif i == '':
            s.remove('')
    arr = []
    for i in s:
        arr.append(i[1:-1].split(","))
    
    arr.sort(key=lambda x:len(x))
    
    for i in arr:
        for j in i:
            if int(j) not in answer:
                answer.append(int(j))
    
    return answer

solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")