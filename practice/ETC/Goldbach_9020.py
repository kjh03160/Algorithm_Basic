# https://www.acmicpc.net/problem/9020


def answer(n, primes):
    x = n // 2
    y = x
    for _ in range(10000):
        if primes[x] and primes[y]:
            return x, y
        x -= 1
        y += 1

def get_primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime


import sys

input = sys.stdin.readline
n = int(input())
L = []
k = 0
for _ in range(n):
    L.append(int(input()))
    if L[-1] > k:
        k = L[-1]
primes = get_primes(k)
for i in L:
    print(*answer(i, primes))
