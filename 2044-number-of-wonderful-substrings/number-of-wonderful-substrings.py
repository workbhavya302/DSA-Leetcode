class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count=[0]*1024
        count[0]=1 
        ans=0
        prefix=0
        
        for char in word:
            prefix^=1<<(ord(char)-ord('a'))
            ans+=count[prefix]
            for i in range(10):
                ans += count[prefix^(1<<i)]
            count[prefix]+=1
            
        return ans
