# DNA
import sys
from collections import defaultdict
si = sys.stdin.readline
N, M = map(int, si().split())

# 1. Hamming_represent 찾기
Hamming_represent = []
answer = 0
ATGC_list = []

for i in range(N):
    tmp = list(map(str, si().rstrip()))
    ATGC_list.append(tmp)

for j in range(len(ATGC_list[0])): # 0 ~ 7
    # dict에 값 저장하기
    tmp_dict = defaultdict(int)
    for idx in range(len(ATGC_list)): # 0 ~ 4
        tmp = ATGC_list[idx][j]
        tmp_dict[tmp] =  tmp_dict[tmp] + 1

    # 중복이라면 사전 순으로 와야 하므로
    candidate = []
    for key, value in tmp_dict.items():
        if value == max(tmp_dict.values()):
            candidate.append(key)
    
    candidate.sort()
    Hamming_represent.append(candidate[0])


# 2. Hamming distance 더하기
for i in range(len(ATGC_list)):
    tmp = 0
    for string, compare in zip(ATGC_list[i], Hamming_represent):
        if (string != compare):
            tmp += 1 
    answer += tmp

# 정답 출력하기
for string in Hamming_represent:
    print(string, end="")
print()
print(answer)