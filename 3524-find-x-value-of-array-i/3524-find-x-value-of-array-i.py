class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        # dp[r] stores the number of subarrays ending at the current position with product % k == r
        dp = [0] * k
        
        for num in nums:
            new_dp = [0] * k
            num_mod = num % k
            
            # 1. Start a new subarray with just the current element
            new_dp[num_mod] = 1
            
            # 2. Extend all previous subarrays
            for i in range(k):
                if dp[i] > 0:
                    new_mod = (i * num_mod) % k
                    new_dp[new_mod] += dp[i]
                    
            # 3. Accumulate counts into the final answer array
            for i in range(k):
                ans[i] += new_dp[i]
                
            # Move to the next element
            dp = new_dp
            
        return ans