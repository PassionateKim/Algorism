#숨바꼭질

from collections import deque


N,K = map(int,input().split())

def DFS():
    if(N == K):
        print(0)
        return
    queue = deque()
    queue.append([N,0])

    while queue:
        a,b = queue.popleft()
       
        # print(a,b,queue)
        if(2*a == K or a-1 == K or a+1 == K):
            print(b+1)
            return
        if(a != 0):
            if([a-1,b+1] not in queue):
                queue.append([a-1,b+1])
            if([2*a,b+1] not in queue):
                queue.append([2*a,b+1])
        if([a+1,b+1] not in queue):
            queue.append([a+1,b+1])


DFS()