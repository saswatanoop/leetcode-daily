# https://leetcode.com/problems/maximum-product-of-two-digits/?envType=daily-question&envId=2026-07-25

class Solution:
    def maxProduct(self, n: int) -> int:
        f = s = 0
        ans = 0
        while n:
            last = n % 10
            n = n // 10
            if last >= f:  # set first
                s = f
                f = last
            elif last > s:  # set second
                s = last
            ans = max(ans, s * f)

        return ans
