def frac_knapsack(i, size):
    max_value = 0
    fractions = [0]*len(value)
    for k in range(i, n):
        if value[k] <= size:
            fractions[k] = 1
            max_value += weight[k]
            size -= value[k]
        else:
            fractions[k] = size / value[k]
            max_value += weight[k] * size / value[k]
            break
    return max_value


def knapsack(i, size):
    global n, x, MP
    if i >= n or size <= 0:
        return

    pv = sum(weight[j] for j in range(i) if x[j] == 1)

    if value[i] <= size:
        b = frac_knapsack(i + 1, size - value[i])
        if pv + weight[i] + b > MP:
            MP = max(MP, pv + weight[i])
            x[i] = 1
            knapsack(i + 1, size - value[i])

    x[i] = 0
    b = frac_knapsack(i + 1, size)

    if pv + b > MP:
        x[i] = 0
        knapsack(i + 1, size)


n, k = map(int, input().split())
value = []
weight = []
for i in range(n):
    v, w = map(int, input().split())
    value.append(v)
    weight.append(w)

MP = 0
index = list(range(len(value)))
n = len(value)
x = [0 for i in range(n)]

# contains ratios of values to weight
ratio = [w / v for v, w in zip(value, weight)]
# index is sorted according to value-to-weight ratio in decreasing order
index.sort(key=lambda i: ratio[i], reverse=True)

for i in range(n):
    value.append(value[index[i]])
    weight.append(weight[index[i]])

value, weight = value[n:], weight[n:]
knapsack(0, k)
print(MP)
