# 메뉴 리뉴얼
from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    answer = []

    for menu_cnt in course: 
        candidates = []
        tmp_combi_dict = defaultdict(int)
        
        for order in orders:
            order_list = list(''.join(order))
            for li in combinations(order_list, menu_cnt):
                res = ''.join(sorted(li))
                if res not in candidates:
                    candidates.append(res)
                else:
                    if res not in tmp_combi_dict.keys():
                        tmp_combi_dict[res] = 2
                    else:
                        tmp_combi_dict[res] += 1
                
        # 가장 많이 주문 된 경우
        if tmp_combi_dict:
            maxi = max(tmp_combi_dict.values())
            for key, value in tmp_combi_dict.items():
                if value == maxi:
                    answer.append(key)
    answer.sort()
    return answer
solution(["XYZ", "XWY", "WXA"], [2,3,4])