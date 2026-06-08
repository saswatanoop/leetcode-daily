# https://leetcode.com/problems/partition-array-according-to-given-pivot/description/?envType=daily-question&envId=2026-06-08

from typing import List

class Solution:
    # Time: O(n) to iterate through nums once, O(n) to concatenate the three lists
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        before=[]
        pivots=[]
        after=[]

        for n in nums:
            if n<pivot:
                before.append(n)
            elif n==pivot:
                pivots.append(n)
            else:
                after.append(n)
        
        return before+pivots+after