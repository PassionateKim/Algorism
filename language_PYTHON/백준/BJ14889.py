# 스타트와 링크
from itertools import combinations
import sys
si = sys.stdin.readline

N = int(si())
graph = [list(map(int, si().split())) for _ in range(N)]
players = [i for i in range(N)] 
teams = list(combinations(players, N//2))

vs = []
# 팀 vs 넣기
for idx in range(len(teams)//2):
    vs.append([teams[idx], teams[len(teams)-1-idx]])

mini = 1e4
for team in vs:
    tmp = []
    # 팀 탐색
    for i in team:#[0,1,2], [3,4,5]
        pair = list(combinations(i, 2)) #[0,1], [0,2], [1,2]
        sumi = 0
        for x, y in pair:
            sumi += graph[x][y] #[0,1]
            sumi += graph[y][x] #[1,0] 
        tmp.append(sumi)
    # 팀 탐색
    diff = abs(tmp[0] - tmp[1])
    mini = min(diff, mini)

print(mini)