# 복습횟수:0, 03:00:00, 복습필요3
from collections import defaultdict

def solution(tickets):
    # 특정 티켓의 인접 리스트를 구하는 함수
    def init_graph():
        routes = defaultdict(list)
        for key, value in tickets:
            routes[key].append(value)
        return routes

    # 재귀 호출을 사용한 DFS
    def dfs(key, footprint):
        if len(footprint) == N + 1:
            return footprint
        
        for idx, country in enumerate(routes[key]):
            poped_country = routes[key].pop(idx)

            fp = footprint[:]
            fp.append(poped_country)

            res = dfs(country, fp)

            if res:
                return res
            
            routes[key].insert(idx, poped_country)
        
        return

    routes = init_graph()
    for r in routes:
        routes[r].sort()

    N = len(tickets)
    answer = dfs("ICN", ["ICN"])

    return answer

solution([["ICN", "AAA"], ["ICN", "BBB"], ["BBB", "ICN"]])