class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
 
        m, n = len(grid), len(grid[0])
        
        # dp[j] holds a set of all reachable XOR values for column j
        dp = [set() for _ in range(n)]
        dp[0].add(grid[0][0])
        
        # Pre-fill the first row (can only come from the left)
        for j in range(1, n):
            for val in dp[j - 1]:
                dp[j].add(val ^ grid[0][j])
                
        # Process the remaining rows
        for i in range(1, m):
            next_dp = [set() for _ in range(n)]
            
            # The first column can only come from directly above
            for val in dp[0]:
                next_dp[0].add(val ^ grid[i][0])
                
            # For the rest of the row, union the possibilities from above and left
            for j in range(1, n):
                current_val = grid[i][j]
                for val in next_dp[j - 1]:
                    next_dp[j].add(val ^ current_val)
                for val in dp[j]:
                    next_dp[j].add(val ^ current_val)
                    
            dp = next_dp
            
        return min(dp[-1])