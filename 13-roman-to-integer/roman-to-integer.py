class Solution:
    def romanToInt(self, s: str) -> int:
        map={
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total=0
        n=len(s)
        
        for i in range(n):
            if i+1<n and map[s[i]]<map[s[i+1]]:
                total-=map[s[i]]
            else:
                total+=map[s[i]]
                
        return total
