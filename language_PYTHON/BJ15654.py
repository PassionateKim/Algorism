# N과 M(5)

N, M = map(int, input().split())

N_array = list(map(int, input().split()))

N_array.sort() # 정렬
answer_list = []
def dfs(array, depth):
    
    if depth == M:
        print(*answer_list)
        return
    
    for i in array:    
        if i not in answer_list:
            answer_list.append(i)
            dfs(array, depth+1)
            answer_list.pop() # 원위치




dfs(N_array, 0)