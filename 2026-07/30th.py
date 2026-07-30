# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/

from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        
        freq=Counter(word)
        arr=[v for v in freq.values()]
        arr.sort(reverse=True)

        count=0
        for i,v in enumerate(arr):
            count+=(i//8+1)*v

        
        return count
    
# Solved:
# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/description/
