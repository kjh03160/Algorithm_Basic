# https://www.acmicpc.net/problem/17281
def answer(G):
    entry = get_entry()
    max_score = 0
    for i in entry:
        players = list(i[:3]) + [0] + list(i[3:])
        player = 0
        inning = 0
        score = 0

        while inning < len(G):
            inning += 1
            out = 0
            base1, base2, base3 = 0, 0, 0
            while out != 3:
                hit = G[inning - 1][players[player]]
                player = (player + 1) % 9

                if not hit:
                    out += 1
                    continue
                elif hit == 1:
                    score += base3
                    base1, base2, base3 = 1, base1, base2
                elif hit == 2:
                    score += base3 + base2
                    base1, base2, base3 = 0, 1, base1
                elif hit == 3:
                    score += base3 + base2 + base1
                    base1, base2, base3 = 0, 0, 1
                else:
                    score += base3 + base2 + base1 + 1
                    base1, base2, base3 = 0, 0, 0

        max_score = max(score, max_score)
    return max_score


def get_entry():
    result_list = []
    for i in range(1, 9):
        L = []
        L.append(i)
        visited = [False for _ in range(9)]
        visited[i] = True
        back_track(result_list, L, visited)
    return result_list


def back_track(result_list, L, visited):
    if len(L) == 8:
        return result_list.append(L[:])

    for i in range(1, 9):
        if not visited[i]:
            visited[i] = True
            L.append(i)
            back_track(result_list, L, visited)
            L.pop()
            visited[i] = False


# print(get_entry())
import sys
input = sys.stdin.readline
n = int(input())
G = []

for _ in range(n):
    G.append(list(map(int, input().split())))


print(answer(G))