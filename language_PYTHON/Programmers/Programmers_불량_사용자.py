# 복습 횟수:0, 02:30:00, 복습필요O

# == 시간초과 코드 == #
# 차이: 미리 구해놓고 탐색을 해서 dfs 시간 차이를 줄인 것이 정답 코드임
# def dfs(li: list, visited: list, user_list: list, ban_list: list):
#     index = len(li)
#     if index == len(ban_list):
#         li = tuple(sorted(li))
#         answer.add(li)
#         return
    
#     for i in range(len(user_list)):
#         if user_list[i] not in li:
#             isTrue = True
#             for j in range(len(ban_list)):
#                 if visited[j] == 0:
#                     if len(user_list[i]) != len(ban_list[j]): 
#                         isTrue = False
#                     else:
#                         for user_str, ban_str in zip(user_list[i], ban_list[j]):
#                             if user_str != ban_str and ban_str != '*':
#                                 isTrue = False
#                                 break
#                     if isTrue and user_list[i] not in li:
#                         li.append(user_list[i])
#                         visited[j] = 1
#                         dfs(li, visited, user_list, ban_list)
#                         li.pop()
#                         visited[j] = 0

#     return

# def solution(user_id, banned_id):
#     global answer
#     answer = set()

#     visited = [0 for _ in range(len(banned_id))]
#     dfs([], visited, user_id, banned_id)
#     return len(answer)

def solution(user_ids, banned_ids):
    bad_possible_users = [] # banned_ids와 같은 길이를 갖는다. 각 인덱스에 들어 있는 값들에는, bannded_ids 에 각 인덱스에 있는 `불량 사용자의 조건` 에 맞는 모든 사용자들이 들어있다.

    # `i번의 불량 사용자의 조건` 에 부합하는 응모자의 아이디만 temp 배열에 넣어준다.
    # 이 배열을 bad_possible_users 배열에 넣어준다.
    for banned_id in banned_ids:
        temp = []
        for user_id in user_ids:
            banned_id_length = len(banned_id)
            if banned_id_length == len(user_id):
                flag = True
                for idx in range(banned_id_length):
                    if banned_id[idx] != user_id[idx] and banned_id[idx] != '*':
                        flag = False
                        break

                # 조건에 해당하는 유저만 temp배열에 넣어준다        
                if flag:
                    temp.append(user_id)

        bad_possible_users.append(temp)

    # 각 bad_possible_users에 있는 각 단계의 불량사용자 후보군들을 ans 배열에 넣어준다.
    # 각 단계에서는 1명의 불량 사용자 만 뽑는다.
    # 1명을 뽑고, 그 뽑았을 때를 기준으로 다음 단계 불량 사용자를 뽑고,
    # 그 후 그 1명을 빼고나서 다음 후보자를 뽑는 식으로 불량사용자 set을 만든다. 
    ans = []
    def dfs(answers, level):
        if level == len(banned_ids):
            ans.append(answers)
            return

        for value in bad_possible_users[level]:
            if value not in answers:
                answers.append(value)
                dfs(answers[:], level + 1)
                answers.pop()

    dfs([], 0)

    # ans에는 불량사용자 set을 나타내는 배열이 들어있는데, 중복을 허용하지 않기 위해,
    # 그 값들을 string 값으로 바꾸고 그 길이로 반환을 한다
    ans = set(''.join(sorted(x)) for x in ans)


    return len(ans)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))