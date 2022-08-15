# 2022-08-15
# 후보키
from itertools import combinations

def solution(relation):
    answer = 0
    answer_dict = dict()
    
    attr_length = len(relation[0])
    tmp_list = [i for i in range(attr_length)]

    # 완전 탐색 시작 1 ~ N
    for i in range(1, attr_length + 1):
        attr_cnt = i # 선택 attr 개수

        index_combi = list(combinations(tmp_list, 2)) # 속성 index combination
        
        
        for index in index_combi:
            tmp = []
            for item in relation:
                a = list()
                for i in index:
                    a.append(item[i])
                tmp.append(a)
            print(tmp)
            exit()

        for item in relation:
            for index in index_combi:
                print("index:",index)
                a = list()
                for i in index:
                    a.append(item[i])
                tmp.append(a)
            print(tmp)
            exit(0)


        # 각 인덱스들 마다 비교
        for index in index_combi:
            print("index:",index)
            
        exit()        

            


#     return answer

solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])

# 틀린 이유
# tuple을 어떻게 구현할지 몰랐음 (안에서 list comprehension을 쓸 줄 몰랐음.)
# issubset을 몰랐음





# def solution(relation):
#     row = len(relation)
#     col = len(relation[0])

#     #가능한 속성의 모든 인덱스 조합 
#     combi = []
#     for i in range(1, col+1):
#         combi.extend(combinations(range(col), i))
        
#     #유일성
#     unique = []
#     for i in combi:
#         tmp = [tuple([item[key] for key in i]) for item in relation]

#         if len(set(tmp)) == row:    # 유일성
#             put = True
            
#             for x in unique:
#                 if set(x).issubset(set(i)):  # 최소성
#                     put = False
#                     break
                    
#             if put: unique.append(i)
   
#     return len(unique)