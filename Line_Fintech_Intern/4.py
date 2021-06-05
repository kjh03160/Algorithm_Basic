from collections import deque
def solution(n, queries):
    answer = []

    stacks = [deque() for _ in range(n)]

    for q in queries:
        number, command = q
        if command == -1:
            answer.append(pop(stacks, number - 1))
        elif 1 <= command <= 1000000:
            push(stacks, number - 1, command)
    return answer


def push(stacks, i, x):
    if not stacks[i]:
        for s in stacks:
            s.append(x)
    else:
        stacks[i].append(x)

def pop(stacks, i):
    out = -1

    # 현재 스택에서 값이 중앙 값이 아니면
    if len(stacks[i]) >= 2:
        out = stacks[i].pop()
    # 현재 스택에서 뺄 값이 중앙 값이면
    elif stacks[i]:
        now = i
        # 중앙 값을 빼줌
        out = stacks[now].pop()
        # 다음 시계방향 스택으로 이동
        now = (now + 1) % len(stacks)

        # 채울 값을 담을 변수
        is_in = 0
        while now != i:
            # 다른 스택에서 중앙이 채워지지 않았다면
            if not is_in:
                # 지금 스택에서 남은 값이 있다면
                if stacks[now]:
                    # 최초 스택에서 빠진 값을 빼주고
                    stacks[now].popleft()
                    # 위에 남은 값이 있다면
                    if stacks[now]:
                        # 그 값을 다른 곳에 채워주기 위해 값 저장
                        is_in = stacks[now][0]
                        # 현재 스택을 다시 출발점으로 해서 이전 스택까지 순회해서 넣을 수 있도로 갱신
                        i = now
            # 다른 스택에서 채워짐
            else:
                # 현재 스택에서 최초 스택에서 뺀 값을 빼줘야할때
                if stacks[now]:
                    stacks[now].popleft()
                # 다른 스택에서 채워진 값을 넣어줌
                stacks[now].appendleft(is_in)
            # 다음 스택으로 이동
            now = (now + 1) % len(stacks)

    return out

n = 4
quries = [[1, 3], [1, 2], [3, 6], [3, -1], [4, 5], [2, -1], [3, -1], [1, -1]]
assert [6, 3, 5, 2] == solution(n, quries)

n = 5
quries = [[1, -1], [2, -1], [3, -1], [4, -1], [5, -1]]
assert [-1, -1, -1, -1, -1] == solution(n, quries)
