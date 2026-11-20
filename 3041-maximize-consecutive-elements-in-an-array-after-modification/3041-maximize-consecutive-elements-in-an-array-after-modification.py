from collections import defaultdict

class Solution:
    def maxSelectedElements(self, nums: list[int]) -> int:
        nums.sort()
        dp = defaultdict(int)
        
        for x in nums:
            # Update x + 1 first so we don't reuse the current element x twice
            dp[x + 1] = dp[x] + 1
            dp[x] = dp[x - 1] + 1
            
        return max(dp.values())