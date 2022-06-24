# 카카오 뉴스 클러스터링
from collections import defaultdict


def solution(str1, str2):
    
    answer = 0
    # 대소문자 차이 무시하기 -> 모두 대문자로 치환
    str1 = str1.upper()
    str2 = str2.upper()
    
    # 다중 집합으로 만들기
    A = defaultdict(int)
    B = defaultdict(int)
    andi = defaultdict(int)
    ori = defaultdict(int)

    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            # 이미 존재하는 경우
            if (str1[i] + str1[i+1]) in A.keys():
                A[(str1[i] + str1[i+1])] += 1
            # 존재하지 않는 경우
            else:
                A[(str1[i] + str1[i+1])] = 1
            
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            # 이미 존재하는 경우
            if (str2[i] + str2[i+1]) in B.keys():
                B[(str2[i] + str2[i+1])] += 1
            # 존재하지 않는 경우
            else:
                B[(str2[i] + str2[i+1])] = 1
    
    # 교집합 구하기
    for key in A.keys():
        if key in B.keys(): # 다중집합의 교집합
            andi[key] = min(A[key], B[key])

    
    # 합집합 구하기
    for key in A.keys():
        if key in B.keys(): # 다중집합의 합집합
            ori[key] = max(A[key], B[key])
        else: #일반집합의 합집합 -> 합집합은 구분이 필요함.
            ori[key] = A[key]
    
    # 합집합 B엔 있지만 A엔 없는 것 넣어주기 마무리
    for key in B.keys():
        if key not in A.keys():
            ori[key] = B[key]
   

    # 둘다 공집합인 경우
    if len(andi) == 0 and len(ori) == 0:
        return 65536 
    
    # 교집합 개수
    tmp1 = 0
    for i in andi.keys():
        if andi[i] != 1:
            tmp1 += andi[i]
        else:
            tmp1 += 1
    # 합집합 개수
    tmp2 = 0
    for i in ori.keys():
        if ori[i] != 1:
            tmp2 += ori[i]
        else:
            tmp2 += 1
    
    

    print(int(tmp1/tmp2 * 65536))
    return int(tmp1/tmp2 * 65536)

solution("abc", "abbb")