# https://www.acmicpc.net/problem/1436

def answer(n):
    i = 666
    l = []
    while True:
        if '666' in str(i):
            l.append(i)
        i += 1
        if len(l) >= n:
            break
    return l[n - 1]


n = int(input())
print(answer(n))