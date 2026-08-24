from bisect import bisect_left
from bisect import insort

class Solution:
    def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        if not matrix or not matrix[0]:
            return 0
            
        rows, cols = len(matrix), len(matrix[0])
        max_sum = float('-inf')
        
        for left in range(cols):
            row_sums = [0] * rows
            for right in range(left, cols):
                for r in range(rows):
                    row_sums[r] += matrix[r][right]
                seen_prefixes = [0]  
                curr_prefix = 0
                
                for val in row_sums:
                    curr_prefix += val
                    target = curr_prefix - k
                    idx = bisect_left(seen_prefixes, target)
                    if idx < len(seen_prefixes):
                        max_sum = max(max_sum, curr_prefix - seen_prefixes[idx])
                    
                    insort(seen_prefixes, curr_prefix)
                    
        return max_sum
