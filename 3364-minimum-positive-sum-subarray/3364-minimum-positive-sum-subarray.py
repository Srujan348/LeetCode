class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        n = len(nums)
        min_sum = float('inf')
        
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                length = j - i + 1
                
                # Check if the current window meets all conditions
                if l <= length <= r and current_sum > 0:
                    min_sum = min(min_sum, current_sum)
                    
                # Stop expanding if the subarray exceeds the maximum allowed length
                if length >= r:
                    break
                    
        return min_sum if min_sum != float('inf') else -1