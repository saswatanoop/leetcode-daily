# https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/?envType=daily-question&envId=2026-05-29

from typing import List

class Solution:
    def minElement(self, nums: List[int]):
        
        def digit_sum(n):
            total=0
            while n:
                total+=n%10
                n=n//10
            return total

        res=float("inf")
        for n in nums:
            res=min(res,digit_sum(n))
            
        return res