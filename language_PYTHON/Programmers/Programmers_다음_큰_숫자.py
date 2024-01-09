def solution(n):
    answer = 0

    binary_n = bin(n)
    binary_n = binary_n[2:]

    number_of_one = binary_n.count('1')

    count = 1
    while True:
        bigger = n + count
        binary_bigger = bin(bigger)
        binary_bigger = binary_bigger[2:]


        if( binary_bigger.count('1') == number_of_one ):
            answer = int(bigger)
            break

        count += 1

    return answer


solution(111)