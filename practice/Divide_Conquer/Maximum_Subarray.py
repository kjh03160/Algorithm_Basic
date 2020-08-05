"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
"""
from typing import List

class Solution:
    def maxSubArray1(self, nums):
        return self.helper(nums, 0, len(nums) - 1)

    def helper(self, nums, low, high):
        """
        Divide and Conquer solution, the solution can lie entirely in left or in right or span in between.
        When it spans in between, we can use principle of optimality. The middle sum can be broken into sum from middle-1 towards left, and sum from middle+1 towards an index <= high. Lets call these sums as lmax and rmax.
        Now the maximum middle sum must be max(lmax,0)+max(rmax,0)+nums[mid].
        Why? We have to include nums[mid]. Now the left sum or right sum will only be included if the sum is positive.
        """
        if low > high:
            return 0
        if low == high:
            return nums[low]
        mid = low + (high - low) // 2
        x_left = self.helper(nums, low, mid)
        x_right = self.helper(nums, mid + 1, high)
        lmax, rmax = float('-inf'), float('-inf')
        lsum, rsum = 0, 0
        for i in range(mid - 1, low - 1, -1):  ### Important Insight in NlgN solutions
            lsum = lsum + nums[i]
            lmax = max(lmax, lsum)
        for i in range(mid + 1, high + 1, 1):
            rsum = rsum + nums[i]
            rmax = max(rmax, rsum)
        return max(x_left, x_right, max(0, lmax) + max(0, rmax) + nums[mid])


    def maxSubArray2(self, nums: List[int]) -> int:
        """
        DP 접근법
        """
        current_sum = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            current_sum = max(current_sum + nums[i], nums[i])

            if current_sum < 0:
                current_sum = nums[i]

            if current_sum > max_sum:
                max_sum = current_sum
        return max_sum
