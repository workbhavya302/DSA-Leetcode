class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        dup=[]
        
        for num in nums:
            idx=abs(num)-1
            if nums[idx]<0:
                dup.append(abs(num))
            else:
                nums[idx]=-nums[idx]
                
        return dup
