
# boj.kr/15961
def answer(F, k, c, eat):
    global n

    count = 0
    for i in range(k):
        if not eat[F[i]]:
            count += 1
        eat[F[i]] += 1

    max_count = count
    for i in range(1, n):
        if max_count <= count:
            if not eat[c]:
                max_count = count + 1
            else:
                max_count = count

        out = i - 1
        eat[F[out]] -= 1
        if not eat[F[out]]:
            count -= 1
        in_ = (i + k - 1) % n
        if not eat[F[in_]]:
            count += 1
        eat[F[in_]] += 1

    return max_count


import sys
input = sys.stdin.readline
n, d, k, c = map(int, input().split())
F = [int(input().rstrip()) for _ in range(n)]
eat = [0 for _ in range(3000001)]
print(answer(F, k, c, eat))


from collections import deque
def answer(F, k, c, eat):
    global n

    start = 0
    end = start + k - 1
    food = deque()
    max_count = 0
    for i in range(start, end + 1):
        food.append(F[i])
        if not eat[F[i]]:
            max_count += 1
        eat[F[i]] += 1
    now = max_count

    if not eat[c]:
        max_count += 1

    start = (start + 1) % n
    end = (end + 1) % n

    while True:
        out = food.popleft()
        eat[out] -= 1

        if not eat[out]:
            now -= 1

        food.append(F[end])
        if not eat[F[end]]:
            now += 1
        eat[F[end]] += 1

        if not eat[c]:
            max_count = max(max_count, now + 1)
        else:
            max_count = max(max_count, now)

        if start == 0:
            break

        start = (start + 1) % n
        end = (end + 1) % n

    return max_count


import sys
input = sys.stdin.readline
n, d, k, c = map(int, input().split())
F = [int(input().rstrip()) for _ in range(n)]
eat = [0 for _ in range(3000001)]
print(answer(F, k, c, eat))