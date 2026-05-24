
# https://leetcode.com/problems/jump-game-v/?envType=daily-question&envId=2026-05-24

from typing import List

class Solution:
    # DP: top down with memoization T:O(n*d) and S:O(n) where n is number of buildings and d is max jump distance
    def maxJumps(self, arr: List[int], d: int) -> int:
    
        def get_max_visits(curr_index):
            if memo[curr_index] != -1:
                return memo[curr_index]

            max_visits = 1 # current index building is also counted as visit
            
            # jump right
            for jump_distance in range(1, d + 1):
                next_index = curr_index + jump_distance
                # Break immediately if out of bounds OR if the building is too tall
                if next_index >= num_buildings or arr[next_index] >= arr[curr_index]:
                    break
                max_visits = max(max_visits, 1 + get_max_visits(next_index))    

            # jump left
            for jump_distance in range(1, d + 1):
                next_index = curr_index - jump_distance
                # Break immediately if out of bounds OR if the building is too tall
                if next_index < 0 or arr[next_index] >= arr[curr_index]:
                    break
                max_visits = max(max_visits, 1 + get_max_visits(next_index))
            
            memo[curr_index] = max_visits
            return max_visits

        num_buildings = len(arr)
        memo = [-1] * num_buildings
        overall_max_visits = 0
        
        for start_index in range(num_buildings):
            overall_max_visits = max(overall_max_visits, get_max_visits(start_index))
            
        return overall_max_visits