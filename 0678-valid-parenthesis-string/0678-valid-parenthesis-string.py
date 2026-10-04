class Solution:
    def checkValidString(self, s: str) -> bool:
        cmin = 0 # minimum open brackets
        cmax = 0 # maximum open brackets
        
        for char in s:
            if char == '(':
                cmin += 1
                cmax += 1
            elif char == ')':
                cmin -= 1
                cmax -= 1
            elif char == '*':
                # * can be ), empty, or (
                cmin -= 1 
                cmax += 1
            
            # If even the maximum possible open brackets is negative, it's invalid
            if cmax < 0:
                return False
                
            # Minimum open brackets can't be negative
            cmin = max(cmin, 0)
            
        return cmin == 0