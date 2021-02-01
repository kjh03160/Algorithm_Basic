# https://programmers.co.kr/learn/courses/30/lessons/72414#fn1

def time_to_sec(time):
    h, m, s = map(int, time.split(":"))
    return h * 3600 + m * 60 + s


def to_hour(time):
    sec = time % 60
    h = time // (60 * 60)
    time = time % 3600
    mn = time // 60
    return "%02d:%02d:%02d" % (h, mn, sec)


def solution(play_time, adv_time, logs):
    answer = 0
    logs_start_sec = []
    logs_end_sec = []
    total_time = [0 for _ in range(60 * 60 * 100)]
    for i in logs:
        start, end = i.split("-")
        logs_start_sec.append(time_to_sec(start))
        logs_end_sec.append(time_to_sec(end))
        total_time[logs_start_sec[-1]] += 1
        total_time[logs_end_sec[-1]] -= 1

    for i in range(1, time_to_sec(play_time)):
        total_time[i] = total_time[i] + total_time[i - 1]

    for i in range(1, time_to_sec(play_time)):
        total_time[i] = total_time[i] + total_time[i - 1]
    max_time = 0
    for i in range(time_to_sec(adv_time) - 1, time_to_sec(play_time)):
        if i >= time_to_sec(adv_time):
            if max_time < total_time[i] - total_time[i - time_to_sec(adv_time)]:
                max_time = total_time[i] - total_time[i - time_to_sec(adv_time)]
                answer = i + 1 - time_to_sec(adv_time)
        else:
            if max_time < total_time[i]:
                max_time = total_time[i]
                answer = i + 1 - time_to_sec(adv_time)

    return to_hour(answer)


print(solution("99:59:59", "25:00:00",
               ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
