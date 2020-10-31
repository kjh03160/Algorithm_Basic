# https://www.acmicpc.net/problem/11651

def answer(l):
    l.sort(key = lambda x: (x[1], x[0]))

import sys
input = sys.stdin.readline

n = int(input())
points = []
for _ in range(n):
    points.append(list(map(int, input().split())))
answer(points)
for x, y in points:
    print(x, y)


from sys import stdin, stdout
# y 값을 크게 만들고 x를 더함 -> 정렬 후 그대로 빼서 출력
stdout.write(
    '\n'.join(
        f'{v % 1000000 - 100000} {v // 1000000 - 100000}'
        for v
        in sorted(
            (int(line.split()[1])+100000) * 1000000
            + int(line.split()[0])+100000
            for line in stdin.read().splitlines()[1:]
        )
    ) + '\n'
)