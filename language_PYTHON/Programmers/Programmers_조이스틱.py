# 2022-08-19
def solution(name):
    answer = 0
    # 상하로 갯수 미리 세서 다 더해두기
    num_list = [min(abs(ord('A')- ord(n)), 26-abs(ord('A')-ord(n))) for n in name]
    answer += sum(num_list)
    min_move = len(name) - 1
    for i, c in enumerate(name):
        next_i = i+1
        while next_i < len(name) and name[next_i] == 'A':
            next_i += 1
        # 각 문자부터 A.. 문자가 있을 경우 몇번씩 조이 스틱을 쓰는지 체크한다.
        # 기존, 연속된 A의 왼쪽 시작 방식, 연속된 A의 오른쪽 시작 비교 및 갱신
        min_move = min(min_move, 2*i + len(name) - next_i, 2*(len(name)-next_i)+i)
    
    answer += min_move
    
    return answer

print(solution("BCAAABCD"))