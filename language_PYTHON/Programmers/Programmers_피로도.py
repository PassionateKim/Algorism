def dfs(depth, k, visited, dungeons, count):
    global answer
    n = len(dungeons)
    
    if ( depth == n ):
        answer = max(answer, count)
        return
    
    for i in range(n):
        if visited[i] != 0: continue

        visited[i] = 1 # 방문 처리

        if k >= dungeons[i][0]:
            dfs(depth + 1, k - dungeons[i][1], visited, dungeons, count + 1)
        else:
            dfs(depth + 1, k, visited, dungeons, count)
        
        visited[i] = 0

    return

answer = -1

def solution(k, dungeons):
    visited = [0 for i in range(len(dungeons))]
    
    dfs(0, k, visited, dungeons, 0)
    
    return answer