# 숫자 카드 2
import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
cards = list(map(int,input().split()))
cards = sorted(cards)# 시간복잡도 O(NlogN)

cards_dict = defaultdict(int)
for i in range(len(cards)): # 시간복잡도 O(N)
    if cards[i] not in cards_dict:
        cards_dict[cards[i]] = 1 # 초기화
    else:
       cards_dict[cards[i]] += 1 
# print(cards_dict)
M = int(input())
cards_to_check = list(map(int,input().split()))


def Binary_search(array, target, start, end): 
    # 탐색 끝났음에도 값이 없는 경우
    if start > end:
        return 0 
    mid = (start + end) // 2
    if array[mid] == target:
        return 1
    elif array[mid] > target: # target이 작은 경우
        return Binary_search(array, target, start, mid-1)
    else: # target이 큰 경우
        return Binary_search(array, target, mid+1, end)

for i in cards_to_check:
    isExist = Binary_search(cards, i, 0, len(cards) -1)
    if isExist:
        cnt = cards_dict[i]
        print(isExist * cnt, end=" ")
    else:
        print(0, end=' ')

    
