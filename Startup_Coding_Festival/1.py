# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input())
S = [input() for _ in range(n)]
x = [0 for _ in range(24 * 60)]
for i in S:
    start, end = i.split(" ~ ")
    s_hour, s_minute = map(int, start.split(":"))
    e_hour, e_minute = map(int, end.split(":"))
    s = s_hour * 60 + s_minute
    e = e_hour * 60 + e_minute
    for i in range(s, e + 1):
        x[i] += 1

start, end = 0, 0

while start < len(x) and end < len(x):
    if x[start] != n:
        start += 1
        end += 1
        continue
    if x[end] != n:
        break
    end += 1
end -= 1
start_hour = "%02d" % (start // 60)
start_m = "%02d" % (start % 60)
end_h = "%02d" % (end // 60)
end_m = "%02d" % (end % 60)

if start == len(x):
    print(-1)
else:
    print(start_hour + ":" + start_m, end_h + ":" + end_m, sep=' ~ ')

