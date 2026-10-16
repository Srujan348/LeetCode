class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        
        MOD = 10**9 + 7
        n = len(nums)
        
        # Segment tree arrays (1-indexed for child calculations)
        sum_sq = [0] * (4 * n + 1)
        sum_x = [0] * (4 * n + 1)
        lazy = [0] * (4 * n + 1)
        
        def apply(node: int, l: int, r: int, v: int):
            length = r - l + 1
            # (x+v)^2 = x^2 + 2vx + v^2
            sum_sq[node] = (sum_sq[node] + 2 * v * sum_x[node] + v * v * length) % MOD
            sum_x[node] = (sum_x[node] + v * length) % MOD
            lazy[node] = (lazy[node] + v) % MOD

        def push_down(node: int, l: int, r: int):
            if lazy[node] != 0:
                mid = (l + r) // 2
                apply(node * 2, l, mid, lazy[node])
                apply(node * 2 + 1, mid + 1, r, lazy[node])
                lazy[node] = 0

        def update(node: int, l: int, r: int, ql: int, qr: int, v: int):
            if ql <= l and r <= qr:
                apply(node, l, r, v)
                return
                
            push_down(node, l, r)
            mid = (l + r) // 2
            
            if ql <= mid:
                update(node * 2, l, mid, ql, qr, v)
            if qr > mid:
                update(node * 2 + 1, mid + 1, r, ql, qr, v)
                
            sum_sq[node] = (sum_sq[node * 2] + sum_sq[node * 2 + 1]) % MOD
            sum_x[node] = (sum_x[node * 2] + sum_x[node * 2 + 1]) % MOD

        last_seen = {}
        total_sum = 0
        
        for i, num in enumerate(nums):
            # The range to increment is from the index after the last occurrence up to i
            start = last_seen.get(num, -1) + 1
            
            # Add 1 to the distinct count for all subarrays in [start, i]
            update(1, 0, n - 1, start, i, 1)
            
            # The root node (1) now holds the sum of squares for all subarrays ending at i
            total_sum = (total_sum + sum_sq[1]) % MOD
            
            last_seen[num] = i
            
        return total_sum