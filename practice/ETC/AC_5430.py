# boj.kr/5430

from collections import deque

def answer(p, X):
    q = deque(X)
    pop_back = False
    for cmd in p:
        if cmd == "R":
            pop_back = not pop_back
        elif cmd == "D" and len(q):
            if pop_back:
                q.pop()
            else:
                q.popleft()
        else:
            return 'error'
    result = list(q)
    if pop_back:
        result.reverse()
    return result


import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    p = input().rstrip()
    n = int(input())
    temp = input().rstrip().strip("[]").split(",")
    X = list(map(int, temp)) if temp[0] != "" else []
    result = answer(p, X)
    if result == "error":
        print(result)
    else:
        print("[", end="")
        print(*answer(p, X), sep=',', end="]\n")