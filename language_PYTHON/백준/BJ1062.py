# 가르침
# 복습 횟수:1, 00:45:00, 복습필요O
import sys

n, k = map(int, input().split())

# k 가 5보다 작으면 어떤 언어도 배울 수 없음
if k < 5:
    print(0)
    exit()
# k 가 26이면 모든 언어를 배울 수 있음
elif k == 26:
    print(n)
    exit()

answer = 0
words = [set(sys.stdin.readline().rstrip()) for _ in range(n)]
learn = [0] * 26

# 적어도 언어 하나는 배우기위해 a,c,i,n,t 는 무조건 배워야함
for c in ('a', 'c', 'i', 'n', 't'):
    learn[ord(c) - ord('a')] = 1

def dfs(idx, cnt):
    global answer
    
    if cnt == k - 5:
        tmp = 0
        for word in words:
            flag = 1
            for c in word:
                if learn[ord(c) - ord('a')] == 0:
                    flag = 0
            if flag:
                tmp += 1
        answer = max(answer, tmp)
        return
    
    for i in range(idx, 26):
        if not learn[i]:
            learn[i] = 1
            dfs(i + 1, cnt + 1)
            learn[i] = 0

dfs(0, 0)
print(answer)