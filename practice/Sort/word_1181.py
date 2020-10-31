# https://www.acmicpc.net/problem/1181

def answer(words):
    words.sort(key=lambda x: (len(x), x))
    pass

import sys
input = sys.stdin.readline

n = int(input())
words = set()

for _ in range(n):
    words.add(input().strip())
words = list(words)
answer(words)
print(*words, sep='\n')

