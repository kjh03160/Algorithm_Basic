# boj.kr/2143

def answer(A, B, t):

    X = []
    Y = []

    for i in range(len(A)):
        s = A[i]
        X.append(s)
        for j in range(i + 1, len(A)):
            s += A[j]
            X.append(s)

    for i in range(len(B)):
        s = B[i]
        Y.append(s)
        for j in range(i + 1, len(B)):
            s += B[j]
            Y.append(s)
    Y.sort()

    import bisect
    result = 0
    s = {}
    for a in X:
        if s.get(a):
            result += s[a]
            continue
        index = bisect.bisect(Y, t - a)
        count = 0
        while True:
            if index - 1 >= 0 and Y[index - 1] == t - a:
                count += 1
                index -= 1
            else:
                break
        s[a] = count
        result += count
    return result


import sys
input = sys.stdin.readline
t = int(input())
a = int(input())
A = list(map(int, input().split()))
b = int(input())
B = list(map(int, input().split()))
print(answer(A, B, t))