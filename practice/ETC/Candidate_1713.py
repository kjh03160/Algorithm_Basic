# boj.kr/1713
def answer(n, K):
    on = [[0, float('inf')] for _ in range(101)]
    count = 0
    result = set()
    aging = 0
    for i in range(len(K)):
        std = K[i]
        if on[std][0]:
            on[std][0] += 1
        else:
            if len(result) != n:
                on[std] = [1, aging]
                aging += 1
            else:
                temp_up = float('inf')
                temp_age = float('inf')
                out = None
                for k in result:
                    up, age = on[k]
                    if up == temp_up:
                        if age < temp_age:
                            out = k
                            temp_age = age
                    elif up < temp_up:
                        temp_up = up
                        temp_age = age
                        out = k

                on[out] = [0, float('inf')]
                result.remove(out)
                on[std] = [1, aging]
                aging += 1

            result.add(std)
    return sorted(list(result))

import sys
input = sys.stdin.readline
n = int(input())
g = int(input())
K = list(map(int, input().split()))
print(*answer(n, K))


def answer(n, K):
    on = [0 for _ in range(101)]
    result = []
    for i in range(len(K)):
        std = K[i]
        if on[std]:
            on[std] += 1
        else:
            result.append(std)
            on[std] = 1
        out = None
        vote = float('inf')
        if len(result) > n:
            for k in range(len(result) - 1):
                if on[result[k]] < vote:
                    vote = on[result[k]]
                    out = result[k]
            result.remove(out)
            on[out] = 0

    return sorted(list(result))

import sys
input = sys.stdin.readline
n = int(input())
g = int(input())
K = list(map(int, input().split()))
print(*answer(n, K))