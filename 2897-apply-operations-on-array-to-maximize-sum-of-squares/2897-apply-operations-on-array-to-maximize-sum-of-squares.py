class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        bit_counts = [0] * 32
        
        # Step 1: Count the total number of set bits at each position
        for num in nums:
            for i in range(32):
                if (num >> i) & 1:
                    bit_counts[i] += 1
                    
        total_sum = 0
        
        # Step 2 & 3: Greedily construct the k largest possible numbers
        for _ in range(k):
            current_num = 0
            for i in range(32):
                if bit_counts[i] > 0:
                    # Set the ith bit
                    current_num |= (1 << i)
                    bit_counts[i] -= 1
            
            # Square the number and add to total, modulo 10^9 + 7
            total_sum = (total_sum + current_num * current_num) % MOD
            
        return total_sum