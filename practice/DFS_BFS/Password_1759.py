# boj.k/1759
def answer(L):
    L.sort()
    result = []
    vowel = {"a", "e", "i", "o", "u"}
    used = [False for _ in range(len(L))]
    v, c = 0, 0
    for i in range(len(L)):
        if L[i] in vowel:
            backtrack(L, i, [], result, vowel, used, v + 1, c)
        else:
            backtrack(L, i, [], result, vowel, used, v, c + 1)
    result.sort()
    return result

def backtrack(L, index, current, result, vowel, used, v, c):
    global n
    current.append(L[index])
    used[index] = True

    if len(current) == n and v >= 1 and c >= 2:
        result.append(''.join(current))
        current.pop()
        used[index] = False
        return

    for i in range(index + 1, len(L)):
        if not used[i]:
            if L[i] in vowel:
                backtrack(L, i, current, result, vowel, used, v + 1, c)
            else:
                backtrack(L, i, current, result, vowel, used, v, c + 1)
    used[index] = False
    current.pop()


import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
n, m = map(int, input().split())
L = input().split()
print(*answer(L), sep='\n')