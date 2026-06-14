# https://leetcode.com/problems/weighted-word-mapping/?envType=daily-question&envId=2026-06-13

from typing import List
class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans=[]
        for word in words:
            total=0
            for c in word:
                total+=weights[ord(c)-ord('a')]
            total%=26
            c=chr(ord('a')+25-total)
            ans.append(c)
        return "".join(ans)
