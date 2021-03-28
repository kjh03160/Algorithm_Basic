
def solution(files):
    answer = []
    temp = []
    idx = 0
    for file in files:
        file = file.lower()
        head_s, head_e = get_head(file)
        num_s, num_e = get_number(file, head_e)

        head = file[head_s:head_e]
        number = file[num_s:num_e]
        tail = file[num_e:]

        temp.append((head, int(number), tail, idx))
        idx += 1
    temp.sort()
    for i in temp:
        answer.append(files[i[-1]])
    return answer


def get_head(string, start=0):
    end = start
    while True:
        if string[end].isdigit():
            break
        else:
            end += 1
    return start, end


def get_number(string, start):
    end = start
    while end < len(string):
        if not string[end].isdigit():
            break
        else:
            end += 1
    return start, end

print(solution(["muzi1"]))