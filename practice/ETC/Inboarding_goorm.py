
# 입국 심사대 평균 대기시간 구하기

import heapq
def answer(k, wait_time, P):
    # 심사대에 도착하는 시간을 구해주기.
    for i in range(1, len(wait_time)):
        wait_time[i] += wait_time[i - 1]

    q = []
    # 큐에는 심사가 끝나는 시간을 넣어줄 것임
    # 즉 심사대에 들어갈 수 있는 시간이 될 것임
    now = 0
    result = 0
    # 심사대 개수만큼 처음에 오는 사람들 바로 넣어줌.
    while now < k and now < len(wait_time):
        # 도착한 시간 + 심사 걸리는 시간
        heapq.heappush(q, wait_time[now] + P[now])
        now += 1

    # 모든 사람이 심사대에 들어갈 때까지
    while now < len(P):
        time = heapq.heappop(q)     # 심사대가 빈 시간

        # 만약 심사대가 비어있는 시간과 이제 들어갈 사람이 도착한 시간이 0보다 크다 -> 기다린 시간이 있다.
        if time - wait_time[now] > 0:
            # 기다린 시간을 더해줌
            result += time - wait_time[now]
        else:
            # 기다린 시간이 없다 => 심사대가 빈 시간이 더 빨랐다.
            # 그러므로 다음 사람이 도착한 시간으로 바꿔줘야됨.
            # 1번 예시에서 5번째 들어간 사람이 들어갈 때를 생각해보면 됨
            time = wait_time[now]

        # 현재 들어간 사람이 심사가 끝나고 비워질 시간을 넣음
        heapq.heappush(q, time + P[now])
        # 다음 사람 차례로 넘김
        now += 1

    return "%.1f" % (result / len(P))


import sys
input = sys.stdin.readline
k = int(input().rstrip())
n = int(input().rstrip())
wait_time = []
P = []
for _ in range(n):
    time, p = map(int,  input().split())
    wait_time.append(time)
    P.append(p)
print(answer(k, wait_time, P))
