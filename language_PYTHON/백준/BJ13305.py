import sys
si = sys.stdin.readline

N = int(si())
distance_list = list(map(int, si().split()))
city_list = list(map(int, si().split()))
answer = 0
sum_distance = 0
before_city = city_list[0]

for distance, city in zip(distance_list, city_list):
    if (before_city <= city):
        sum_distance += distance
    else:
        answer += (before_city * sum_distance)
        before_city = city
        sum_distance = distance

answer += (before_city * sum_distance)
print(answer)