# https://leetcode.com/problems/count-the-number-of-special-characters-ii/submissions/2014181951/?envType=daily-question&envId=2026-05-27


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        n=len(word)
        cap_first_present=[-1]*26
        lower_last_present=[-1]*26

        for i in range(n):
            c=word[i]
            idx=ord(c.lower())-ord('a')
            if c.islower():
                lower_last_present[idx]=i
            else:
                if cap_first_present[idx]==-1:
                    cap_first_present[idx]=i
        count=0
        for i in range(26):
            if cap_first_present[i]!=-1 and lower_last_present[i]!=-1 and lower_last_present[i]<cap_first_present[i]:
                count+=1
        return count