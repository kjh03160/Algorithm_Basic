def solution(n, k, cmd):
    answer = ''
    """
    U int -> int 칸 위에 잇는 것 선택
    D int -> int 칸 아래 있는 것
    C -> 현재 행 삭제 후 아래 선택 -> 마지막인 경우 위 선택
    Z -> 가장 최근 삭제된 행 복구 -> 현재 선택된 행 바뀌지 않음
    """
    now = k
    table = [True for _ in range(n)]
    lase_deleted = []

    for c in cmd:
        c = c.split()
        if c[0] == "D":
            for i in range(int(c[1])):
                if now < n:
                    now += 1
                    while table[now] is False:
                        now += 1
        elif c[0] == "U":
            for i in range(int(c[1])):
                if now > 0:
                    now -= 1
                    while table[now] is False:
                        now -= 1
        elif c[0] == "C":
            table[now] = False
            lase_deleted.append(now)
            prev = now
            for x in range(now + 1, n):
                if table[x]:
                    now = x
                    break
            if now == prev:
                for x in range(now - 1, -1, -1):
                    if table[x]:
                        now = x
                        break
        else:
            table[lase_deleted.pop()] = True
    for i in table:
        if i:
            answer += 'O'
        else:
            answer += 'X'
    return answer









n = 10
k = 1
# cmd =["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C","C","C","C","C","C","U 1"]
cmd = ["C","C"]
print(solution(n, k, cmd))
