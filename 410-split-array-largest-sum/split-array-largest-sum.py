class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        l=max(nums)
        r=sum(nums)
        
        while l<r:
            mid=l+(r-l)//2
            csum=0
            needed=1
            
            for num in nums:
                if csum+num>mid:
                    needed+=1
                    csum=0
                csum+=num
            if needed<=k:
                r=mid
            else:
                l=mid+1
                
        return l
