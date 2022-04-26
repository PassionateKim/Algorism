#나무 자르기
import sys

N,M = map(int,input().split())
colonnade_list = list(map(int,sys.stdin.readline().rstrip().split()))

def Binary(start, end, m):
    #탈출조건
    if start > end:
        return end

    mid = (start + end) // 2

    wood = 0
    for height in colonnade_list:
        if mid < height: # 절단기 높이보다 나무 높이가 더 클 때
            wood += height - mid
     
    if wood >= m: # 잘린 나무가 더 많으면 절단기 높이를 올려야함
        return Binary(mid+1, end, m)
    else:
        return Binary(start, mid-1, m) #잘린 나무가 적으면 절단기 높이를 낮춰야함



print(Binary(1, max(colonnade_list), M))

