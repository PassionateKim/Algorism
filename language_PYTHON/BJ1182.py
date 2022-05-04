# 부분수열의 합

N, S = map(int, input().split())
array_list = list(map(int, input().split()))

cnt = 0
def dfs(sum, depth, flag):
    
    global cnt
    # 탈출 조건
    if depth == N:
        if  S == sum and not flag == N:
            cnt += 1
        return

    dfs(sum, depth+1, flag+1)
    dfs(sum+array_list[depth], depth+1, flag)

    
dfs(0,0,0)


print(cnt)

