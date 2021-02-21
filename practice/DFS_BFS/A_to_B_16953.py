# https://www.acmicpc.net/problem/16953

from collections import deque
def answer(A, B):
    q = deque()
    q.append((A, 0))
    result = float('inf')
    while q:
        num, count = q.popleft()

        if num > B:
            continue

        if count >= result:
            break

        if num == B:
            result = min(result, count)
            continue

        q.append((num * 2, count + 1))
        q.append((num * 10 + 1, count + 1))
    return result + 1 if result != float('inf') else -1

import sys
input = sys.stdin.readline
A, B = map(int, input().split())
print(answer(A, B))