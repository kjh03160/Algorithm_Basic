# boj.kr/2671

import re
def answer(s):
    pattern = "(100+1+|01)+$"
    regex = re.compile(pattern)
    if regex.match(s):
        return "SUBMARINE"
    else:
        return "NOISE"


import sys
input = sys.stdin.readline
s = input().rstrip()
print(answer(s))