# Success

import math
def primes(n):
    N = [True for _ in range(2 * n + 1)]
    N[0] = False
    N[1] = False
    for i in range(2, int(math.sqrt(2 * n)) + 1):
        if N[i]:
            for j in range(i * i, 2 * n + 1, i):
                N[j] = False
    return N

def convert(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]

import re
def find_out(regex, string):
    pattern = re.compile(regex)
    out = pattern.findall(string)
    return out


def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0

    converted = convert(n, k)
    is_prime = primes(n)
    result = list()

    f = find_out(r'([1-9]+0)|([1-9]+)|(0[1-9]+)|(0[1-9]+0)', converted)
    for x in f:
        for i in x:
            if len(i):
                result.append(int(i.strip("0")))
    for number in result:
        if number <= n and is_prime[number]:
            answer += 1
        elif number > n:
            if is_prime_number(number):
                answer += 1
    return answer
