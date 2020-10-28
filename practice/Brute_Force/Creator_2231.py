# https://www.acmicpc.net/problem/2231
import math

def answer(n):
    for i in range(n):
        digit = 0
        if i != 0:
            digit = int(math.log10(i))
        creator = i
        temp = i
        for k in range(digit, -1, -1):
            creator = creator + (temp // (10 ** k))
            temp = temp % (10 ** k)

        if creator == n:
            return i
    return 0

n = int(input())
print(answer(n))