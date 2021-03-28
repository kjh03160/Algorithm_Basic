def get_bin(n):
    count = 0
    while n:
        if n % 2:
            count += 1
        n = n // 2
    return count

def solution(n):
    origin_ones = get_bin(n)
    answer = 0
    while True:
        n += 1
        new_ones = get_bin(n)
        if origin_ones == new_ones:
            answer = n
            break
    return answer