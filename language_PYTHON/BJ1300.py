# K번째 수
N = int(input())
K = int(input())

def Binary(start, end):
    while start <= end:     
        mid = (start + end) // 2
        
        cnt = 0
        for i in range(1, N+1):
            cnt += min(N, mid // i)
                
        print(start, end, mid, cnt)
        if cnt >= K: # 줄여야하므로
            end = mid - 1
        else: # 키워야 하므로
            start = mid + 1 
    return start
print(Binary(1, 10**9))


        
