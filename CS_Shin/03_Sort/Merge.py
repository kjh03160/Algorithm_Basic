def merge_sort(A, first, last):
    if first >= last:
        return

    middle = (first+last) // 2
    merge_sort(A, first, middle)
    merge_sort(A, middle + 1, last)

    B = []
    left = first
    right = middle + 1
    while left <= middle and right <= last:
        if A[left] <= A[right]:
            B.append(A[left])
            left += 1
        else:
            B.append(A[right])
            right += 1

    # 남은 요소 집어 넣기
    for i in range(left, middle+1):
        B.append(A[i])
    for j in range(right, last+1):
        B.append(A[j])

    # A에 덮어 쓰기
    for k in range(first, last+1):
        A[k] = B[k-first]

# 입력 숫자에 대한 inversion 개수 구하기
def inversion(A):
    count = 0

    def merge(A, left, right, count):
        if left >= right:
            return 0
        mid = (left + right) // 2
        count += merge(A, left, mid, count)
        count += merge(A, mid + 1, right, count)

        b= []
        i = left
        j = mid + 1
        while i <= mid and j <= right:
            if A[i] > A[j]:
                b.append(A[j])
                count += 1
                j += 1
            else:
                b.append(A[i])
                i += 1

        for k in range(i, mid + 1):
            b.append(A[k])

        for x in range(j, right + 1):
            b.append(A[x])

        for w in range(left, right + 1):
            A[w] = b[w - left]
        return count
    return merge(A, 0, len(A) - 1, count)

a = [2, 4, 1, 3, 5]
print(inversion(a))
