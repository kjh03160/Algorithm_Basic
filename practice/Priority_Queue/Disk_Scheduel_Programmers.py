# https://programmers.co.kr/learn/courses/30/lessons/42627

import heapq
def solution(jobs):
    count, end_time, answer = 0, -1, 0
    wait = []
    jobs.sort()
    # 시작시간 초기화
    start_time = jobs[0][0]
    while count < len(jobs):
        for st, cost in jobs:
            if end_time < st <= start_time:
                # 작업 소요시간으로 min heap을 만들기 위해 (t, s) 푸시
                heapq.heappush(wait, (cost, st))
        # 바로 수행할 수 있는 작업이 있는 경우
        if len(wait) > 0:
            count += 1
            end_time = start_time
            cost, new = heapq.heappop(wait)
            start_time += cost
            answer += (start_time - new)
        # 바로 수행할 수 있는 작업이 없는 경우
        else:
            start_time += 1
    return answer // len(jobs)


print(solution([[0, 3], [1, 9], [2, 6]]))