class Heap:
    def __init__(self, L = []):
        self.A = L
        self.make_heap()

    def __str__(self):
        return str(self.A)

    def __len__(self):
        return len(self.A)

    def heapify_down(self, k, n):
        while 2 * k + 1 < n:    # arr[k]가 리프노드가 아닐때 까지
            left = 2 * k + 1
            right = 2 * k + 2

            m = k

            if self.A[left] > self.A[k]:
                m = left

            if right < n and self.A[right] > self.A[m]:
                m = right

            if m == k:
                break
            self.A[k], self.A[m] = self.A[m], self.A[k]
            k = m

    def heapify_up(self, k):
        while k > 0 and self.A[(k - 1) // 2] < self.A[k]:
            self.A[(k - 1) // 2], self.A[k] = self.A[k], self.A[(k - 1) // 2]
            k = (k - 1) // 2

    def insert(self, val):
        self.A.append(val)
        self.heapify_up(len(self.A) - 1)

    def make_heap(self):
        n = len(self.A)
        for k in range(n // 2 - 1, -1, -1): # 리프노드는 자식 없으므로 할 필요 없음
            self.heapify_down(k, n)  # arr[k] 힙성질 만족하도록

    def heap_sort(self):
        n = len(self.A)
        for k in range(len(self.A) - 1, -1, -1):
            self.A[0], self.A[k] = self.A[k], self.A[0]
            n = n - 1  # A[n-1]은 정렬되었으므로
            self.heapify_down(0, n)

    def delete_max(self):
        self.A[0], self.A[-1] = self.A[-1], self.A[0]
        x = self.A.pop()
        self.heapify_down(0, len(self.A))
        return x
