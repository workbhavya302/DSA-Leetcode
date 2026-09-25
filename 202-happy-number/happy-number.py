class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(number:int)->int:
            sum=0
            while number>0:
                digit=number % 10
                sum+=digit*digit
                number//=10
            return sum

        slow=n
        fast=get_next(n)        
        while fast!=1 and slow!=fast:
            slow=get_next(slow)            
            fast=get_next(get_next(fast))   
        return fast == 1
