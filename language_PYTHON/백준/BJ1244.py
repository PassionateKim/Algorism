# 스위치 켜고 끄기
import sys
si = sys.stdin.readline

N = int(si()) # 스위치 개수
arr = ['#'] + list(map(int, si().split())) # 켜진 스위치 1 , 꺼진 스위치 0

M = int(si()) # 횟수

for i in range(M):
    isSex, cardNum = map(int, si().split())
    
    # 성별 체크 하기
    cnt = 2
    tmp = cardNum # 3
    if isSex == 1: # 남자
        while cardNum <= N:
            if arr[cardNum] == 1:  # 켜져 있다면
                arr[cardNum] = 0 # 끄기
            else: # 꺼저 있다면
                arr[cardNum] = 1 # 켜기 
            cardNum = tmp * cnt
            cnt += 1
    
    else: # 여자
        if arr[cardNum] == 1:
            arr[cardNum] = 0 # 끄지
        else:
            arr[cardNum] = 1 # 켜기 
        
        
        left, right = cardNum, cardNum
        while True:
            left -= 1
            right += 1

            # 탈출 조건1. 범위 밖
            if left <= 0 or right > N: break

            # 탈출 조건2. 좌우 대칭 X
            if arr[left] != arr[right]: break

            # 왼쪽 바꾸기
            if arr[left] == 1:
                arr[left] = 0
            else:
                arr[left] = 1
            # 오른쪽 바꾸기
            if arr[right] == 1:
                arr[right] = 0
            else:
                arr[right] = 1

cnt = 0
for i in range(1, len(arr)):
    cnt += 1
    print(arr[i], end=" ")
    if cnt == 20:
        cnt = 0
        print() 
