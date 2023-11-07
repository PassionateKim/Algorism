import sys
si = sys.stdin.readline 
N = int(si())

student_score_list = []
for i in range(N):
    math, english = map(int, si().split())
    student_score_list.append((math, english))

index_dict = dict()

sorted_score_list = sorted(student_score_list, key= lambda x: (x[0], x[1]), reverse= True)


for index, value in enumerate(sorted_score_list):
    index_dict[value] = index + 1

for value in student_score_list:
    print(index_dict[value])
