from typing import List
from collections import Counter

"""
Notes
- Time Complexity: O(N)
- Space Complexity: O(N)
"""

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        
        def can(segments):
            events = Counter()
            for start,end in segments:
                events[2*start] += 1
                events[2*end - 1] -= 1
            
            current = 0
            cuts = 0
            for t in sorted(events.keys()):
                if current > 0 and current + events[t] == 0:
                    cuts += 1
                current += events[t]
            return cuts >= 3

        xs = []
        ys = []
        for sx,sy,ex,ey in rectangles:
            xs.append((sx,ex))
            ys.append((sy,ey))
        return can(xs) or can(ys)

