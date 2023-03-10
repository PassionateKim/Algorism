# 복습 횟수:1, 01:00:00, 복습필요O
def solution(user_ids, banned_ids):
    answer = set()

    def dfs(li : list, index):
        
        if len(li) == len(banned_ids):
            answer.add(tuple(sorted(li)))
            return

        for i in range(len(user_ids)):
            if user_ids[i] not in li:
                isTrue = True
                # 체크 
                if len(user_ids[i]) != len(banned_ids[index]): continue

                for user, ban in zip(user_ids[i], banned_ids[index]):
                    if user != ban and ban != '*':
                        isTrue = False
                        break
                
                if isTrue:
                    li.append(user_ids[i])
                    dfs(li, index + 1)
                    li.pop()

        return

    dfs([], 0)

    return len(answer)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))