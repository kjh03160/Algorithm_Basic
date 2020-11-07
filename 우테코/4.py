def solution(n, board):
    answer = 0

    # 다음 요소 찾기
    def find_next(board, x):
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == x:
                    return row, col

    row = 0
    col = 0
    x = 1  # 1부터 찾기

    while x != n * n + 1:
        d_row, d_col = find_next(board, x)
        click = 0
        # 인덱스 벗어나서 갈수 있는 거리
        # 2번 눌러야 갈 수 있는 거리 -> 대각선 끝이나 바로 다음 행 번째
        if (abs(d_row - row) == n - 1 and abs(d_col - col) == n - 1) \
                or (abs(d_row - row) + abs(d_col - d_col)) == n:
            print(row, col)
            click += 2
            row = d_row
            col = d_col
        # 1번 눌러서 갈 수 있는 거리 -> 행이나 열이 같은 곳
        elif abs(d_row - row) == n - 1:
            click += 1
            row = d_row
        elif abs(d_col - col) == n - 1:
            click += 1
            col = d_col
        # 그 이외는 인덱스 거리 만큼 클릭
        # 그리고 엔터
        click += abs(d_row - row) + abs(d_col - col) + 1
        # 현재 위치 갱신
        row = d_row
        col = d_col
        answer += click
        # 다음 요소 찾기
        x += 1

    return answer