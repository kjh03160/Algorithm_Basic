# https://www.acmicpc.net/problem/2960

def get_primes(n, k):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    cnt = 0
    for i in range(2, n + 1):
        for j in range(i, n + 1, i):
            if is_prime[j]:
                is_prime[j] = False
                cnt += 1
                if cnt == k:
                    return j



import sys
input = sys.stdin.readline
n, k = map(int, input().split())
print(get_primes(n, k))