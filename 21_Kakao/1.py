# Success

from collections import defaultdict
def solution(id_list, report, k):
    answer = []

    d = defaultdict(set)
    out = defaultdict(int)
    for i in range(len(report)):
        temp = report[i].split()
        user = temp[0]
        report_user = set(temp[1:])

        for r in report_user:
            if r not in d[user]:
                d[user].add(r)
                out[r] += 1

    for i in range(len(id_list)):
        user = id_list[i]
        result = 0
        for r in d[user]:
            if out[r] >= k:
                result += 1
        answer.append(result)
    return answer


print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))