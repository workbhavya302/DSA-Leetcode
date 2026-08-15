class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts={} 
        left,max_freq,max_len=0,0,0
        
        for right in range(len(s)):
            counts[s[right]]=counts.get(s[right], 0)+1
            max_freq = max(max_freq, counts[s[right]])
            if (right-left+1)-max_freq > k:
                counts[s[left]]-=1
                left+=1
            max_len=max(max_len,right-left+1)
            
        return max_len

        