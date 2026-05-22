# https://leetcode.com/problems/search-in-rotated-sorted-array/?envType=daily-question&envId=2026-05-22

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s,e=0,len(nums)-1

        while s<=e:
            mid=s+(e-s)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>=nums[e]:
                if nums[s]<=target<nums[mid]:
                    e=mid-1
                else:
                    s=mid+1
            else:
                if nums[mid]<target<=nums[e]:
                    s=mid+1
                else:
                    e=mid-1
        return -1