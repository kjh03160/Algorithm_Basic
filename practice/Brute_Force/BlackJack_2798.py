# https://www.acmicpc.net/problem/2798

def answer(n, m, card):
    std = 300000
    answer = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                val = card[i] + card[j] + card[k]
                if std > abs(val - m) and val <= m:
                    answer = val
                    std = abs(val - m)
    return answer


n, m = map(int, input().split())
card = list(map(int, input().split()))

print(answer(n, m, card))