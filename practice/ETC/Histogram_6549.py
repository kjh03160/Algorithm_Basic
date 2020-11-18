# https://www.acmicpc.net/problem/6549

def answer(hist):
    hist = [0] + hist + [0]

    last_hist = [0]
    area = 0
    for i in range(1, len(hist)):
        while last_hist and hist[i] < hist[last_hist[-1]]:
            index = last_hist.pop()
            area = max(area, (i - 1 - last_hist[-1]) * hist[index])

        last_hist.append(i)
    return area

import sys
input = sys.stdin.readline
test = []
while True:
    temp = list(map(int, input().split()))[1:]
    if not len(temp):
        break
    test.append(temp)
for i in range(len(test)):
    print(answer(test[i]))