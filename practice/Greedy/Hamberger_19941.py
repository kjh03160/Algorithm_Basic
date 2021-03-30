# https://www.acmicpc.net/problem/19941

def answer(A: str):
    global k
    people = []
    B = [False for i in range(len(A))]

    for i in range(len(A)):
        if A[i] == "P":
            people.append(i)
            B[i] = True

    count = 0
    for p in people:
        for i in range(p - k, p + k + 1):
            if len(A) > i >= 0 and not B[i]:
                B[i] = True
                count += 1
                break
    return count


import sys
input = sys.stdin.readline
n, k = map(int, input().split())
A = input().rstrip()
print(answer(A))
