#연산자 끼워넣기
N = int(input())
A_array = list(map(int, input().split()))
calculation = list(map(int, input().split()))
answer = [-10**9-1, 10**9+1]

def DFS(sum, plus, minus, multi, div, depth):
    print(sum, plus, minus, multi, div, depth)
    # 탈출조건
    if depth == len(A_array) - 1:
        if answer[0] < sum:
            answer[0] = sum

        if answer[1] > sum:
            answer[1] = sum 
        return   
    if plus:
        DFS(sum + A_array[depth+1], plus-1, minus, multi, div, depth+1)
    if minus:
        DFS(sum-A_array[depth+1], plus, minus-1, multi, div, depth+1)
    if multi:
        DFS(sum*A_array[depth+1], plus, minus, multi-1, div, depth+1)
    if div:
        if sum < 0:
            DFS(-(-sum//A_array[depth+1]), plus, minus, multi, div-1, depth+1)            
        else:
            DFS(sum//A_array[depth+1], plus, minus, multi, div-1, depth+1)

# 덧셈, 뺼셈, 곱셈, 나눗셈
DFS(A_array[0], calculation[0], calculation[1], calculation[2], calculation[3], 0)
print(answer[0])
print(answer[1])