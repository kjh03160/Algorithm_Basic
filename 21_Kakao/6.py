# Correctness Pass
# 효율성 모두 실패
def solution(board, skill):
    process(board, skill)
    answer = check(board)
    return answer


def process(board, skill):
    for i in skill:
        type, r1, c1, r2, c2, degree = i
        if type == 1:
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    board[r][c] -= degree
        else:
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    board[r][c] += degree
def check(board):
    result = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] > 0:
                result += 1
    return result

print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))