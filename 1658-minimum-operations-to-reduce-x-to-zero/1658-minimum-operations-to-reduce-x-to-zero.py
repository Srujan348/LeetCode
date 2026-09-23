class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        
        # If target is exactly 0, we need all elements
        if target == 0:
            return len(nums)
            
        # If target is negative, no valid subarray can exist
        if target < 0:
            return -1
            
        left = 0
        current_sum = 0
        max_len = -1
        
        for right in range(len(nums)):
            current_sum += nums[right]
            
            # Shrink window if we overshoot the target
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1
                
            # If we hit the target exactly, see if it's the longest window
            if current_sum == target:
                max_len = max(max_len, right - left + 1)
                
        return len(nums) - max_len if max_len != -1 else -1