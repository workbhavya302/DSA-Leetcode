class Solution:
    def subarraySum(self,nums: list[int],k: int)->int:
        count,csum = 0,0
        prefix_map = {0:1}
        
        for num in nums:
            csum+=num
            
            if (csum-k) in prefix_map:
                count+=prefix_map[csum-k]
            prefix_map[csum]=prefix_map.get(csum,0)+1
            
        return count

        