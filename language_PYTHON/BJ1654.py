# 랜선 자르기
import sys

K, N = map(int,input().split())
lines_list = [int(input()) for _ in range(K)]

def Binary(target, start, end):
    # 탈출 조건
    if start > end:
        print(end)
        return

    mid = (start + end) // 2
    
    line = 0
    for i in lines_list: #입력값 리스트 원소 하나씩 비교해서 넣어주기
        tmp = i // mid
        line += tmp
        
    if line < target: # 값이 작으면 나누는 수가 작아져야 하므로
        return Binary(target, start, mid-1) # 왼쪽
    else:
        return Binary(target, mid+1, end) # 오른쪽

Binary(N, 1, max(lines_list))