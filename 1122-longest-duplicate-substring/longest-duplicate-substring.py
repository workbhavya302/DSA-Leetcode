class Solution:
    def longestDupSubstring(self, s: str) -> str:
        nums=[ord(c)-ord('a') for c in s]
        n=len(s)
        
        base=26
        mod=2**63-1 
        
        def search(len:int)->int:
            """Returns the starting index of a duplicate substring of 'length', or -1."""
            if len==0:
                return -1
                
            base_pow=pow(base,len,mod)
            chash=0
            for i in range(len):
                chash=(chash*base+nums[i])%mod
                
            seen={chash}
            for start in range(1,n-len+1):
                chash=(chash*base-nums[start-1]*base_pow+nums[start+len-1])%mod
                
                if chash in seen:
                    return start
                seen.add(chash)
                
            return -1

        l,h=1,n-1
        start_idx,max_len=-1, 0
        
        while l<=h:
            mid=(l+h) // 2
            idx=search(mid)
            if idx!=-1:
                start_idx=idx
                max_len=mid
                l=mid+1 
            else:
                h=mid-1 
                
        return s[start_idx:start_idx+max_len] if start_idx!=-1 else ""
