class Solution:
    def compress(self, chars: list[str]) -> int:
        write=0
        read=0
        n=len(chars)
        
        while read<n:
            c_char=chars[read]
            count=0
            while read<n and chars[read]==c_char:
                count+=1
                read+=1
            chars[write]=c_char
            write+=1
            if count>1:
                for digit in str(count):
                    chars[write]=digit
                    write+=1
                    
        return write
