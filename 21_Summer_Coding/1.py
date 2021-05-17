def solution(code, day, data):
    answer = []

    D = []
    for d in data:
        price, c, date = d.split()
        price = price.split("=")[1]
        c = c.split("=")[1]
        date = date.split("=")[1]
        if c == code and day == date[:-2]:
            D.append((int(date), int(price)))
    D.sort(key=lambda x:x[0])
    for i in D:
        answer.append(i[1])

    return answer