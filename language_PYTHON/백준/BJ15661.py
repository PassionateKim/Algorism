# 링크와 스타트
# 복습 횟수:1, 01:00:00, 복습필요X
import sys
from itertools import combinations 
si = sys.stdin.readline 
N = int(si())
score_graph = []
for i in range(N):
    tmp = list(map(int, si().split()))
    score_graph.append(tmp)

# 1. home, away 팀원 수 
number_of_teammate_case = []
home, away = 2, N - 2
while home <= away:
    number_of_teammate_case.append([home, away])
    home += 1
    away -= 1

def dfs(team_list: list, case_list: list, depth, index, tmp: list):
    if len(tmp) == 2:
        case_list.append(tmp[:])
        return
    
    for i in range(index, len(team_list)):
        if team_list[i] not in tmp:
            tmp.append(team_list[i])
            dfs(team_list, case_list, depth + 1, i + 1, tmp)
            tmp.pop()

    return

answer = sys.maxsize

# home, away 가능한 case 구하기
for home_number, away_number in number_of_teammate_case:
    home_team_list = list(combinations(range(N), home_number))
    
    for home_team in home_team_list:
        home_team = list(home_team)
        away_team = [i for i in range(N) if not i in home_team]
        
        home_team_total_score = 0
        away_team_total_score = 0

        home_case = []
        dfs(home_team, home_case, 0, 0, [])
        away_case = []
        dfs(away_team, away_case, 0, 0, [])

        for x, y in home_case:
            home_team_total_score += score_graph[x][y]
            home_team_total_score += score_graph[y][x]
        
        for x, y in away_case:
            away_team_total_score += score_graph[x][y]
            away_team_total_score += score_graph[y][x]

        diff = abs(away_team_total_score - home_team_total_score)
        answer = min(diff, answer)
    
print(answer)