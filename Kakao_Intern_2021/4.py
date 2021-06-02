def solution(n, start, end, roads, traps):
    answer = float('inf')

    G = {i: {} for i in range(1, n + 1)}
    rev_G = {i: {} for i in range(1, n + 1)}

    for a, b, c in roads:
        G[a][b] = min(c, G[a].get(b, float('inf')))
        if b in traps:
            rev_G[b][a] = min(c, rev_G[b].get(a, float('inf')))
        # if a in traps:
        #     rev_G[a][b] = min(c, rev_G[a].get(b, float('inf')))

    trap_is_r = [False for _ in range(n + 1)]

    from collections import deque
    q = deque()
    q.append((start, 0))

    vist = [False for _ in range(n + 1)]
    rev_vist = [False for _ in range(n + 1)]

    while q:
        print(q)
        now, cost = q.popleft()

        if now == end:
            answer = min(answer, cost)
            continue
        if now in traps:
            trap_is_r[now] = not trap_is_r[now]
            # print(now, trap_is_r[now], rev_G)
            if trap_is_r[now]:
                for node in rev_G[now]:
                    trap_is_r[node] = not trap_is_r[node]
                    q.append((node, cost + rev_G[now][node]))
            else:
                for node in G[now]:
                    q.append((node, cost + G[now][node]))
        else:
            for node in G[now]:
                if trap_is_r[now]:
                    if node in rev_G[now]:
                        q.append((node, cost + rev_G[now][node]))
                else:
                    q.append((node, cost + G[now][node]))

    return answer

n = 4
start = 1
end = 4
roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
traps = [2, 3]

print(solution(n, start, end, roads, traps))