# 2022-08-16
# 순위검색
from collections import defaultdict
from itertools import combinations
from bisect import bisect_left
def solution(information, queries):
    answer = []
    dic = defaultdict(list)
    for info in information:
        info = info.split()
        condition = info[:-1]  
        score = int(info[-1])
        for i in range(5):
            case = list(combinations([0,1,2,3], i))
            for c in case:
                tmp = condition.copy()
                for idx in c:
                    tmp[idx] = "-"
                key = ''.join(tmp)
                dic[key].append(score) 

    for value in dic.values():
        value.sort()   
    
    for query in queries:
        query = query.replace("and","")
        query = query.split()
        target_key = ''.join(query[:-1])
        target_num = int(query[-1])
        count = 0
        if target_key in dic:
            idx = bisect_left(dic[target_key], target_num)
            count = len(dic[target_key]) - idx
        answer.append(count)

    return answer

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])