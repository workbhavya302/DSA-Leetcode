class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:
        start,end=0,len(n)-1
        while start<end:
            total=n[start]+n[end]
            if total==target:
                return [start+1,end+1]
            elif total>target:
                end-=1
            else:
                start+=1
        
                

        