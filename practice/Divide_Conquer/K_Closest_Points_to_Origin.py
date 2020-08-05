"""
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)
"""
from typing import List
import math
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def distance(point: List):
            return math.sqrt((point[0] ** 2) + (point[1] ** 2))

        def quickselect(arr, k):
            print(k)
            pivot = arr[0]

            L, M, R = [], [], []

            for i in arr:
                p_dist = distance(pivot)
                now = distance(i)
                if now < p_dist:
                    L.append(i)
                elif now > p_dist:
                    R.append(i)
                else:
                    M.append(i)
            print(L, M, R)
            if len(L) >= k:
                return quickselect(L, k)
            elif len(L) + len(M) < k:
                return quickselect(R, k - len(L) - len(M))
            else:
                if len(M) > 1:
                    for i in M:
                        if i not in result:
                            pivot = i
                            break
                return pivot

        result = []
        for i in range(1, K + 1):
            result.append(quickselect(points, i))
            print()
            # print(result)
        return result

print()
print(Solution().kClosest([[1, 3], [-2, 2]], 1))
# print(Solution().kClosest([[1, 3], [-2, 2]], 2))
# print(Solution().kClosest([[3, 3], [5, -1], [-2, 4]], 2))