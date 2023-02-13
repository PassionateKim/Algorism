# 애너그램
# 복습 횟수:0, 00:30:00, 복습필요O
# import sys
# si = sys.stdin.readline
# N = int(si())

# def dfs(current, li: list):

#     if current == len(input):
#         word_set.add("".join(li))
#         return
    
#     for i in range(len(input)):
#         if visited[i] == 0:
#             li.append(input[i]) # 추가
#             visited[i] = 1 # 방문처리
#             dfs(current + 1, li)
#             li.pop() # 초기화
#             visited[i] = 0 # 초기화

#     return

# for i in range(N):
#     word_list = list()
#     word_set = set() 

#     input = list(map(str, si().rstrip()))
#     input.sort()
#     visited = [0 for _ in range(len(input))]

#     dfs(0, [])
#     word_list = list(word_set)
#     word_list.sort()
#     for word in word_list:
#         print(word)

import sys
si = sys.stdin.readline
def dfs(cnt):
    if cnt == len(word):
        print("".join(answer))
        return
    
    for k in visited:
        if visited[k]:
            visited[k] -= 1
            answer.append(k)
            dfs(cnt + 1)
            visited[k] += 1
            answer.pop()
n = int(si())
for _ in range(n):
    word = sorted(list(map(str, si().strip())))
    visited = {}
    answer = []


    for i in word:
        if i in visited:
            visited[i] += 1
        else:
            visited[i] = 1

    dfs(0)