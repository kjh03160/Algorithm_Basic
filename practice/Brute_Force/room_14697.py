# 14697

x = input().split()
n = int(x[-1])
k = list(map(int, x[:3]))

def answer(n, k):
    for i in range((n // k[0]) + 2):
        for j in range((n // k[1]) + 2):
            for w in range((n // k[2]) + 2):
                if k[0] * i + k[1] * j + k[2] * w == n:
                    return 1
    return 0

print(answer(n, k))