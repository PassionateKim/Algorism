# K번째 수
N = int(input())
K = int(input())

def Binary(start, end):
    while start <= end:
        mid = (start + end) // 2
        count = 0
        for i in range(1, N+1):
            count += min(N, mid // i)

        if count < K:
            start = mid + 1
        else:
            end = mid - 1
        print(start, end) 
    




Binary(1, 10**9)