# https://www.acmicpc.net/problem/1158
from collections import deque
def answer(n, k):
    result = []
    q = deque()
    q.extend([i for i in range(1, n + 1)])
    count = 0
    while q:
        count += 1
        if count % k:
            q.append(q.popleft())
        else:
            result.append(str(q.popleft()))
    return result

import sys
input = sys.stdin.readline
n, k = map(int, input().split())
print("<" + ", ".join(answer(n, k)) + ">")