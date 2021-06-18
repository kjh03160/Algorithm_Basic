# boj.kr/20440

import heapq
def answer(K):
    K.sort()
    q = []
    ans_size = 0
    ans_range = [0, 0]
    for i in range(len(K)):
        # 시작시간이 top() 원소의 끝나는 시간보다 작아질때까지
        # 즉, 이전 시간에 있던 모기들을 빼는 것
        while q and q[0][0] <= K[i][0]:
            heapq.heappop(q)

        # 끝나는 시간이 적은게 우선 오도록 힙 구성
        heapq.heappush(q, (K[i][1], K[i][0]))

        # 만약 현재 답의 마리 수가 같고, 해당 끝 시간이 현재 시작 시간이라면
        # 즉 전의 답과 딱 이어지는 부분, ex) 4 6, 6 10
        if ans_size == len(q) and ans_range[1] == K[i][0]:
            # 끝 시간을 큐에 들어있는 가장 일찍 끝나는 시간으로
            ans_range[1] = q[0][0]
        elif len(q) > ans_size:
            ans_range = [K[i][0], q[0][0]]
            ans_size = len(q)

    print(ans_size)
    print(*ans_range)


import sys
input = sys.stdin.readline
n = int(input())
K = [list(map(int, input().split())) for _ in range(n)]
answer(K)