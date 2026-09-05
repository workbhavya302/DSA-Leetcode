class Solution:
    def countSubstrings(self, s: str) -> int:
        count=0
        
        def expand_around_center(left: int,right:int)->int:
            ans=0
            while left>=0 and right<len(s) and s[left]==s[right]:
                ans+=1
                left-=1
                right+=1
            return ans

        for i in range(len(s)):
            count+=expand_around_center(i,i)
            count+=expand_around_center(i,i+1)
            
        return count
