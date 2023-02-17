# 가르침
# 복습 횟수:0, 01:30:00, 복습필요O
# ==== 시간초과 코드 ==== #
import sys
si = sys.stdin.readline
N, K = map(int, si().split())
tmp = [list(map(str, si().strip())) for _ in range(N)]
string_set = list()
word = {'a', 'n', 't', 'i', 'c'}
if K < 5:
    print(0)
    exit()
elif K == 26:
    print(N)
    exit()

for string in tmp:
    string_set.append(string)

answer = 0
# a n t i c
using_word = dict()
for string in string_set:
    for s in string:
        if s == 'a' or s == 'n' or s == 't' or s == 'i' or s == 'c': continue

        using_word[s] = 1
def dfs(index, word: set):
    global answer
    if index == K - 5:
        tmp = 0
        for string in string_set:
            isTrue = True 
            for s in string:
                if s not in word:
                    isTrue = False
                    break
            if isTrue:
                tmp += 1
        answer = max(answer, tmp)
        return
    
    for key, val in using_word.items():
        if using_word[key]:

            word.add(key)
            using_word[key] = 0
            
            dfs(index + 1, word)
            
            word.remove(key)
            using_word[key] = 1

dfs(0, word)
print(answer)
# # ==== 정답코드 ==== #
# import sys

# n, k = map(int, input().split())

# # k 가 5보다 작으면 어떤 언어도 배울 수 없음
# if k < 5:
#     print(0)
#     exit()
# # k 가 26이면 모든 언어를 배울 수 있음
# elif k == 26:
#     print(n)
#     exit()

# answer = 0
# words = [set(sys.stdin.readline().rstrip()) for _ in range(n)]
# learn = [0] * 26

# # 적어도 언어 하나는 배우기위해 a,c,i,n,t 는 무조건 배워야함
# for c in ('a', 'c', 'i', 'n', 't'):
#     learn[ord(c) - ord('a')] = 1

# def dfs(idx, cnt):
#     global answer

#     if cnt == k - 5:
#         readcnt = 0
#         for word in words:
#             check = True
#             for w in word:
#                 if not learn[ord(w) - ord('a')]:
#                     check = False
#                     break
#             if check:
#                 readcnt += 1
#         answer = max(answer, readcnt)
#         return

#     for i in range(idx, 26):
#         if not learn[i]:
#             learn[i] = True
#             dfs(i, cnt + 1)
#             learn[i] = False


# dfs(0, 0)
# print(answer)
