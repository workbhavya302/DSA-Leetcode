class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        # 1."Bulky" condition
        large_dimension = length >= 10000 or width >= 10000 or height >= 10000
        volume = length * width * height
        is_bulky = large_dimension or volume >= 10**9
        
        # 2."Heavy" condition
        is_heavy = mass >= 100
        
        # 3.routing rules
        if is_bulky and is_heavy:
            return "Both"
        if is_bulky:
            return "Bulky"
        if is_heavy:
            return "Heavy"
            
        return "Neither"
