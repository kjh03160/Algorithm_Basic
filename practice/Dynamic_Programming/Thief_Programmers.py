# https://programmers.co.kr/learn/courses/30/lessons/42897
def solution(money):
    DP = [0 for _ in range(len(money))]
    DP[0] = money[0]
    DP[1] = max(DP[0], money[1])
    for i in range(2, len(DP) - 1):
        DP[i] = max(DP[i - 1], DP[i - 2] + money[i])

    result = max(DP)
    DP = [0] * len(money)
    DP[0] = 0
    DP[1] = money[1]

    for i in range(2, len(money)):  # 마지막 집을 무조건 터는 경우
        DP[i] = max(DP[i - 1], money[i] + DP[i - 2])

    return max(result, max(DP))