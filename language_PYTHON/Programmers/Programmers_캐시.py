# 복습 횟수:0, 01:00:00, 복습필요O
from collections import deque
def solution(cacheSize, cities):
    cash = list()
    answer = 0
    if cacheSize == 0:
        answer = len(cities) * 5
        return answer
    
    lowerCities = []
    for city in cities:
        lowerCities.append(city.lower())


    for city in lowerCities:
        if city not in cash:
            if(len(cash) >= cacheSize):
                cash.pop(0)
            cash.append(city)
            answer += 5
        else:
            cityIndex = cash.index(city)
            cash.pop(cityIndex)
            cash.append(city)
            answer += 1

    return answer

solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])
