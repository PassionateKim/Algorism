# 2022-08-05
# 튜플
import re
from collections import defaultdict
def solution(s):
    answer = []
    result = re.findall('[{][\d,]+[}]', s)
    result.sort(key=lambda x: len(x))
    now = set()
    print("result", result)
    for x in result:
        next = set(list(x[1:-1].split(',')))
        print("next", next)
        print("now", now)
        print(next - now)
        exit()
        num = list(next - now)[-1]
        answer.append(int(num))
        now = next

    return answer


solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")