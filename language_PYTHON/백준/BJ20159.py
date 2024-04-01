import sys
si = sys.stdin.readline 
answer = 0

N = int(si())
card_list = list(map(int, si().split()))

prefix_sum_list = [0 for i in range(N + 1)]
prefix_odd_list = [0 for i in range(N + 1)]
prefix_even_list = [0 for i in range(N + 1)]

for i in range(1, N + 1):
    prefix_sum_list[i] = prefix_sum_list[i - 1] + card_list[i - 1]

for i in range(1, N + 1, 2):
    prefix_odd_list[i] = prefix_odd_list[i - 2] + card_list[i - 1]

for i in range(2, N + 1, 2):
    prefix_even_list[i] = prefix_even_list[i - 2] + card_list[i - 1]    

# 0 일 때
sumi = 0
for i in range(0, N, 2):
    sumi = sumi + card_list[i]
    answer = max(answer, sumi)

# 1 일 때
sumi = 0
for i in range(1, N, 2):
    sumi = sumi + card_list[i]
    answer = max(answer, sumi)

# 내가 밑장을 가지는 경우
count = N // 2
for i in range(1, count): # 1, 2, 3, 4
    other_sumi = prefix_even_list[(i-1) * 2] + (prefix_sum_list[2*i + 1] - prefix_sum_list[2*i - 1]) + prefix_odd_list[N-1] - prefix_odd_list[2*i + 1]
    answer = max(answer, prefix_sum_list[N] - other_sumi)
    
# 상대에게 밑장을 주는 경우
for i in range(1, count):
    if i == 1:
        sumi = prefix_even_list[2*i] - prefix_even_list[2*(i-1)] + prefix_even_list[(count - 1) * 2] - prefix_even_list[2*i]
    else:
        sumi = prefix_odd_list[2*i - 1] + prefix_even_list[2*i] - prefix_even_list[2*(i-1)] + prefix_even_list[(count - 1) * 2] - prefix_even_list[2*i]
    answer = max(answer, sumi)

print(answer)