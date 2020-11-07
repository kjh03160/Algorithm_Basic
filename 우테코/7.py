def solution(n, horizontal):
    answer = [[0 for _ in range(n)] for _ in range(n)]

    # 인덱스 벗어나는지 확인을 위한 변수
    margin = n - 1
    row = 0
    col = 0

    time = 0  # 시간

    # n이 1이라면 움직일 필요 없음
    if n != 1:
        # 오른쪽으로 움직이기 > 열 + 1
        # 왼쪽 아래 대각선으로 가기 위해 False로 바뀜
        if horizontal:
            col += 1
            horizontal = False
        # 아래로 움직이기 > 행 + 1
        # 오른쪽 위 대각선으로 가기 위해 True로 바뀜
        else:
            row += 1
            horizontal = True

        # 1초 더하기
        time += 1

    # 해당 행렬에 입력
    answer[row][col] = time

    # 왼쪽 아래, 오른쪽 위 대각선으로 가기위한 방향 벡터
    direction = [(1, -1), (-1, 1)]

    # 오른쪽 아래 끝에 도달할때까지
    while row != margin or col != margin:

        if horizontal:  # 오른쪽 대각선 위로 가야함
            d_row, d_col = row + direction[1][0], col + direction[1][1]
            time += 2

        else:  # 왼쪽 대각 아래
            d_row, d_col = row + direction[0][0], col + direction[0][1]
            time += 2

        if d_row > margin or d_col < 0:  # 대각선 아래로 내려오면서 이탈
            if d_row > margin:  # 오른쪽으로 이동해야댐
                d_row = row
                d_col = col + 1
            else:  # 아래로 이동
                d_row = row + 1
                d_col = col
            # 대각선 움직임이 아니기에 기존 time 2 더한것을 1 빼줌
            time -= 1
            horizontal = not horizontal  # 다음은 오른쪽 위로 가기 위해 바꿔줌

        elif d_row < 0 or d_col > margin:  # 대각선 위로 올라가면서 이탈
            # 아래 이동
            if d_row < 0 and d_col > margin:
                d_row = row + 1
                d_col = col
            # 오른쪽 이동
            elif d_row < 0 or d_col < margin:
                d_row = row
                d_col = col + 1
            # 아래 이동
            else:
                d_row = row + 1
                d_col = col
            time -= 1
            horizontal = not horizontal

        # 행렬 확정
        row, col = d_row, d_col
        # 초 입력
        answer[row][col] = time

    return answer