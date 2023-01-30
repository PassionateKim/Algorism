# 귀여운 라이언
# 복습 횟수:1, 01:00:00, 복습필요O
# ====오답 코드====#
import sys
si = sys.stdin.readline
N, K = map(int, si().split())
li = list(map(int, si().split())) # 라이언 1, 어피치 2

answer = sys.maxsize
check = 0
left = 0
right = 0

while left <= len(li) - 1 and right <= len(li) - 1:
    if li[right] == 1:
        check += 1
    
    if check == K:
        while left <= len(li)-1 and check == K:
            answer = min(answer, (right - left) + 1) 
            if li[left] == 1:
                check -= 1
            left += 1
    
    right += 1

if answer == sys.maxsize:
    print(-1)
else: print(answer)