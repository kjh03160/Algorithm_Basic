def max_profit(price_list, count):
    # count가 price_list의 길이보다 클 때, 인덱스 범위 벗어나는 것을 위해 0을 삽입
    if count > len(price_list) - 1:
        price_list.extend([0] * (count - len(price_list) + 1))

    # count까지 가면서, 해당 인덱스에 최댓값 기록하기
    for i in range(2, count + 1):
        # 현재 최댓값
        max_v = price_list[i]
        # 최댓값 탐색
        for j in range(1, i // 2 + 1):
            val = price_list[j] + price_list[i - j]
            if max_v < val:
                max_v = val
        # 최댓값 기록
        price_list[i] = max_v

    # count에서 얻을 수 있는 최댓값 리턴
    return price_list[count]



# 테스트
print(max_profit([0, 200, 600, 900, 1200, 2000], 5))
print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))
