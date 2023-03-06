# 복습 횟수:0, 00:30:00, 복습필요X
from copy import deepcopy
answer = 10

def dfs(begin, target, words, cnt, visited: list):
    global answer
    # 탈출 조건
    if begin == target:
        answer = min(answer, cnt)
        return
    
    for i in range(len(words)):
        if visited[i] == 1: continue

        check = []
        for j in range(len(words[i])):
            if begin[j] != words[i][j]:
                check.append(j)
        
        if len(check) == 1:
            visited[i] = 1 # 방문처리

            tmp = deepcopy(begin)
            begin = deepcopy(words[i])

            dfs(begin, target, words, cnt + 1, visited)

            visited[i] = 0 # 초기화
            begin = tmp # 초기화
             
    return

def solution(begin, target, words):
    if target not in words:
        return 0
    
    visited = [0 for i in range(len(words))]
    dfs(begin, target, words, 0, visited)


    return answer


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))