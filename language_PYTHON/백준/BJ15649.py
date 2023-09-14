# N과 M (1)
import sys
si = sys.stdin.readline 
N, M = map(int, si().split())

def dfs(depth, answer_list: list):
    if depth == M:
        print(*answer_list)
        return
    
    for i in range(1, N + 1):
        if i not in answer_list:
            answer_list.append(i)
            dfs(depth + 1, answer_list)
            answer_list.pop()

    return

dfs(0, [])