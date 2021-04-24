# https://programmers.co.kr/learn/courses/30/lessons/42895
def solution(N, number):
    answer = -1
    if N == number:
        return 1

    s = [set() for _ in range(9)]

    for i, x in enumerate(s):
        if i == 0:
            continue
        s[i].add(int(str(N) * i))

    for now in range(1, len(s)):
        # 현재 사용해야되는 횟수 = sub + (now - sub)
        # sub 꺼와 now - sub꺼를 사칙연산한 것
        # 예를 들어, 3번이라고 하면,
        # sub = 2, now = 1
        # 2번 쓴 것과 1번 쓴것 을 사칙 연산 -> 3번 쓴 것이 된다.
        for sub in range(now):
            for first in s[sub]:
                for second in s[now - sub]:
                    s[now].add(first + second)
                    s[now].add(first - second)
                    s[now].add(first * second)
                    if second != 0:
                        s[now].add(first // second)
        if number in s[now]:
            answer = now
            break
    return answer