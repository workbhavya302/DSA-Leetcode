class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        minlen=float('inf')
        csum=0
        l=0
        
        for r in range(len(nums)):
            csum += nums[r]
            
            while csum>=target:
                minlen=min(minlen,r-l+1)
                csum-=nums[l]
                l+=1
                
        return minlen if minlen!= float('inf') else 0

        