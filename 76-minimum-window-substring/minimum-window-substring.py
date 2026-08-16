from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        dict_t = Counter(t)
        required = len(dict_t)
        l, r,formed = 0, 0,0
        counts = {}
        ans = float("inf"), None, None
        
        while r< len(s):
            char= s[r]
            counts[char]=counts.get(char, 0) + 1
            if char in dict_t and counts[char] == dict_t[char]:
                formed += 1
        
            while l<=r and formed==required:
                char=s[l]
                if r-l+1 < ans[0]:
                    ans = (r-l+1,l,r)
                counts[char] -= 1
                if char in dict_t and counts[char] < dict_t[char]:
                    formed -= 1
                l+=1    
            r+=1
            
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]

        