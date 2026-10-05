class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        n = len(heights)
        result = [0] * n
        stack = []  
        
        for i in range(n - 1, -1, -1):
            visible_count = 0
            while stack and heights[i] > stack[-1]:
                stack.pop()
                visible_count += 1
            if stack:
                visible_count += 1
                
            result[i] = visible_count
            stack.append(heights[i])
            
        return result
