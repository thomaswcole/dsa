from typing import List
from collections import defaultdict

"""
Notes
- Time Complexity: O(N)
- Space Complexity: O(N)


Since were grouping anagrams, we can just sort the strings and
store them that way.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            s = ''.join(sorted(word))
            groups[s].append(word)
        
        res = []        
        for group in groups.values():
            res.append(group)
        return res