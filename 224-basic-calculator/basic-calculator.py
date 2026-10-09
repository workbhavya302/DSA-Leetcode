class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        running_sum = 0
        sign = 1  
        n = len(s)
        i = 0
        
        while i < n:
            char = s[i]
            
            if char.isdigit():
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                running_sum += sign * num
                continue  
                
            elif char == '+':
                sign = 1
            elif char == '-':
                sign = -1
            elif char == '(':
                stack.append(running_sum)
                stack.append(sign)
                running_sum = 0
                sign = 1
            elif char == ')':
                prev_sign = stack.pop()
                prev_sum = stack.pop()
                running_sum = prev_sum + prev_sign * running_sum
                
            i += 1
            
        return running_sum
