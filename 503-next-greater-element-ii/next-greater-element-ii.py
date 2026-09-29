class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n=len(nums)
        result=[-1]*n
        stack=[]  
        
        for i in range(2*n):
            current_num=nums[i%n]
            while stack and nums[stack[-1]]<current_num:
                prev_idx=stack.pop()
                result[prev_idx]=current_num
           
            if i<n:
                stack.append(i)
                
        return result
