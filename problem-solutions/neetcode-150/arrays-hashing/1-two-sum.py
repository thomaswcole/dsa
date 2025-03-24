from typing import List

"""
Notes
- Time Complexity: O(N)
- Space Complexity: O(N)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff],i]
            else:
                seen[nums[i]] = i
        