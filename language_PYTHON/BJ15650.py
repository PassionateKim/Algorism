#N과 M(2)
#문제
#자연수 N과 M이 주어졌을 때, 
# 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
#1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
#고른 수열은 오름차순이어야 한다.

from dis import code_info


N,M = map(int,input().split())
check_list = [False] * N
arr = []

def dfs(count):
    #깊이 탐색 완료 시
    if(count == M and arr == sorted(arr)):
        print(*arr)
    
    for i in range(N):
        #수열이므로 중복은 제거하는 조건
        if(check_list[i]):
            continue

        #자기보다 작은건 안된다는 조건
        

        check_list[i] = True
        arr.append(i+1)
        
        #depth 추가
        dfs(count+1)

        #초기화
        check_list[i] = False
        arr.pop()

dfs(0)
