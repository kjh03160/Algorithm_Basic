# boj.kr/1072

def answer(X, Y):
    target = int(Y * 100 / X)

    if target >= 99:
        return -1

    ans = 0
    start = 0
    end = 10 ** 9

    while start <= end:
        mid = (start + end) // 2

        if int((Y + mid) * 100 / (X + mid)) > target:
            end = mid - 1
        else:
            start = mid + 1
            ans = start

    return ans

import sys
input = sys.stdin.readline
x, y = map(int, input().split())
print(answer(x, y))