# 배열 돌리기
import sys
si = sys.stdin.readline

T = int(si())

def clockWise(d):
    num = d // 45

    for i in range(num):
        beforeArray = []
        # 행 저장하기
        for i in range(n):
            beforeArray.append(graph[n//2][i])
        
        # 행 -> 주대각선
        for i in range(n):
            tmp2 = graph[i][i]
            graph[i][i] = beforeArray[i]
            beforeArray[i] = tmp2
        

        # 주대각선 -> 열
        for i in range(n):
            tmp2 = graph[i][n//2]
            graph[i][n//2] = beforeArray[i]
            beforeArray[i] = tmp2

        #열 -> 부대각선
        for i in range(n): # 4 3 2 1 0 
            tmp2 = graph[(n-1)-i][i]
            graph[(n-1)-i][i] = beforeArray[(n-1)-i]
            beforeArray[(n-1)-i] = tmp2

        # 부대각선 -> 행 
        for i in range(n): 
            graph[n//2][i] = beforeArray[n-1-i]
       
    return

def counterClockWise(d):
    num = abs(d) // 45

    for i in range(num):
        beforeArray = []
        # 행 저장하기
        for i in range(n):
            beforeArray.append(graph[n//2][i])
        
        # 행 -> 부대각선
        for i in range(n):
            tmp2 = graph[n-1-i][i]
            graph[n-1-i][i] = beforeArray[i]
            beforeArray[i] = tmp2

        # 부대각선 -> 열
        for i in range(n):
            tmp2 = graph[i][n//2] # 3 8 13 18 23
            graph[i][n//2] = beforeArray[n-1-i]
            beforeArray[n-1-i] = tmp2 # 23 18 13 8 3
        # before = [23, 18, 13, 8, 3]
        beforeArray.reverse() # -> [3, 8, 13, 18, 23]
        #열 -> 주대각선
        for i in range(n): # 4 3 2 1 0 
            tmp2 = graph[i][i]  # 1 7 13 19 25
            graph[i][i] = beforeArray[i]
            beforeArray[i] = tmp2
        # before = [1, 7, 13, 19, 25]
        
        # 주대각선 -> 행 
        for i in range(n): 
            graph[n//2][i] = beforeArray[i]
        
    return

for i in range(T):
    n, d = map(int, si().split())
    graph = [list(map(int, si().split())) for _ in range(n)]

    if d >= 0:  
        clockWise(d)
    else:
        counterClockWise(d)
    
    for i in graph:
        print(*i)