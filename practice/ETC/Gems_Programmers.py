# https://programmers.co.kr/learn/courses/30/lessons/67258

def solution(gems):
    answer = [0, float('inf')]

    start, end = 0, 0
    g = {i: 0 for i in set(gems)}
    count = 1
    g[gems[start]] += 1

    while start <= end and end < len(gems):

        if len(g) == count:
            if answer[1] - answer[0] > end - start:
                answer = [start + 1, end + 1]

            g[gems[start]] -= 1
            if not g[gems[start]]:
                count -= 1

            start += 1

        else:
            end += 1
            if end >= len(gems):
                break

            g[gems[end]] += 1
            if g[gems[end]] == 1:
                count += 1

    return answer


gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
print(solution(gems))