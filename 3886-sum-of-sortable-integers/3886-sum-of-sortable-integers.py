class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
 
        n = len(nums)
        
        # 1. Precompute Prefix Maximums
        prefMax = [0] * n
        prefMax[0] = nums[0]
        for i in range(1, n):
            prefMax[i] = max(prefMax[i-1], nums[i])
            
        # 2. Precompute Suffix Minimums
        suffMin = [0] * n
        suffMin[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            suffMin[i] = min(suffMin[i+1], nums[i])
            
        # 3. Precompute Internal Drops Prefix Sum
        prefDrop = [0] * n
        for i in range(1, n):
            prefDrop[i] = prefDrop[i-1] + (1 if nums[i-1] > nums[i] else 0)
            
        total_sum = 0
        
        for k in range(1, n + 1):
            # Must be a divisor
            if n % k != 0:
                continue
                
            is_valid = True
            
            # Check 1: Block Boundaries
            for i in range(1, n // k):
                p = i * k
                if prefMax[p-1] > suffMin[p]:
                    is_valid = False
                    break
                    
            if not is_valid:
                continue
                
            # Check 2: Cyclic Sortability for each Block
            for i in range(n // k):
                L = i * k
                R = L + k - 1
                
                internal_drops = prefDrop[R] - prefDrop[L]
                wrap_drop = 1 if nums[R] > nums[L] else 0
                
                if internal_drops + wrap_drop > 1:
                    is_valid = False
                    break
                    
            if is_valid:
                total_sum += k
                
        return total_sum