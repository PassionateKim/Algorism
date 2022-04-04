#이분 그래프
import sys
from collections import deque
K = int(input())

for i in range(K):
    V,E = map(int, sys.stdin.readline().rstrip().split())
    graph = [[] for _ in range(V+1)] #빈 그래프 생성
    visited = [0] * (V+1)   #방문한 정점 체크
    
    #그래프 값 넣기
    for i in range(E):
        x,y = map(int,sys.stdin.readline().rstrip().split())
        graph[x].append(y) #무방향 그래프
        graph[y].append(x) #무방향 그래프

    q = deque()
    group = 1
    bipatite = True
    for i in range(1,V+1):
        if visited[i] == 0: #방문하지 않은 정점이면 BFS 수행
            q.append(i)
            visited[i] = group
            while q:
                v = q.popleft()
                for w in graph[v]:
                    if visited[w] == 0: #방문하지 않은 정점이면 큐에 삽입 
                        q.append(w)
                        visited[w] = -1 * visited[v]
                    elif visited[w] == visited[v]:
                        bipatite = False
    print("YES" if bipatite else "NO")   

