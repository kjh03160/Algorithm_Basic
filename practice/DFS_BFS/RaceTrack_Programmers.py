# https://programmers.co.kr/learn/courses/30/lessons/67259

from collections import deque
def solution(board):
    answer = float('inf')
    visited = [[float('inf') for _ in range(len(board[0]))] for _ in range(len(board))]
    visited[0][0] = 0

    q = deque()
    q.append((0, 0, 0, 0))
    q.append((1, 0, 0, 0))

    direction = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}

    while q:
        go, cost, row, col = q.popleft()
        if row == len(board) - 1 and col == len(board[0]) - 1:
            answer = min(answer, cost)
            continue

        for k, value in list(direction.items()):
            r, c = value
            drow, dcol = row + r, c + col
            if 0 <= drow < len(board) and 0 <= dcol < len(board[0]) and board[drow][dcol] != 1:
                if k % 2 == go % 2 and visited[drow][dcol] >= cost + 100:
                    visited[drow][dcol] = cost + 100
                    q.append((k % 2, cost + 100, drow, dcol))
                elif k % 2 != go % 2 and visited[drow][dcol] >= cost + 600:
                    visited[drow][dcol] = cost + 600
                    q.append((k % 2, cost + 600, drow, dcol))

    return answer


b = [[0,0,0],[0,0,0],[0,0,0]]
print(solution(b))
