# https://programmers.co.kr/learn/courses/30/lessons/64064

from itertools import permutations
def solution(user_ids, banned_ids):
    answer = []
    cands = list(permutations(user_ids, len(banned_ids)))

    for c in cands:
        is_true = True
        for i in range(len(banned_ids)):
            if not is_match(banned_ids[i], c[i]):
                is_true = False
                break
        if is_true:
            c = set(c)
            if c not in answer:
                answer.append(c)
    return len(answer)

def is_match(ban_id, user_id):
    if len(ban_id) != len(user_id):
        return False

    for i in range(len(ban_id)):
        if ban_id[i] == '*':
            continue
        elif ban_id[i] != user_id[i]:
            return False
    return True



user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
b = ["*rodo", "*rodo", "******"]
print(solution(user_id, b))

