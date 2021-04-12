# boj.kr/18222

def answer(k):
    count = 0
    while k:
        count += k % 2
        k = k >> 1

    if count % 2:
        return 1
    return 0

import sys
input = sys.stdin.readline
n = int(input()) - 1
print(answer(n))