# boj.kr/17822

def remove_dup(P):
    global n, m
    check = [[0 for _ in range(m)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(m):
            if P[i][j] == 0:
                continue
            value = P[i][j]

            # 이미 지워진 것 -> 이전 값 가져옴
            if value == -1:
                value = check[i][j]

            # 깉은 원판 내 인접
            if value == P[i][(j + 1) % m]:
                adj = (j + 1) % m
                check[i][j] = value
                check[i][adj] = value
                P[i][j] = -1
                P[i][adj] = -1
            if value == P[i][j - 1]:
                check[i][j] = value
                check[i][j - 1] = value
                P[i][j] = -1
                P[i][j - 1] = -1

            # 서로 다른 원판 간 인접
            if i + 1 < n + 1 and value == P[i + 1][j]:
                check[i][j] = value
                check[i + 1][j] = value
                P[i][j] = -1
                P[i + 1][j] = -1

            elif i - 1 != 0 and value == P[i - 1][j]:
                check[i][j] = value
                check[i - 1][j] = value
                P[i][j] = -1
                P[i - 1][j] = -1


def rotate(P, x, d):
    global n, m
    for i in range(x, n + 1, x):
        # 시계
        if d == 0:
            zero = P[i][-1]
            for j in range(m - 1, 0, -1):
                P[i][j] = P[i][j - 1]
            P[i][0] = zero
        # 반시계
        else:
            zero = P[i][0]
            for j in range(m - 1):
                P[i][j] = P[i][j + 1]
            P[i][-1] = zero


def sum_and_check_deleted(P):
    global n, m
    result = 0
    count = 0
    is_deleted = False
    for i in range(1, n + 1):
        for j in range(m):
            if P[i][j] > 0:
                count += 1
            if P[i][j] < 0:
                is_deleted = True
                P[i][j] = 0
            result += P[i][j]
    return is_deleted, count, result


def cal(P, result, count):
    global n, m
    avg = result / count
    for i in range(1, n + 1):
        for j in range(m):
            if P[i][j] > avg and P[i][j]:
                P[i][j] -= 1
                result -= 1
            elif P[i][j] < avg and P[i][j]:
                P[i][j] += 1
                result += 1
    return result


def answer(P, T):
    result = 0
    count = 0
    for x, d, k in T:
        result = 0

        for _ in range(k):
            rotate(P, x, d)

        remove_dup(P)

        is_deleted, count, result = sum_and_check_deleted(P)

        if count == 0 or is_deleted:
            continue
        result = cal(P, result, count)

    return result if count else 0


import sys

input = sys.stdin.readline
n, m, t = map(int, input().split())
P = [[]] + [list(map(int, input().split())) for _ in range(n)]
T = [list(map(int, input().split())) for _ in range(t)]
print(answer(P, T))
