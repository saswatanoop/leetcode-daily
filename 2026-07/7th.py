# https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/?envType=daily-question&envId=2026-07-07
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        num_str=str(n)
        final=[]
        mul=0
        for digit in num_str:
            if digit!='0':
                final.append(digit)
                mul+=int(digit)
        num=''.join(final)
        return int(num if num else 0)*mul
