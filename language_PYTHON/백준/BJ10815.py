# 숫자 카드
# 복습 횟수:1, 00:15:00, 복습필요X
import sys
si = sys.stdin.readline
N = int(si())
my_card = list(map(int, si().split()))
my_card.sort()
M = int(si())
check_list = list(map(int, si().split()))

answer = []

def binary(start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if my_card[mid] == target:
            return 1

        if my_card[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return 0

for check in check_list:
    val = binary(0, len(my_card) - 1, check)
    answer.append(val)

print(*answer)