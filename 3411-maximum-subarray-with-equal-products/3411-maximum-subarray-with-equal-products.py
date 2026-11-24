import math

class Solution:
    def maxLength(self, nums: list[int]) -> int:
        # Any subarray of length 2 is always valid
        max_len = 2
        window_prod = 1
        left = 0
        
        for right, x in enumerate(nums):
            # Shrink the window until x is coprime with all remaining elements
            while math.gcd(window_prod, x) > 1:
                window_prod //= nums[left]
                left += 1
                
            window_prod *= x
            max_len = max(max_len, right - left + 1)
            
        return max_len