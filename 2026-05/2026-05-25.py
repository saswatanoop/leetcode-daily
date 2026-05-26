# https://leetcode.com/problems/jump-game-vii/submissions/2012935135/?envType=daily-question&envId=2026-05-25

'''
=== PATTERN: DP + Prefix Sum (Sliding Window Optimization) ===

STANDARD DP APPROACH:
- Inner for loop iterates through all previous states: O(N^2) time complexity
- Recalculates sums for overlapping ranges repeatedly (wasteful)

PREFIX SUM OPTIMIZATION:
- Maintain running cumulative sum of valid states in O(1) space
- Query any range [left, right] with single subtraction: prefix_sum[right] - prefix_sum[left-1]
- Replaces inner loop with O(1) calculation: (valid_in_range - expired)
- Result: O(N) time complexity with O(N) space

KEY INSIGHT: Trade space (prefix array) for time (eliminate inner loop)
'''

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        
        # reachable[i] = True if we can successfully land on index i
        reachable = [False] * n
        
        # prefix_sum[i] = cumulative count of reachable indices from 0 to i
        prefix_sum = [0] * n
        prefix_sum[0] = 1  # Base case: index 0 is always reachable (starting point)

        for i in range(1, n):
            # Current index must be '0' (safe) and reachable with minJump constraint
            if s[i] == '0' and i - minJump >= 0:
                
                # Count reachable indices within [i-maxJump, i-minJump] window
                valid_in_range = prefix_sum[i - minJump]
                
                # Subtract indices beyond maxJump (too far to jump from)
                expired = 0
                if i - maxJump - 1 >= 0:
                    expired = prefix_sum[i - maxJump - 1]
                    
                # Can reach index i if valid window contains at least one reachable index
                reachable[i] = (valid_in_range - expired) >= 1
            
            # Update the prefix sum array for the next iteration
            prefix_sum[i] = prefix_sum[i - 1] + (1 if reachable[i] else 0)
            
        return reachable[-1]
    

