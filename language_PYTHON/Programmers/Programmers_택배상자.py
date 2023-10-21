def solution(order):
    answer = 0

    n = len(order)

    container_belt = [i for i in range(n, 0, -1)]
    sub_belt = []

    while True:
        if len(container_belt) != 0:
            # container_belt 체크
            if (container_belt[-1] != order[answer]): # 만약 container
                # sub_belt 체크
                if len(sub_belt) != 0:
                    if (sub_belt[-1] > order[answer]): break

                    elif (sub_belt[-1] == order[answer]):
                        answer += 1
                        sub_belt.pop()
                    
                    else:
                        sub_belt.append(container_belt.pop())
                else:
                    sub_belt.append(container_belt.pop())

            else:
                answer += 1
                container_belt.pop()

        else:
            # 바로 sub_belt 체크
            if len(sub_belt) != 0:
                    if (sub_belt[-1] > order[answer]): break

                    elif (sub_belt[-1] == order[answer]):
                        answer += 1
                        sub_belt.pop()
                    
                    else:
                        sub_belt.append(container_belt.pop())
            else:
                break

    return answer

print(solution([1, 2, 5, 3, 4]))