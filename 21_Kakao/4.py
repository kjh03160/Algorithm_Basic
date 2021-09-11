# partial Fail
max_score = -1
def solution(n, info):
    answer = []
    dfs(info, 0, 0, n, answer, [0 for _ in range(len(info))])

    return answer


def dfs(info, index, score, remain, answer, result):
    global max_score
    if index >= len(info) or not remain:
        if max_score >= score:
            max_score = score
            return answer.append(result)
    if index + 1 < len(info) and info[index] + 1 <= remain:
        result[index] = info[index] + 1
        dfs(info, index + 1, score + (10 - index), remain - info[index] - 1, answer, result[:])
        result[index] = 0
        dfs(info, index + 1, score, remain, answer, result[:])




print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))