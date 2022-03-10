#N과 M(4)

#N과 M(3)

N,M = map(int,input().split())

arr = []
def backTraking(count,check):
    if(count == M):
        print(*arr)
        return
        
    
    for i in range(N):
        if(i >=check-1):
            arr.append(i+1)
            backTraking(count+1,i+1)
            arr.pop()

backTraking(0,0)

    


