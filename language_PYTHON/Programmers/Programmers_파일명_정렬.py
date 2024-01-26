from collections import defaultdict

def solution(files):
    
    first_dict = defaultdict(str)
    for i in range(len(files)):
        first_dict[i] = files[i]
    
    head_list = [] # [["amg", 0], ["amg", 1], ["img", 2], ["img", 3], ["amg", 4], ["amg", 5]] 
    number_list = []

    for i in range(len(files)):
        head = ""
        cursor = 0
        file = files[i]
        while True:
            head_str = str(file[cursor]).upper()
            
            if(head_str.isdigit()):
                break
            
            head = head + head_str
            
            cursor += 1

        head_list.append([head, i, first_dict[i]])
    # head 기준으로 구분하기
    head_list.sort(key = lambda x : x[0])
   
    second_dict = defaultdict(str)

    for i in range(len(head_list)):
        key = head_list[i][1]
        second_dict[i] = first_dict[key]

    visited = [0 for i in range(len(files))]
    

    count = 1

    # 중복 체크 로직   
    duple_dict = defaultdict(list)
    for i in range(len(files)):
        duple_dict[head_list[i][0]].append(head_list[i][1])


    print(duple_dict)

    key = duple_dict.keys()

    for index, value in enumerate(head_list):
        if value[0] in key and len(duple_dict[value[0]]) >= 2:
            visited[index] = value[0]
    
    answer_list = []

    index = 0
    length = 0
    while index != len(files):
        
        if visited[index] != 0:
            number_list = []
            check = visited[index]
            while index != len(files) and visited[index] == check:
                target = head_list[index][2]
                number_str = ""
                flag = 0
                for s in target:
                    if(len(number_str) == 5):
                        break

                    if(flag == 1 and not s.isdigit()):
                        break

                    if(s.isdigit()):
                        number_str = number_str + s
                        flag = 1

                number = int(number_str)

                number_list.append([number, head_list[index][2]])     

                index += 1
            number_list.sort(key = lambda x: x[0])
            answer = [item[1] for item in number_list]

            answer_list.extend(answer)
            length = index
            # ['a10sgr.td', 'a1234.t', 'A-10 Thunderbolt II', 'asfa124.tgc', 'B-50 Superfortress', 'F014F33.', 'F0213.TXT', 'F13456.png', 'F22414', 'f31013', 'F-5 Freedom Fighter', 'F-14 Tomcat']

        else:
            answer_list.append(head_list[index][2])
            length = length + 1
            index = index + 1
                
    return answer_list


print(solution(["asfa124.tgc", "a1234.t", "a10sgr.td", "F13456.png", "F22414", "f31013", "F014F33.", "F0213.TXT","F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))

# print(solution(["F13456.png", "F22414", "f31013", "F014F33.", "F0213.TXT"]))

# print(solution( ["F-5AD34 Freedom Fighter", "B-50A3 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
# print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
# solution(["amg10.png", "amg12.png", "bb23", "img1.png", "img2.png", "amg010.png", "amg0010.png", "amg0310.png", "amg310.png", "amg5.png"])
# "amg10.png" "amg010.png", "amg0010.png", "amg12.png", "img1.png", "img2.png"