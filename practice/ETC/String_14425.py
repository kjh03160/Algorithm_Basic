# boj.kr/14425

def answer(S, query):
    Trie = make_trie(S)
    count = 0
    for q in query:
        if check(q, Trie):
            count += 1
    return count


def check(q, Trie):
    for i in q:
        if not Trie.get(i):
            return False
        Trie = Trie[i]
    if "*" in Trie:
        return True
    return False

def make_trie(S):
    T = {}
    for i in S:
        now = T
        for char in i:
            if char not in now:
                now[char] = {}
            now = now[char]
        now["*"] = i
    return T




import sys
input = sys.stdin.readline
n, m = map(int, input().split())
S = [input().rstrip() for _ in range(n)]
M = [input().rstrip() for _ in range(m)]
print(answer(S, M))
