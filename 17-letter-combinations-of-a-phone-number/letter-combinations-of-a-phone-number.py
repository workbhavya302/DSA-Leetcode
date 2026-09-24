class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
            
        phone_map = {"2": "abc", 
        "3": "def", 
        "4": "ghi", 
        "5": "jkl",
        "6": "mno", 
        "7": "pqrs", 
        "8": "tuv", 
        "9": "wxyz"
        }
        result=[]
        
        def backtrack(index: int, cpath: list[str]):
            if index==len(digits):
                result.append("".join(cpath))
                return
                
            letters=phone_map[digits[index]]
            for letter in letters:
                cpath.append(letter)      
                backtrack(index+1,cpath) 
                cpath.pop()               
                
        backtrack(0,[])
        return result
