# https://www.acmicpc.net/problem/1107

def answer(n, broken):
    result = backtrack('', str(n), broken, 500000 - 100)
    return result

def backtrack(ch, n, broken, result):
    if len(ch) == 7:
        return result
    if ch:
        result = min(len(str(int(ch))) + abs(int(ch) - int(n)), result, abs(100 - int(n)))
    result = min(result, abs(100 - int(n)))

    for i in range(10):
        if i not in broken:
            k = backtrack(ch + str(i), n, broken, result)
            result = min(result, k)
    return result



import sys
input = sys.stdin.readline
n = int(input())
broken = set()
k = int(input())
if k:
    broken.update(set(map(int, input().split())))
print(answer(n, broken))