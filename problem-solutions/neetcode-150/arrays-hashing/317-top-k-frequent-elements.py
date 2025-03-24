from typing import List
from collections import Counter
import heapq

"""
Notes:
- Time Complexity O(N)
- Space Complexity O(N)
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)

        h = [(-freq,-item) for item,freq in c.items()]
        heapq.heapify(h)

        ans = []
        while k > 0:
            freq,item = heapq.heappop(h)
            ans.append(-item)
            k -= 1
        return ans