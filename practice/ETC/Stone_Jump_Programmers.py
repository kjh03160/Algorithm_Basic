# https://programmers.co.kr/learn/courses/30/lessons/64062

def solution(stones, k):
    answer = 0

    min_friends = 1
    max_friends = 200000000 * 2 + 1

    while min_friends <= max_friends:
        mid = (min_friends + max_friends) // 2

        if able(mid, stones, k):
            min_friends = mid + 1
        else:
            max_friends = mid - 1
    return max_friends


def able(value, stones, k):
    now = 0
    for i in stones:
        if i - value < 0:
            now += 1
        else:
            now = 0
        if now >= k:
            return False
    return True


s = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
print(solution(s, k))
