class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_brackets = 0
        additions_needed = 0
        
        for char in s:
            if char == '(':
                open_brackets += 1
            elif open_brackets > 0:
                # We have a matching open bracket to pair this with
                open_brackets -= 1
            else:
                # Unmatched closing bracket, we must add an open bracket
                additions_needed += 1
                
        # Return unmatched closing brackets + unmatched opening brackets
        return open_brackets + additions_needed