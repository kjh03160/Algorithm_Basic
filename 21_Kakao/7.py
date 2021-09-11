# partial Fail

from collections import deque
import copy
def solution(board, aloc, bloc):
    answer = -1
    win = [-1, -1]
    win_a = list()
    win_b = list()
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    q = deque()
    q.append((board, 0, True, aloc[0], aloc[1], bloc[0], bloc[1]))
    while q:
        board, walk, t, a_r, a_c, b_r, b_c = q.popleft()
        # print()
        # print(*board, sep="\n")
        # print("걸음 :", walk, "/ 턴 :", "A" if t else "B",  "/ A", [a_r, a_c], "B",[b_r, b_c])
        # print()

        if not board[a_r][a_c]:
            win[1] = max(win[1], walk)
            win_b.append(walk)
            continue
        if not board[b_r][b_c]:
            win[0] = max(win[0], walk)
            win_a.append(walk)
            continue
        # print(win)

        is_move = False
        if t:
            for r, c in direction:
                if 0 <= a_r + r < len(board) and 0 <= a_c + c < len(board[0]):
                    dr, dc = a_r + r, a_c + c
                    if board[dr][dc] and board[dr][dc] != 3:
                        # prev = board[dr][dc]
                        # board[dr][dc] = 2
                        board[a_r][a_c] = 0
                        is_move = True
                        q.append((copy.deepcopy(board), walk + 1, t ^ 1, dr, dc, b_r, b_c))
                        board[a_r][a_c] = 1
                        # board[dr][dc] = prev

            if not is_move:
                win[1] = max(win[1], walk)
                win_b.append(walk)
                continue
        else:
            is_move = False
            for r, c in direction:
                if 0 <= b_r + r < len(board) and 0 <= b_c + c < len(board[0]):
                    dr, dc = b_r + r, b_c + c
                    if board[dr][dc] and board[dr][dc] != 2:
                        # prev = board[dr][dc]
                        board[b_r][b_c] = 0
                        # board[dr][dc] = 3
                        is_move = True
                        q.append((copy.deepcopy(board), walk + 1, t ^ 1, a_r, a_c, dr, dc))
                        board[b_r][b_c] = 1
                        # board[dr][dc] = prev
            if not is_move:
                win[0] = max(win[0], walk)
                win_a.append(walk)
                continue
    # print(win, win_a, win_b)
    # if win[0] == -1:
    #     answer = win[1]
    # elif win[1] == -1:
    #     answer = win[0]
    # else:
    #     answer = min(win)
    print(win_a, win_b)
    if len(win_a) == 0:
        return min(win_b)
    elif len(win_b) == 0:
        return min(win_a)
    else:
        return min(max(win_a), max(win_b))
    # return min(win_b + win_a)