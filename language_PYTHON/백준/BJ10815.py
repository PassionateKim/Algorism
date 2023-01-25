# 숫자 카드
# 복습 횟수:0, 00:30:00, 복습필요O
import sys
si = sys.stdin.readline
N = int(si())
my_card = list(map(int, si().split()))
my_card.sort()
mini = min(my_card)
maxi = max(my_card)

answer = []
M = int(si())
check_list = list(map(int, si().split()))


def binary(start, end, target):
    while start <= end:
        idx = (start + end) // 2
        mid = my_card[idx]

        if mid <= target:
            if mid == target:
                return 1
            start = idx + 1
        else:
            end = idx - 1

    return 0

for check in check_list:
    val = binary(0, len(my_card) -1, check)
    answer.append(val)

print(*answer)
