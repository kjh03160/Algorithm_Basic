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

        def swap_elements(my_list, index1, index2):
            my_list[index1], my_list[index2] = my_list[index2], my_list[index1]

        def partition(my_list, start, end):
            pivot = distance(my_list[end])
            i = start
            b = start
            while i < end:
                if distance(my_list[i]) < pivot:
                    swap_elements(my_list, b, i)
                    b += 1
                i += 1

            swap_elements(my_list, b, i)
            return b

        def quicksrot(my_list, start, end):
            if start >= end:
                return
            q = partition(my_list, start, end)
            quicksrot(my_list, start, q - 1)
            quicksrot(my_list, q + 1, end)

        quicksrot(points, 0, len(points) - 1)
        return points[:K]
