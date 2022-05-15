# 소수의 연속합
# 하나 이상의 연속된 소수의 합으로 나타낼 수 있는 방법의 개수

N = int(input())
a = [False, False] + [True] * (N-1)
prime_list = []
answer = 0
# 범위 이하의 소수 list 만들기
for i in range(2, N+1):
    if a[i]:
        prime_list.append(i)
        for j in range(2*i, N+1, i):
            a[j] = False

# for i in range(2, N+1):
#     flag = 0
#     for j in range(2, i):
#         if i % j == 0:
#             flag = 1
#             break
#     if flag == 0:
#         prime_list.append(i)

# 1인 경우(본인이 소수인 경우) 
if N in prime_list:
    answer += 1

# 더하는 소수의 개수 cases 
for cases in range(2, len(prime_list)): 
    total = len(prime_list)-1 # 총 개수
    check = total - cases + 1 # 체크 횟수
    cnt = 0

    #index의 끝을 고려한 while문 범위
    while cnt <= check - cases: # 체크 범위 index 0부터 쭉 순서대로
        sum = 0 # 하나 이상의 연속된 소수의 합
        for i in range(cnt, cases + cnt): 
            sum = sum + prime_list[i]
        
        if sum == N: # 다더했을 때 소수의 합으로 나타낼 수 있는 경우
            answer += 1 # answer 에 + 1 
            break #나가주기
            
        elif sum > N: # 초과할 경우 그 다음은체크할 필요X 이므로 
            break # 나가기

        cnt += 1 #체크했으면 다음칸으로

print(answer)  
        





