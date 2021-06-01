# boj.kr/21775

from collections import deque
def answer(T, C):
    global n

    is_not_free = set()
    cards = deque(C)
    turn = deque(T)

    on_hand = [None for _ in range(n + 1)]

    while turn:
        now = turn.popleft()

        if on_hand[now]:
            cid, op, num = on_hand[now]
            print(cid)
            if num not in is_not_free:
                is_not_free.add(num)
                on_hand[now] = None

        else:
            c = cards.popleft()
            print(c[0])
            if c[1] == "next":
                continue
            elif c[1] == "acquire":
                cid, op, num = c
                if num not in is_not_free:
                    is_not_free.add(num)
                else:
                    on_hand[now] = c
            else:
                cid, op, num = c
                is_not_free.remove(num)


import sys
input = sys.stdin.readline
n, t = map(int, input().split())
T = list(map(int, input().split()))
C = [input().split() for _ in range(t)]
answer(T, C)