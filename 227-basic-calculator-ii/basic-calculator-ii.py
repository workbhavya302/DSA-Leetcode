class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
            
        running_sum = 0
        last_num = 0
        current_num = 0
        operator = '+'
        for i, char in enumerate(s):
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            if char in "+-*/" or i == len(s) - 1:
                if operator == '+':
                    running_sum += last_num
                    last_num = current_num
                elif operator == '-':
                    running_sum += last_num
                    last_num = -current_num
                elif operator == '*':
                    last_num = last_num * current_num
                elif operator == '/':
                    last_num = int(last_num / current_num)
                    
                operator = char
                current_num = 0
                
        running_sum += last_num
        return running_sum
