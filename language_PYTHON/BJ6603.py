# 로또




def dfs(start, depth):
    if depth == 6:
        for i in range(6):
            print(answer[i], end=' ')
        print()
        return
    

    for i in range(start, len(set_s)):
        answer[depth] = set_s[i]
        
        dfs(i+1, depth+1)


while True:
    set_s = list(map(int, input().split()))
    answer = [0 for _ in range(13)]

    if set_s[0] == 0:
        break
    del set_s[0]

    dfs(0,0)
    print()

