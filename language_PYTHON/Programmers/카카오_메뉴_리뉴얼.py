# 메뉴 리뉴얼
from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for c in course:
        order_combi = []
        for order in orders:
            for combi in combinations(order, c):
                order_combi.append(''.join(sorted(combi)))
        # ['AB', 'AC', 'AD', 'AE', 'BC', 'BD', 'BE', 'CD']
        order_count = Counter(order_combi).most_common()
        maxi = -1
        for oc in order_count:
            maxi = max(maxi, oc[1])
        for oc in order_count:
            if oc[1] == maxi and maxi != 1:
                answer.append(oc[0])
    answer.sort()
    print(answer)
    return answer
solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])

# set.add
# set, dict 는 in 체크할때 해쉬를 사용해 O(1)