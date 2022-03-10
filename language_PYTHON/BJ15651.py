#N과 M(3)

N,M = map(int,input().split())

arr = []
def backTraking(count):
    if(count == M):
        print(*arr)
        return
        
    
    for i in range(N):
        arr.append(i+1)
        backTraking(count+1)
        arr.pop()

backTraking(0)

    


