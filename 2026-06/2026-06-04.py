# https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/?envType=daily-question&envId=2026-06-04


class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def count(s:str)->int:
            if len(s)<=2:
                return 0
            total=0
            for i in range(1,len(s)-1):
                if s[i-1]<s[i]>s[i+1] or s[i-1]>s[i]<s[i+1]:
                    total+=1
            return total
        
        waves=0
        for i in range(num1,num2+1):
            waves+=count(str(i))
        return waves
