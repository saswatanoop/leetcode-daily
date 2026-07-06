# https://leetcode.com/problems/remove-covered-intervals/?envType=daily-question&envId=2026-07-06
from typing import List
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals=sorted(intervals,key=lambda x: (x[0],-x[1]))
        required=1
        last=sorted_intervals[0]

        for i in range(1,len(intervals)):
            cur=sorted_intervals[i]
            if last[0]<=cur[0] and cur[1]<=last[1]:
                continue
            else:
                last=cur
                required+=1
        return required