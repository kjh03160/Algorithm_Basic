# https://programmers.co.kr/learn/courses/30/lessons/72410?language=python3

def solution(new_id):
    new_id = new_id.lower()
    REMOVE = '~!@#$%^&*()=+[{]}:?,<>/'
    answer = ''
    is_ = False
    for i in new_id:
        if i == "." and is_:
            continue
        if i not in REMOVE:
            answer += i
            is_ = False
        if i == ".":
            is_ = True
    while len(answer) and (answer[-1] == "." or answer[0] == '.'):
        answer = answer.strip('.')
    # print(answer)

    if not len(answer):
        answer += 'a'

    if len(answer) >= 16:
        answer = answer[:15]
        while answer[-1] == "." or answer[0] == '.':
            answer = answer.strip('.')

    while len(answer) <= 2:
        answer += answer[-1]

    return answer