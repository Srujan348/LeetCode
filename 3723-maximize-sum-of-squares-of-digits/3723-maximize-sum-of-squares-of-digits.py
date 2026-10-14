class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:

        if sum > 9 * num:
            return ""
            
        nines = sum // 9
        rem = sum % 9
        
        # If there is a remainder, it occupies exactly one digit
        rem_str = str(rem) if rem > 0 else ""
        
        # The rest of the digits must be padded with zeros
        zeros = num - nines - (1 if rem > 0 else 0)
        
        return "9" * nines + rem_str + "0" * zeros