from collections import defaultdict

problems = defaultdict(dict)
min_ = float('inf')

def solution(n, data, limit):
    global problems
    answer = []
    limit_time, limit_space = map(int, limit.split())
    if not limit_time:
        limit_time = float('inf')
    if not limit_space:
        limit_space = float('inf')

    for i in data:
        algo, p, time, spc = i.split()
        problems[int(p)][algo] = [int(time), int(spc)]

    backtrack(n, 1, [], 0, 0, limit_time, limit_space, answer)
    answer.sort()
    return answer[0] if answer else answer

def backtrack(n, p, now, total_time, total_space, limit_t, limit_spc, answer):
    global min_, problems

    if total_time > limit_t or total_space > limit_spc:
        return

    if p > n:
        if min_ > total_time + total_space:
            answer.clear()
            answer.append(now[:])
            min_ = total_time + total_space
        elif min_ == total_time + total_space:
            answer.append(now[:])
        else:
            return

    for algo in problems[p]:
        now.append(algo)
        t, s = total_time + problems[p][algo][0], total_space + problems[p][algo][1]
        backtrack(n, p + 1, now[:], t, s, limit_t, limit_spc, answer)
        now.pop()

'["알고리즘 이름(name) 해결 문제 번호(number) 필요한 시간(time) 필요한 공간(space)"]'
n = 3
data = ["a1 1 1 4", "a2 1 4 1", "a3 1 3 3", "b1 2 5 6", "b2 2 1 4", "b3 2 4 2", "c1 3 3 6", "c2 3 6 3"]
limit = "10 10"
assert ['a3', "b2", "c2"] == solution(n, data, limit)