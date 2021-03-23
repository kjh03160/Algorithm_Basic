# https://www.acmicpc.net/problem/20164
def answer(s, result):
    global min_v, max_v

    x = add_odd(s)
    if len(s) >= 3:
        for i in range(1, len(s)):
            for j in range(i + 1, len(s)):
                a = s[:i]
                b = s[i:j]
                c = s[j:]
                n = str(sum(map(int, [a, b, c])))
                answer(n, result + x)

    elif len(s) >= 2:
        n = str(int(s[0]) + int(s[1]))
        answer(n, result + x)
    elif len(s) == 1:
        min_v = min(min_v, result + x)
        max_v = max(max_v, result + x)


def add_odd(s):
    x = 0
    for i in s:
        if int(i) % 2 == 1:
            x += 1
    return x

import sys
input = sys.stdin.readline
n = input().rstrip()
min_v = float('inf')
max_v = 0
answer(n, 0)
print(min_v, max_v)
