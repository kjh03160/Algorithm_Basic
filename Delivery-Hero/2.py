# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


from collections import defaultdict
def solution(S):
    month = "Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec"
    month = {key: i + 1 for i, key in enumerate(month.split(", "))}
    r_month = {value: key for key, value in month.items()}

    S = S.strip().split('\n')
    QUERY_SIZE = 14 * (2 ** 20)
    cand = defaultdict(list)
    for file in S:
        file = file.split()
        owner, perm, date, size, name = file[0], file[1], file[2:5], file[5], file[6]
        size = int(size)
        if perm[-1] != "x" or perm[1] != "w" or size >= QUERY_SIZE:
            continue
        date[1] = month[date[1]]
        date = list(map(int, date))
        cand[name].append((owner, date))

    last = []
    for file in cand:
        cand[file].sort(key=lambda x: (x[1][2], x[1][1], x[1][0]))
        if cand[file][0][0] != "admin":
            continue
        last.append(cand[file][-1][1])
    if not last:
        return "NO FILES"
    last.sort(key=lambda x: (x[2], x[1], x[0]))
    last[0][1] = r_month[last[0][1]]
    return " ".join(map(str, last[0]))

S ="""
admin  -wx 29 Sep 1983        833 source.h
admin  r-x 23 Jun 2003     854016 blockbuster.mpeg
admin  --x 02 Jul 1997        821 delete-this.py
admin  -w- 15 Feb 1971      23552 library.dll
admin  --x 15 May 1979  645922816 logs.zip
jane   -wx 04 Dec 2110      93184 source.h
jane   -w- 08 Feb 1982  681574400 important.java
admin  rwx 26 Dec 1952   14680064 to-do-list.txt
"""
print(solution(S))

