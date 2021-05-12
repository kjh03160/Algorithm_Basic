# https://www.acmicpc.net/problem/20366

def answer(n, H):
    H.sort()
    result = float('inf')

    # 바깥쪽
    for outer_a in range(n - 3):
        for outer_b in range(outer_a + 3, n):
            inner_a, inner_b = outer_a + 1, outer_b - 1
            # 안쪽
            while inner_a < inner_b:
                inner = H[inner_a] + H[inner_b]
                outer = H[outer_a] + H[outer_b]

                diff = inner - outer
                result = min(abs(diff), result)

                if diff > 0:
                    inner_b -= 1
                else:
                    inner_a += 1
    return result
    pass

import sys
input = sys.stdin.readline
n = int(input())
H = list(map(int, input().split()))
print(answer(n, H))
