# 2022-08-19
# 2022-08-20
def solution(name):
    answer = 0
    name_list = list(name)
    min_cnt = len(name_list) - 1
    # 1. 각 자리수 체크
    for string in name_list:  
        cnt = min(abs(ord(string) - ord('A')), 26 - (ord(string) - ord('A')))
        answer += cnt
    
    # 2. min 체크
    for idx, string in enumerate(name_list):
        next = idx+1 # 왼쪽 
        # AAAA 같은 것이 있을 수 있으므로 체크
        while next < len(name_list) and name_list[next] == 'A':
            next += 1
        # 일반적인 경우, A의 왼쪽에서 탐색 시작하는 경우, A의 오른쪽에서 탐색 시작하는 경우
        min_cnt = min(min_cnt, (2*idx + len(name_list) - next), 2*(len(name_list)- next)+idx)

    answer += min_cnt

    return answer

print(solution("ABAAAAAAAAABB"))