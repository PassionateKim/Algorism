#이항 계수3

N,K = map(int,input().split())


answer = []
def solution(N,K):
    
    if K == 1:
        return N
    elif N == K:
        return 1
    return solution(N-1,K-1) + solution(N-1,K)

print(solution(N,K))
    


