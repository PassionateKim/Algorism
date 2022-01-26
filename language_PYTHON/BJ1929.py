#1929번 소수 구하기  에라토스테네스의 체


#입력
M,N = input().split()


M = int(M)
N = int(N)


#숫자 배열
nums = []

for i in range(M,N+1):
    nums.append(i)

print(nums)


#배수들 다 제거하기
for i in range(1,N-M+1):
    print(nums.index(i))
