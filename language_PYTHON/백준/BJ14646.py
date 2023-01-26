# 욱제는 결정장애야!!
# 복습 횟수:0, 01:00:00, 복습 필요O
import sys
from collections import defaultdict
si = sys.stdin.readline
N = int(si())

choice_list = list(map(int, si().split()))
check = 0
answer = 0
sticker_dict = defaultdict(int)
# O(NlogN) 안에 끝내야함
for choice in choice_list:
    if choice in sticker_dict:
        sticker_dict[choice] = 0
        check = check -1
    else:
        sticker_dict[choice] = 1
        check = check + 1
        
    answer = max(answer, check)
print(answer)