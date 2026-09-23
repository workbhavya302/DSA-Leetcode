class Solution:
    def firstUniqChar(self, s: str) -> int:
        frequency={}
        for char in s:
            frequency[char]=frequency.get(char,0)+1
        for index,char in enumerate(s):
            if frequency[char]==1:
                return index
                
        return -1
