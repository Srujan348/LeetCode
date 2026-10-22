class Solution:
    def minOperations(self, nums: List[int]) -> int:
    
        n = len(nums)
        zero = nums.index(0)
        
        # Check if the array is cyclically increasing
        is_inc = True
        for i in range(1, n):
            if nums[(zero + i) % n] != i:
                is_inc = False
                break
                
        # Check if the array is cyclically decreasing
        is_dec = True
        for i in range(1, n):
            if nums[(zero + i) % n] != n - i:
                is_dec = False
                break
                
        ans = float('inf')
        
        if is_inc:
            ans = min(ans, zero, n - zero + 2)
            
        if is_dec:
            ans = min(ans, n - zero, zero + 2)
            
        return ans if ans != float('inf') else -1