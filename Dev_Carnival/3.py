from itertools import combinations

def answer(n, k):
    result = 0
    tmp = range(n)
    for i in range(n + 1):
        x = list(combinations(tmp, i))
        for j in x:
            if len(j) >= k:
                flag = True
                start, end = 0, k - 1
                while end < len(j):
                    diff = j[end] - j[start]
                    if diff < 7:
                        flag = False
                        break
                    start += 1
                    end += 1
                if flag:
                    result += 1
            else:
                result += 1
    return result

import sys
input = sys.stdin.readline
n, k = map(int, input().split())
print(answer(n, k))