from collections import deque
# 배달

from collections import defaultdict
def solution(N, road, K):
    answer, mydict = {1:0}, defaultdict(set)
    for st, end, cost in road:
        mydict[st].add((end, cost))
        mydict[end].add((st, cost))
    def dfs(curr, total_c):
        if total_c > K:
            return
        for end, cost in mydict[curr]:
            if end in answer and total_c+cost >= answer[end]:
                continue
            elif total_c + cost <= K:
                answer[end] = total_c + cost
                dfs(end, total_c + cost)
    dfs(1, 0)
    return len(answer)
    
# 시간초과 풀이
# def dfs(start, target, sum, K, road, graph, flag):
#     global answer
#     # dfs가 target에 도달한 경우
#     if start == target:
#         if sum <= K:
#             flag[0] = 1 # 가능처리
#         return
    
#     visited[start] = 1 # 방문처리

#     for end in graph[start]:
#         if visited[end] == 0: # 방문하지 않은 경우
#             visited[end] = 1 # 방문처리
#             distance = 1e6
#             # road 완전 탐색하며 최솟값 구하기
#             for rd in road:
#                 if (rd[0] == start and rd[1] == end) or (rd[1] == start and rd[0] == end):
#                     distance = min(distance, rd[2])
#             dfs(end, target, sum+distance, K, road, graph, flag)
#             visited[end] = 0 # 방문처리 원상 복구

# answer = 0
# visited = []
# road = []

# def solution(N, road, K):
#     global visited
#     global answer
#     visited = [0 for _ in range(N+1)]
#     # 간선관계
#     graph = [set() for i in range(N+1)]
#     for i in road:
#         x, y = i[0], i[1]
#         graph[x].add(y)
#         graph[y].add(x)

#     for i in range(1, len(graph)):
#         graph[i] = sorted(list(graph[i]))
    
#     # 간선 탐색
#     for target in range(2, N+1):
#         flag = [0]
#         dfs(1, target, 0, K, road, graph, flag)
#         if flag[0] == 1:
#             answer += 1
#     return answer+1 # 본인 포함

solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4)