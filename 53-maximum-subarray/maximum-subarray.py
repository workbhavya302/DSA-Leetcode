class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = nums[0]
        csum = nums[0]
        
        for num in nums[1:]:
            csum = max(num,csum + num)
            max_sum = max(max_sum,csum)
            
        return max_sum
