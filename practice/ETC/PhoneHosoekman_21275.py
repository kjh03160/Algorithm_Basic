# https://www.acmicpc.net/problem/21275
def to_int(S, i, asc):
    a = 0
    for k in range(len(S) - 1, -1, -1):
        if asc[S[k]] >= i:
            return -1
        a += asc[S[k]] * (i ** (len(S) - k - 1))
        if a >= 2 ** 63:
            return -1
    return a


def answer(A, B):
    asc = {chr(i + 87): i for i in range(10, 36)}
    asc.update({str(i): i for i in range(10)})
    result = []

    for i in range(2, 37):
        for j in range(2, 37):
            if i != j:
                a = to_int(A, i, asc)
                b = to_int(B, j, asc)
                if a == -1 or b == -1:
                    continue

                if a == b:
                    result.append((a, i, j))
                if len(result) >= 2:
                    print('Multiple')
                    return
    if result:
        print(*result[0])
        return
    print('Impossible')

import sys
input = sys.stdin.readline
A, B = input().split()
answer(A, B)