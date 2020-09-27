# 회의실 배정 1931
# https://www.acmicpc.net/problem/1931

def Greedy(T):
    global ans
    L = [0]
    k = 0
    i = 1
    while i < len(T):
        if T[i][0] >= T[k][1] and k != i:
            L.append(i)
            k = i
            ans += 1
        else:
            i += 1
    return L

n = int(input())

times = []

for i in range(n):
    start, end = map(int, input().split())
    times.append((start, end))

times.sort(key= lambda times : times[0])
times.sort(key= lambda times : times[1])

print(len(Greedy(times)))
