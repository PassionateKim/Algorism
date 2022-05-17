# 정수 삼각형
import sys
input = sys.stdin.readline

# 2차원배열에 값을 넣어야할 거같은데..?
N = int(input())
dp = [0] * N
triangle_list = []

# triangle_list 넣기 2차원 배열
for i in range(N):
    triangle_list.append(list(map(int, input().split())))

#dp 생성하기
dp[0] = triangle_list[0][0] # 기존 값 넣어두기

for x in range(len(triangle_list)-1): # [8,1,0]
    tmp = list() # 임시로 만들어둬야함.. 값이 겹침 -> 주소 복사 x를 위해 append
    for i in dp: # dp 복사하자
        tmp.append(i)
    print(tmp)

    # 다음 회차 배열tmp를 돌면서 dp 수정하기
    for idx in range(len(triangle_list[x+1])): # 0 1 (3 8)  
        if idx == 0: # 첫번째
            dp[0] = tmp[0] + triangle_list[x+1][0]

        elif idx == len(triangle_list[x+1]) - 1: # 마지막 1 
            dp[idx] = tmp[idx-1] + triangle_list[x+1][idx]

        else: # 중간에 있는 경우 
            dp[idx] = max(tmp[idx-1],tmp[idx]) + triangle_list[x+1][idx]

print(max(dp))
            
        

