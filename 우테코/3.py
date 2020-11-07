def solution(money, expected, actual):
    answer = -1
    # 시작 배팅
    bet = 100
    # 게임 시작
    for i in range(len(actual)):
        # 졌을 때
        if expected[i] != actual[i]:
            money -= bet    # 배팅 금액 차감
            bet *= 2    # 다음 배팅 금액
        else:   # 이겼을때
            money += bet    # 배팅 금액 획득
            bet = 100   # 배팅 금액 초기화
        if money < bet: # 배팅 금액이 현재 가지고 있는 돈보다 적으면
            bet = money # 올인
    answer = money
    return answer