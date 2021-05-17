from collections import deque
def solution(t, r):
    answer = []
    q = deque()
    kk = t
    t = list(enumerate(t))
    t.sort(key=lambda x: x[1])
    for idx, time in t:
        q.append([time, idx])

    while q:
        time, idx = q.popleft()
        equal = [[time, idx]]
        while q and time == q[0][0]:
            equal.append(q.popleft())
        equal.sort(key=lambda x:  (-r[x[1]], -kk[x[1]], -x[1]))
        print(equal)
        answer.append(equal.pop()[1])
        for i in range(len(equal)):
            equal[i][0] = equal[i][0] + 1
        q.extendleft(equal)

    return answer

t = [0,1,3,0]
r =	[0,1,2,3]

print(solution(t, r))