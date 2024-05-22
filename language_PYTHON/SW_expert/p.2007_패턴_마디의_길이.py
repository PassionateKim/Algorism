N = int(input())

for test_case in range(1, N+1):
    string_input = input().rstrip() # "ABKOREAKOREABCDEFABCDEF"
    # 마디의 길이
    pattern_size = 1 
    for length in range(1, 11):
        parsed_pattern = string_input[:length]

        # 더 클 때 예외 처리
        if length * 2 > len(string_input):
            if parsed_pattern[0] != string_input[length]: continue

            pattern_size = length
            break
        
        next_paresed_pattern = string_input[length: length * 2] 
        if parsed_pattern == next_paresed_pattern:
            pattern_size = length
            break
    
    print(f"#{test_case} {pattern_size}")

            
        