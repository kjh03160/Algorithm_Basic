# https://programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations


def solution(orders, course):
    answer = []
    menus = dict()
    for i in course:
        for order in orders:
            for menu in list(combinations(list(order), i)):
                menu = sorted(menu)
                menu = "".join(menu)

                if menu not in menus:
                    menus[menu] = 1
                else:
                    menus[menu] += 1

    menus = sorted(menus.items(), key=lambda x: (len(x[0]), -x[1]))
    now = 0
    k = 2
    for menu, count in menus:
        if len(menu) != now:
            if count >= 2:
                answer.append(menu)
                now = len(menu)
                k = count
        else:
            if k == count:
                answer.append(menu)

    answer = sorted(answer)
    return answer