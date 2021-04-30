# boj.kr/1062
from itertools import combinations
def answer(W):
    global k
    if k - 5 < 0:
        return 0

    x = [False for _ in range(26)]
    for i in 'aticn':
        x[ord(i) - 97] = True

    no = list(combinations([i for i in range(len(x)) if not x[i]], k - 5))

    result = 0
    for case in no:
        for k in case:
            x[k] = True

        count = 0
        for word in W:
            flag = True
            for t in word:
                if not x[ord(t) - 97]:
                    flag = False
                    break
            if flag:
                count += 1

        for k in case:
            x[k] = False

        result = max(result, count)
    return result

import sys
input = sys.stdin.readline
n, k = map(int, input().split())
W = []
for _ in range(n):
    W.append(set(input().rstrip().strip('anti').strip('tica')))
print(answer(W))