# boj.kr/11062

# 왼쪽 끝이 x, 오른쪽 끝이 y일때 내가 얻을 수 있는 최대
def func(my_turn, x, y, DP):
    global K

    # 카드 1장이 남았는데, 만약 그때가 내 차례면 더해줌
    if x >= y:
        return K[x] if my_turn else 0

    # 값이 갱신 되었을 떄
    if DP[my_turn][x][y] != -1:
        return DP[my_turn][x][y]
    DP[my_turn][x][y] = 0
    if my_turn:
        # 내가 왼쪽 뽑았을때 vs 오른쪽 뽑았을때의 최대
        DP[my_turn][x][y] = max(func(my_turn - 1, x + 1, y, DP) + K[x], func(my_turn - 1, x, y - 1, DP) + K[y])
    else:
        # 상대가 왼쪽 뽑았을 때 vs 오른쪽 뽑았을 때 값의 최소
        DP[my_turn][x][y] = min(func(my_turn + 1, x + 1, y, DP), func(my_turn + 1, x, y - 1, DP))
    return DP[my_turn][x][y]


def answer(K):
    DP = [[[-1 for _ in range(len(K) + 1)] for _ in range(len(K) + 1)] for _ in range(2)]
    return func(1, 0, len(K) - 1, DP)


import sys
sys.setrecursionlimit(20001)
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    K = list(map(int, input().split()))
    print(answer(K))