#백트레킹
#N과 M(1)


N,M = map(int,input().split())

num_list = [i+1 for i in range(N)]
check_list = [False] * N

print("num_list: ",num_list) 
arr = []

def dfs(count):
    #print(arr)
    if count == M:                                                                           
        #원소만 빼서 출력하는것 * 
        print(*arr)
        return
    
    for i in range(N):
        #print("for i : -------",i)
        if check_list[i]:
            #print("중복이라 continue",check_list)
            continue
    #i번쨰는 거쳐갈것이기에 True
        check_list[i] = True
        arr.append(num_list[i])
        #print("append 이후",arr)
        #print(check_list)
    #현재의 i를 기준으로 가지치기
        dfs(count + 1)
       # print("재귀함수끝", i,count)
        arr.pop()
        #print("pop이후",arr)
        check_list[i] = False

dfs(0)

