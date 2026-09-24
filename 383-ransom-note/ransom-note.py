class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote)>len(magazine):
            return False
            
        charcounts={}
        for char in magazine:
            charcounts[char]=charcounts.get(char,0)+1
            
        for char in ransomNote:
            if char not in charcounts or charcounts[char]<=0:
                return False
            charcounts[char]-=1
            
        return True
