# https://www.acmicpc.net/problem/1747

def answer(n):
    primes = get_prime(1003001, n)
    for p in primes:
        if is_pal(p):
            return p


def get_prime(n, k):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 2):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(k, len(is_prime)) if is_prime[i]]


def is_pal(n):
    n = str(n)
    length = len(n)
    for i in range(length // 2):
        if n[i] != n[length - i - 1]:
            return False
    return True


import sys

input = sys.stdin.readline
n = int(input())
print(answer(n))
