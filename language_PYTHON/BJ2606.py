#바이러스
from collections import deque


N = int(input())
M = int(input())

count = 0

computer_list = [[] for i in range(N+1)]
visited = [False] *(N+1)
visited[1] = True
for i in range(M):
    a,b = map(int,input().split())
    computer_list[a].append(b)
    computer_list[b].append(a)

for i in range(1,N+1):
    computer_list[i].sort()



def bfs(idx):
    global count
    queue = deque([idx])
    
    while queue:
        
        v = queue.popleft()
        for i in computer_list[v]:
            if not visited[i]:
                queue.append(i)
                count += 1
                visited[i] = True


    
 




bfs(1)
print(count)