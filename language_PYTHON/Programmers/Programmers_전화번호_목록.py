# 2022-08-08
# 2022-08-09
# 전화번호 목록
def solution(phone_book):
    phone_book_dict = dict()

    for i in phone_book:
        phone_book_dict[i] = 1

    for string in phone_book:
        tmp = ''
        for i in string:
            tmp += i
            if tmp in phone_book_dict and tmp != string:
                return False
    return True 


print(solution(["119", "97674223", "1195524421"]))
# 생각바꾸기 119를 기준으로 1195524421 비교 -> 1195524421 -> 119 비교
# <= 20 인 부분을 활용한 점도 기억하기