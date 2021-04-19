# boj.kr/1963

import math
def get_prime():
    is_prime = [True for _ in range(10001)]
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2,  int(math.sqrt(len(is_prime))) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, len(is_prime), i):
            is_prime[j] = False
    return is_prime

from collections import deque

def print_answer(a, b, primes):
    q = deque()
    visited = [False for _ in range(10001)]
    visited[a] = True

    q.append((a, 0))

    while q:
        num, count = q.popleft()

        if num == b:
            print(count)
            return

        x = str(num)
        for i in range(4):
            for j in map(str, range(10)):
                if i == 0 and j == '0':
                    continue
                num = int(x[:i] + j + x[i + 1:])
                if primes[num] and not visited[num]:
                    visited[num] = True
                    q.append((num, count + 1))

def answer(T):
    primes = get_prime()
    for a, b in T:
        print_answer(a, b, primes)


import sys
input = sys.stdin.readline
t = int(input().rstrip())
T = [list(map(int, input().split())) for _ in range(t)]
answer(T)