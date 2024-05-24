import heapq
T = int(input())

for test_case in range(T):
    N, K = map(int, input().split())
    input_list = list(map(int, input().split()))
    input_list.sort()

    diff = N - K 

    prefix_left_sum = [0 for i in range(len(input_list))]    
    prefix_right_sum = [0 for i in range(len(input_list))]    

    prefix_left_sum[0] = input_list[0]
    prefix_right_sum[-1] = input_list[-1]
    for i in range(len(input_list) - 1):
        prefix_left_sum[i+1] = prefix_left_sum[i] + input_list[i+1]

    for i in range(len(input_list) -1, 0, -1):
        prefix_right_sum[i-1] = prefix_right_sum[i] + input_list[i-1]

    # i = left에서 얼마나 제거하는지
    answer = 1000000000
    for i in range(diff + 1):
        right_cut = diff - i # 4 
        parsed_list = input_list[i: N + - right_cut]
        c = max(parsed_list) - min(parsed_list)

        answer = min(c, answer)

    print(f"#{test_case + 1} {answer}") 