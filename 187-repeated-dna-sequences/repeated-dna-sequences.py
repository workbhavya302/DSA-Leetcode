class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        seen=set()
        repeated=set()
        for i in range(len(s)-9):
            ten_letter_seq=s[i:i+10]
            
            if ten_letter_seq in seen:
                repeated.add(ten_letter_seq)
            else:
                seen.add(ten_letter_seq)
                
        return list(repeated)
