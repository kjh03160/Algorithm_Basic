def max_sum(L, left, right):
    if left >= right:
        return L[left]
    m = (left + right) // 2

    left_val = max_sum(L, left, m)  # 좌측 최대 구간
    right_val = max_sum(L, m + 1, right)    # 우측 최대구간

    # m을 포함한 최대 구간
    temp = 0
    left_part = -99999999
    for i in range(m, -1, -1):
        temp += L[i]
        left_part = max(left_part, temp)

    temp = 0
    right_part = -999999
    for i in range(m + 1, right):
        temp += L[i]
        right_part = max(right_part, temp)

    mid = left_part + right_part
    return max(left_val, mid, right_val)


a = [1, -1, 3, -4, 5, -4, 6, -2]
print(max_sum(a, 0, len(a) - 1))