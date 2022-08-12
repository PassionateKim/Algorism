# 2022-08-05
# 2022-08-06
# 2022-08-12
# 튜플
import re
def solution(s):
    answer = []
    r = re.findall('{[\d,]+}', s)
    print(r)
    s = re.split(r'({[\d,]+})', s[1:-1])
    # # ", 제거"
    # for i in s:
    #     if i == ',':
    #         s.remove(i)

    # # 길이 순 정렬
    # s.sort(key = lambda x: len(x))
    # tmp = list()

    # for i in s:
    #     tmp.append(i.split(","))
    # # # 키로 저장하기
    # for i in tmp:
    #     for j in i:
    #         if int(j) not in answer:
    #             answer.append(int(j))
    
    # return answer

solution("{{20,111},{111}}")