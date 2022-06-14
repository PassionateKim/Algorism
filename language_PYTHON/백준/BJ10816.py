# 숫자 카드 2
import sys
from collections import defaultdict
input = sys.stdin.readline
cards_dict = defaultdict(int)

N = int(input())
N_cards = list(map(int, input().split()))
N_cards.sort()

for i in range(len(N_cards)): 
    if N_cards[i] not in cards_dict:
        cards_dict[N_cards[i]] = 1 # 초기화
    else:
        cards_dict[N_cards[i]] += 1 

M = int(input())
M_cards = list(map(int, input().split()))


for card in M_cards:
    if card in cards_dict.keys():
        print(cards_dict[card], end=" ")
    else:
        print(0, end=" ")
