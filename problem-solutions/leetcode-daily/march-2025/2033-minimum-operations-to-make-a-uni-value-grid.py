from typing import List

"""
Notes
Time Complexity: O(N*M)
Space Complexity: O(N*M)

"""
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = []
        residual = set()
        R = len(grid)
        C = len(grid[0])
        for r in range(R):
            for c in range(C):
                residual.add(grid[r][c] % x)
                arr.append(grid[r][c])
                if len(residual) > 1:
                    return -1

        arr.sort()
        mid = arr[len(arr) // 2]
        res = 0
        for num in arr:
            res += abs(num - mid) // x
        return res