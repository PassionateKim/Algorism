# 2023-07-13
# 복습 횟수:1, 00:30:00, 복습필요:* (3번째에 맞으면 끝)
def solution(cacheSize, cities):
    answer = 0
    cash_table = []
    lower_cities = []
    for city in cities:
        city = city.lower()
        lower_cities.append(city)

    for city in lower_cities:
        if city not in cash_table:
            if cacheSize != 0:
                if len(cash_table) >= cacheSize:
                    cash_table.pop(0)

                cash_table.append(city)
            answer += 5
        else:
            cash_table.pop(cash_table.index(city))
            cash_table.append(city)
            answer += 1

    return answer

print(solution(0, ["Jeju", "Jeju", "Jeju", "Jeju", "Jeju"]))
