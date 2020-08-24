# 1170원을 거슬러 주기 위해서는 500원 2개, 100원 1개, 50원 1개, 10원 2개를 줄 수 있기 때문에 6을 리턴
# 동전의 조합은 항상 500원, 100원, 50원, 10원이라고 가정

def min_coin_count(value, coin_list):
    coin = 0
    coin_list.sort(reverse=True)
    index = 0
    while value != 0 and index < len(coin_list):
        if value >= coin_list[index]:
            coin += value // coin_list[index]
            value = value % coin_list[index]

        index += 1
    return coin
# 테스트
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))