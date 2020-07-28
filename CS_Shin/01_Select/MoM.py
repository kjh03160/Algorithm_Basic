def find_median_five(A):
	"""
	4개의 값을 토너먼트 형식으로 비교하여 최댓값을 구한다. 이 값은 중앙값이 될 수 없다. (이 과정에서 3번의 비교가 필요하다.)
	위에서 사용되지 않은 나머지 한 값을 1.에서의 최댓값 자리에 넣고, 4개의 값을 토너먼트 형식으로 비교하여 최댓값을 구한다.
	이 값은 중앙값이 될 수 없다. (이 과정에서 2번의 비교가 필요하다.)
	남은 세 숫자 중 최댓값을 구한다. 이 값이 중앙값이다. (이 과정에서 1번의 비교가 필요하다.)
	총 6번의 비교가 필요하다
	"""
	a1, a2, b1, b2 = 0, 0, 0, 0

	if A[0] > A[1]:
		b1 = A[0]
		a1 = A[1]
	else:
		b1 = A[1]
		a1 = A[0]

	if A[2] > A[3]:
		b2 = A[2]
		a2 = A[3]
	else:
		b2 = A[3]
		a2 = A[2]

	if b1 > b2:
		if A[4] > a1:
			b1 = A[4]
		else:
			b1 = a1
			a1 = A[4]
	else:
		if A[4] > a2:
			b2 = A[4]
		else:
			b2 = a1
			a2 = A[4]

	if b1 > b2:
		if b2 > a1:
			return b2
		return a1

	if b1 > a2:
		return a1
	return a2


def MoM(L, k):
	if len(L) == 1:
		return L[0]
	A, B, M, medians = [], [], [], []

	i = 0
	while i + 4 < len(L):
		medians.append(find_median_five(L[i : i + 5]))
		# 정렬하는 코드 여기 들어가야함

	if i < len(L) <= i + 4:
		# 4개 이하의 리스트에서 중앙값 뽑고 정렬하는 코드
		pass

	mom = MoM(medians, len(medians) // 2)
	for v in L:
		if v < mom:
			A.append(v)
		elif v > mom:
			B.append(v)
		else: M.append(v)

	if len(A) < k:
		return MoM(A, k)
	elif len(A) + len(M) < k:
		return MoM(B, k - len(A) - len(M))
	return mom
