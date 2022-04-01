#숨바꼭질

from collections import deque

N,K = map(int,input().split())
dist = [0]*100001
print(dist)

def DFS():
    queue = deque()
    queue.append(N)

    while queue:
        x = queue.popleft()
        if(dist[x] == K):
            print(x)
            return
        
        for i in (x-1,x+1,x*2):
            if(dist[i] == 0 and 0<=i<=100000):
                dist[i] = dist[x] + 1
                queue.append(i)
    


    

 
DFS()