# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/?envType=daily-question&envId=2026-05-23

from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)

        # 2 sorted subarrays, 2nd submarrays max should be smaller than 1st ones smallest, n-1 and 0th comparision will take care of it
        for i in range(n):

            if nums[i] > nums[(i + 1) % n]:
                count += 1

            if count > 1:
                return False

        return True
