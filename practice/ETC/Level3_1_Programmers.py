def solution(n, t, m, timetable):
    timetable.sort()
    start = get_time("09:00")

    answer = "09:00"

    last_p = 0
    for round in range(n):
        can_take_p = m
        for p in range(last_p, len(timetable)):
            if get_time(timetable[p]) <= start:
                can_take_p -= 1
                last_p += 1
                if not can_take_p:
                    break

        if round == n - 1:
            if not can_take_p:
                answer = to_str(get_time(timetable[last_p - 1]) - 1)
            else:
                answer = to_str(start)
        start += t
        if start >= get_time("24:00"):
            break
    return answer


def get_time(s):
    h, m = s.split(":")
    return int(h) * 60 + int(m)


def to_str(i):
    h, m = i // 60, i % 60
    return "%02d:%02d" % (h, m)