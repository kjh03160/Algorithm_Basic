def solution(absolutes, signs):
    answer = 0

    for i in range(len(signs)):
        num = absolutes[i]
        if not signs[i]:
            num = -num
        answer += num
    return answer