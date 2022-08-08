# 2022-08-08
# 전화번호 목록

from collections import defaultdict

def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book)
    print(list(zip(phone_book, phone_book[1:])))
    return answer
print(solution(["119", "97674223", "1195524421"]))