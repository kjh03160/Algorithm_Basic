# https://programmers.co.kr/learn/courses/30/lessons/72412

from itertools import combinations
from collections import defaultdict
import bisect
def solution(info, query):
    answer = []
    table = defaultdict(list)
    chg = []
    for k in range(5):
        chg.extend(combinations([0, 1, 2, 3], k))

    for _ in info:
        person = _.split()
        score = int(person[-1])
        person = person[:-1]

        for k in chg:
            tmp = person[:]
            for idx in k:
                tmp[idx] = "-"
            table["".join(tmp)].append(int(score))

    for key in table:
        table[key].sort()

    for q in query:
        key = q.split(" and ")
        last, score = key[-1].split()
        key = "".join(key[:-1]) + last
        score = int(score)
        count = len(table[key]) - bisect.bisect_left(table[key], score)
        answer.append(count)
    return answer
