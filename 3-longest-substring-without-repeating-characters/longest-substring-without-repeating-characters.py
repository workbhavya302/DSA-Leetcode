class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {} 
        left = 0
        maxlen = 0
        
        for right in range(len(s)):
            char = s[right]
            if char in seen and seen[char] >= left:
                left = seen[char] + 1
                
            seen[char] = right
            maxlen = max(maxlen, right - left + 1)
            
        return maxlen
        