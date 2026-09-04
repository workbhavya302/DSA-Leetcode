class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        s_len,p_len=len(s),len(p)
        if s_len<p_len:
            return []
            
        p_count=[0]*26
        s_count=[0]*26
        result=[]
        
        for i in range(p_len):
            p_count[ord(p[i])-ord('a')] +=1
            s_count[ord(s[i])-ord('a')] +=1
        
        if s_count==p_count:
            result.append(0)
    
        for i in range(p_len,s_len):
            s_count[ord(s[i])-ord('a')]+=1
            s_count[ord(s[i - p_len])-ord('a')]-=1
            if s_count==p_count:
                result.append(i-p_len+1)
                
        return result
