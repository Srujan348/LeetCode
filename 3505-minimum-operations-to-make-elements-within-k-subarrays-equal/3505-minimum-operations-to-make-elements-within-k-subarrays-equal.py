class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)
        unique_vals = sorted(list(set(nums)))
        max_rank = len(unique_vals)
        rank = {v: i + 1 for i, v in enumerate(unique_vals)}
        
        # Fenwick Trees for frequency and sum
        tree_count = [0] * (max_rank + 1)
        tree_sum = [0] * (max_rank + 1)
        
        def add(i: int, count_delta: int, sum_delta: int):
            while i <= max_rank:
                tree_count[i] += count_delta
                tree_sum[i] += sum_delta
                i += i & (-i)
                
        def query_count(i: int) -> int:
            s = 0
            while i > 0:
                s += tree_count[i]
                i -= i & (-i)
            return s
            
        def query_sum(i: int) -> int:
            s = 0
            while i > 0:
                s += tree_sum[i]
                i -= i & (-i)
            return s
            
        def find_kth(target_k: int) -> int:
            idx = 0
            # Binary lifting to find the k-th smallest element
            for i in range(19, -1, -1):
                next_idx = idx + (1 << i)
                if next_idx <= max_rank and tree_count[next_idx] < target_k:
                    idx = next_idx
                    target_k -= tree_count[next_idx]
            return idx + 1
            
        C = []
        current_sum = 0
        sz_low = (x + 1) // 2
        sz_high = x - sz_low
        
        for i in range(n):
            val = nums[i]
            r = rank[val]
            add(r, 1, val)
            current_sum += val
            
            # Remove element falling out of the window
            if i >= x:
                out_val = nums[i - x]
                out_r = rank[out_val]
                add(out_r, -1, -out_val)
                current_sum -= out_val
                
            # Once window is full, calculate its minimum flattening cost
            if i >= x - 1:
                med_rank = find_kth(sz_low)
                med_val = unique_vals[med_rank - 1]
                
                clt = query_count(med_rank - 1)
                slt = query_sum(med_rank - 1)
                
                low_sum = slt + (sz_low - clt) * med_val
                high_sum = current_sum - low_sum
                
                cost = high_sum - low_sum + med_val * (sz_low - sz_high)
                C.append(cost)
                
        # Space-optimized DP: dp[i] holds min cost to pick j subarrays up to index i
        dp = [0] * (n + 1)
        
        for j in range(1, k + 1):
            next_dp = [float('inf')] * (n + 1)
            for i in range(j * x, n + 1):
                next_dp[i] = min(next_dp[i - 1], dp[i - x] + C[i - x])
            dp = next_dp
            
        return dp[n]