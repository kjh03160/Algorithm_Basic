# https://www.acmicpc.net/problem/5052

class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, val):
        node = self.root
        flag = False
        for string in val:
            if string not in node:
                node[string] = {}
            if self.end_symbol in node:
                flag = True
            node = node[string]
        node[self.end_symbol] = val
        return flag

def answer(L):
    L.sort()
    trie = Trie()
    f = False
    for word in L:
        f |= trie.add(word)
        if f:
            break
    return "NO" if f else "YES"

import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input().rstrip())
    L = []
    for i in range(n):
        L.append(input().rstrip())
    print(answer(L))
