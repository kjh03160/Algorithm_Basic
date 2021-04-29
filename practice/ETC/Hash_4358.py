# boj.kr/4358
def answer(S, count):

    for i in sorted(list(S.keys())):
        print("%s %.4f" % (i, (S[i] / count) * 100))

import sys
input = sys.stdin.readline
S = {}
count = 0
while True:
    x = input().rstrip()
    if not x:
        break
    if S.get(x):
        S[x] += 1
    else:
        S[x] = 1
    count += 1
answer(S, count)