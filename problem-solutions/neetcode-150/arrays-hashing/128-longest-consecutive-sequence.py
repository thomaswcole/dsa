from typing import List

"""
Note
- Time Complexity: O(N)
- Space Comlexity: O(N)
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)

        for n in num_set:
            if (n-1) not in num_set:
                length = 0
                while (n+length) in num_set:
                    length += 1
                longest = max(longest,length)
        return longest