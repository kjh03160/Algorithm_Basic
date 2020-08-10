def max_sum(n, L):
    result = [L[0]]
    for i in range(1, n):
        result.append(max(result[i - 1] + L[i], L[i]))
    return max(result)