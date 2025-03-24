from typing import List
from collections import Counter

"""
Notes
- Time Complexity: O(N)
- Space Complexity: O(N)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        fs = Counter(s)
        ft = Counter(t)
        for char in fs.keys():
            if char not in ft or ft[char] != fs[char]:
                return False

        for char in ft.keys():
            if char not in fs or ft[char] != fs[char]:
                return False
        return True