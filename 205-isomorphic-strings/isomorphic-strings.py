class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
            
        st={}
        ts={}
        
        for char_s,char_t in zip(s, t):
            if char_s in st and st[char_s]!=char_t:
                return False
            if char_t in ts and ts[char_t]!=char_s:
                return False
                
            st[char_s]=char_t
            ts[char_t]=char_s
            
        return True
