# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import defaultdict
def solution(S, C):
    answer = []
    S = S.split(", ")
    dup = defaultdict(int)
    for i in S:
        string = ''
        first, middle, last = None, None, None
        i = i.split()
        if len(i) > 2:
            first, middle, last = i
        else:
            first, last = i
        first = first[0]
        last = last.replace("-", "")
        if len(last) > 8:
            last = last[:8]
        if middle:
            string = "".join([first, middle, last])
        else:
            string = "".join([first, last])
        if string in dup:
            dup[string] += 1
            string += str(dup[string])
        else:
            dup[string] = 1
        string += "@" + C
        answer.append("%s <%s>" % (" ".join(i), string.lower()))
    return ", ".join(answer)

S = "John Doe, Peter Parker, Mary Jane Watson-Parker, James Doe, John Elvis Doe, Jane Doe, Penny Parker"
C = "exmaple"
print(solution(S, C))