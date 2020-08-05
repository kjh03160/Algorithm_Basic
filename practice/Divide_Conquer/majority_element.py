"""
169. Majority Element
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def func(left_inx, right_inx):
            if left_inx == right_inx:
                return nums[left_inx]

            mid = (right_inx - left_inx) // 2 + left_inx
            left = func(left_inx, mid)
            right = func(mid + 1, right_inx)

            if left == right:
                return left

            left_count = sum(1 for i in range(left_inx, right_inx + 1) if nums[i] == left)
            right_count = sum(1 for i in range(left_inx, right_inx + 1) if nums[i] == right)

            return left if left_count > right_count else right

        return func(0, len(nums) - 1)
import math
print(math.sqrt(-2147483648))