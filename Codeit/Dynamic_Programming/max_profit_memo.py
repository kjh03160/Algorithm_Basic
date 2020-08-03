"""
솔희는 학원 쉬는 시간에 친구들을 상대로 새꼼달꼼 장사를 합니다. 그러다 문뜩, 갖고 있는 새꼼달꼼으로 벌어들일 수 있는 최대 수익이 궁금해졌는데요...

가능한 최대 수익을 리턴시켜 주는 함수 max_profit을 작성해 보세요. max_profit은 파라미터로 개수별 가격이 정리되어 있는 리스트 price_list와 판매할 새꼼달꼼 개수 count를 받습니다.

예를 들어 price_list가 [100, 400, 800, 900, 1000]이라면,

새꼼달꼼 1개에 100원
새꼼달꼼 2개에 400원
새꼼달꼼 3개에 800원
새꼼달꼼 4개에 900원
새꼼달꼼 5개에 1000원
이렇게 가격이 책정된 건데요. 만약 오늘 솔희가 새꼼달꼼 5개를 판매한다면 최대로 얼마를 벌 수 있을까요?

한 친구에게 3개 팔고 다른 친구에게 2개를 팔면, 800 + 400800+400을 해서 총 1200원의 수익을 낼 수 있겠죠.
"""


def max_profit_memo(price_list, count, cache):
    # base case
    if count == 1:
        # memo
        cache[count] = price_list[1]
        return price_list[1]
    # memo한 값이 있으면 바로 리턴
    if count in cache:
        return cache[count]

    # 최댓값 찾기 위한 변수 설정
    max_v = 0

    # count가 price_list 범위 내라면,
    if count < len(price_list):
        max_v = price_list[count]

    # count // 2 까지 반복문을 돌면서 최댓값 찾기
    for i in range(1, count // 2 + 1):
        val = max_profit_memo(price_list, count - i, cache) + max_profit_memo(price_list, i, cache)
        if max_v < val:
            max_v = val

    # 최댓값 기록
    cache[count] = max_v
    return cache[count]

def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)


# 테스트
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))
