# 링크와 스타트
# 복습 횟수:0, 01:45:00, 복습필요O
import sys
from itertools import combinations
si = sys.stdin.readline
N = int(si())
answer = sys.maxsize
graph = []
for i in range(N):
    tmp = list(map(int, si().split()))
    graph.append(tmp)

team_list = [i for i in range(N)]

for i in range(2, len(team_list)//2 + 1):
    combi_list = list(combinations(team_list, i))
    for combi in combi_list:
        other_list = [x for x in team_list if x not in combi]
        start = combi
        link = other_list
        # 점수 구하기
        start_sum = 0
        link_sum = 0
        start_pair = list(combinations(start, 2))
        link_pair = list(combinations(link, 2))
        # start 점수 
        # print("start_pair",start_pair)
        for x, y in start_pair:
            start_sum += graph[x][y]
            start_sum += graph[y][x]
        # link 점수
        for x, y in link_pair:
            link_sum += graph[x][y]
            link_sum += graph[y][x]
        # 차이
        diff = abs(start_sum - link_sum)
        # print(start, link, "start:", start_sum, "link", link_sum, "diff", diff)
        answer = min(answer, diff)
print(answer)