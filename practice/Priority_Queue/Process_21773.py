
# https://www.acmicpc.net/problem/21773
import heapq
def answer(P):
    global t

    heapq.heapify(P)
    end = 0
    while P:
        prio, pid, duration = heapq.heappop(P)

        duration -= 1
        print(pid)
        end += 1

        if end == t:
            return

        if not duration:
            continue

        prio += 1

        heapq.heappush(P, (prio, pid, duration))


import sys
input = sys.stdin.readline
t, n = map(int, input().split())
P = []
for _ in range(n):
    pid, duration, priority = map(int, input().split())
    P.append((-priority, pid, duration))
answer(P)