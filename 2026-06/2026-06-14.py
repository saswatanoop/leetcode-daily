# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/?envType=daily-question&envId=2026-06-14
from collections import defaultdict
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]):
        max_sum=float("-inf")
        # n is not known, go to the last to know the last index, 2 traversals needed
        value=defaultdict(int)
        idx=0
        while head:
            value[idx]=head.val
            head=head.next
            idx+=1
        # idx is at n now,
        for i in range(idx//2):
            max_sum=max(max_sum,value[i]+value[idx-i-1])
        return max_sum
