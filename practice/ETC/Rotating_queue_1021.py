# https://www.acmicpc.net/problem/1021

def answer(n, index_list):
    q = list(range(1, n + 1))
    count = 0
    for i in range(len(index_list)):
        left = set(q[:(len(q) // 2) + 1])
        val = index_list[i]

        if val in left:
            out = q.pop(0)
            while out != val:
                q.append(out)
                count += 1
                out = q.pop(0)

        else:
            out = q.pop()
            while out != val:
                q.insert(0, out)
                count += 1
                out = q.pop()
            count += 1

    return count

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
index = list(map(int, input().split()))

print(answer(n, index))