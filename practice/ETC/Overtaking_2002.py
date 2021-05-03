# boj.kr/2002
from collections import deque
def answer(IN, OUT):
    IN = deque(IN)
    OUT = deque(OUT)
    result = 0
    while OUT:
        now = OUT.popleft()
        x = IN.popleft()

        out = 0
        flag = False
        while x != now:
            out += 1
            flag = True
            IN.append(x)
            x = IN.popleft()

        while IN and len(OUT) != out:
            IN.append(IN.popleft())
            out += 1

        if flag:
            result += 1
    return result

import sys
input = sys.stdin.readline
n = int(input())
IN = [input().strip() for _ in range(n)]
OUT = [input().strip() for _ in range(n)]
print(answer(IN, OUT))