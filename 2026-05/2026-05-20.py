# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/description/?envType=daily-question&envId=2026-05-20
from collections import defaultdict
from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n=len(A)
        freq=defaultdict(int)
        count=0
        ans=[0]*n
        for i in range(n):
            freq[A[i]]+=1
            if freq[A[i]]==2:
                count+=1
            freq[B[i]]+=1
            if freq[B[i]]==2:
                count+=1
            ans[i]=count
        return ans
        