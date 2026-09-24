class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        for i, num in enumerate(nums):
            # Calculate digit sum using modulo arithmetic
            dsum = 0     
            temp = num
            while temp > 0:
                dsum += temp % 10
                temp //= 10
                # STEP TO CHECK THE SUM
            # Check if the digit sum equals the current index
            if dsum == i:
                return i
                
        return -1