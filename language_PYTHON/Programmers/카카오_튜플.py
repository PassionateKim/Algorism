# 2022-08-05
# 2022-08-06
# 2022-08-12
# 2022-08-19
# 튜플
import re
def solution(s):
    answer = []
    
    s = re.findall('{[\d,]+}', s)
    print(s)
    for i in s:
        i = i[1:-1].split(",")
        print("i:",i)
        return
        for ii in i:
            if int(ii) not in answer:
                answer.append(int(ii))
    
    return answer

solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")