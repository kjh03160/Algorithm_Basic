def consecutive_sum(start, end):
    # base case
    if end == start:
        return start

    # 부분 문제를 반으로 나눠주기 위해서 문제의 정중앙을 정의한다 (Divide)
    mid = (start + end) // 2

    # 각 부분 문제를 재귀적으로 풀고(Conquer), 부분 문제의 답을 서로 더한다(Combine).
    return consecutive_sum(start, mid) + consecutive_sum(mid + 1, end)

# 테스트
print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))

"""
일반적인 재귀적으로 푸는 것과 무엇이 다른가?
분할 정복은 깊이가 log N으로 된다.
하지만 일반적인 재귀로 풀면 깊이는 N으로 된다.
파이썬에서 정한 max_depth는 1000, 그러므로 분할 정복으로 하면 더 큰 숫자를 연산할 수 있다!
"""