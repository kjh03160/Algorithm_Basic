def solution(places):
    answer = []
    for p in places:
        if check(p):
            answer.append(1)
        else:
            answer.append(0)
    return answer


from collections import deque
def check(G):
    P = []
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j] == "P":
                P.append((i, j))

    for r, c in P:
        q = deque()

        visited = [[False for _ in range(len(G))] for _ in range(len(G))]
        q.append((r, c, 0))
        visited[r][c] = True

        while q:
            row, col, dist = q.popleft()
            if dist > 2:
                continue
            if G[row][col] == "P" and 0 < dist <= 2:
                return False

            for r, c in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
                drow, dcol = row + r, c + col
                if 0 <= drow < len(G) and 0 <= dcol < len(G):
                    if not G[drow][dcol] == "X" and not visited[drow][dcol]:
                        visited[drow][dcol] = True
                        q.append((drow, dcol, dist + 1))
    return True


places = [["PXPOO",
           "XPOOP",
           "OXXOX",
           "OXXOX",
           "OXXOX"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))
