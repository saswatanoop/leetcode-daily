# https://leetcode.com/problems/left-and-right-sum-differences/description/?envType=daily-question&envId=2026-06-06


from typing import List
class Solution:
    # T:O(n) S:O(n)
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left_sum=[0]*n
        right_sum=[0]*n
        for i in range(1,n):
            left_sum[i]=left_sum[i-1]+nums[i-1]
            right_sum[n-i-1]=right_sum[n-i]+nums[n-i]
        for i in range(n):
            nums[i]=abs(left_sum[i]-right_sum[i])
        
        return nums