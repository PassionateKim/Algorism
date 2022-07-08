# 약수

N = int(input())

divisor_list = list(map(int, input().split()))

divisor_list = sorted(divisor_list)

print(divisor_list[0] * divisor_list[-1])