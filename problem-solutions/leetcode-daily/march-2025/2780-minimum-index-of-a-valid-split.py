from typing import List
from collections import defaultdict,Counter

"""
Notes
- Time Complexity: O(N)
- Space Complexity: O(N)
"""

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        f = Counter(nums)
        max_count = max(f.values())
        max_val = None
        for val,count in f.items():
            if count == max_count:
                max_val = val
                break
        n = len(nums)
        obs = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] == max_val:
                obs[max_val] += 1
            lmatch = obs[max_val]*2 > (i+1)
            rmatch = (f[max_val]-obs[max_val])*2 > (n-i-1)
            if lmatch and rmatch:
                return i
        return -1

