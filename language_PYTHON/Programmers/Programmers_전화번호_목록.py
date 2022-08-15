# 2022-08-08
# 2022-08-09
# 2022-08-11
# 2022-08-15
# 전화번호 목록
def solution(phone_book):
    phone_book = set(phone_book)

    for p in phone_book:
        tmp = ''
        for i in p:
            tmp += i
            if tmp in phone_book and tmp != p:
                return False        



    return True 


print(solution(["119", "97674223", "1195524421"]))
# 생각바꾸기 119를 기준으로 1195524421 비교 -> 1195524421 -> 119 비교
# <= 20 인 부분을 활용한 점도 기억하기