# https://www.acmicpc.net/problem/1018

def answer(chess):
    ans = []
    max_row = len(chess) - 8
    max_col = len(chess[0]) - 8
    for division_row in range(max_row + 1):
        for division_col in range(max_col + 1):
            std = chess[division_row][division_col]
            temp = 0
            temp2 =0
            for row in range(division_row, division_row + 8):
                for col in range(division_col, division_col + 8):
                    if (row + col) % 2 == 0:
                        if chess[row][col] != std:
                            temp += 1
                        else:
                            temp2 += 1
                    else:
                        if chess[row][col] == std:
                            temp += 1
                        else:
                            temp2 += 1
            ans.append(temp)
            ans.append(temp2)
    return min(ans)


n, m = map(int, input().split())
chess = []
for _ in range(n):
    chess.append(input())

print(answer(chess))
