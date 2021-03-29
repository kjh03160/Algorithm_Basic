
def solution(routes):
    routes = sorted(routes, key=lambda route: route[1])
    prev = -30000
    answer = 0

    for route in routes:
        if prev < route[0]:
            answer += 1
            prev = route[1]

    return answer