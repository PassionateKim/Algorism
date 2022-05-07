# 진정한 효도

graph = [list(map(int, input().split())) for _ in range(3)]

answer_list = []
answer_list2 = []
# 가로
for i in range(3):
    answer = []
    for j in range(3):
        answer.append(graph[i][j])
    answer_list.append(answer)
# 세로
for i in range(3):
    answer = []
    for j in range(3):
        answer.append(graph[j][i])
    answer_list.append(answer)


for items in answer_list:
    tmp = 0
    answer = []
    answer2 = []
    answer3 = []
    for j in items: # 1 1 3 인 경우
        answer.append(abs(j-1))
        answer2.append(abs(j-2))
        answer3.append(abs(j-3))
        
    answer_list2.append(min(sum(answer), sum(answer2), sum(answer3)))

print(min(answer_list2))




    
        