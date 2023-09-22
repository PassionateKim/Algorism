# N과 M (1)
# 복습횟수:3, 00:30:00, 복습필요1
import sys
si = sys.stdin.readline 
N, M = map(int, si().split())


def dfs(depth, candidate_list: list):
    if depth == M:
        print(*candidate_list)
        return
    
    for i in range(1, N+1):
        if i not in candidate_list:
            candidate_list.append(i)
            dfs(depth + 1, candidate_list)
            candidate_list.pop()

    return

dfs(0, [])