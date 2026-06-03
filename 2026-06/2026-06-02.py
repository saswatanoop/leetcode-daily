# https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/description/?envType=daily-question&envId=2026-06-02

from typing import List

# T:O(n+m) S:O(1)
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]):
        
        n,m=len(landStartTime), len(waterStartTime)
        min_water=min_land=float("inf")

        # find min for single use case
        for i in range(n):
            min_land=min(min_land , landStartTime[i] + landDuration[i])
        for i in range(m):
            min_water=min(min_water, waterStartTime[i]+ waterDuration[i])

        min_time=float("inf")

        
        # Try 1) land first then water and 
        for i in range(m):
            min_time=min(min_time, max(min_land,waterStartTime[i])+waterDuration[i])

        # 2) water first then land, pick min of both
        for i in range(n):
            min_time=min(min_time, max(min_water,landStartTime[i])+landDuration[i])

        return min_time
