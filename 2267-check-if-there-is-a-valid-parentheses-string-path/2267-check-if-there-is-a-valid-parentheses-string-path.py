from functools import cache

class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # A valid parentheses string must have an even length
        if (m + n - 1) % 2 != 0:
            return False
            
        # Must start with an open bracket and end with a closed bracket
        if grid[0][0] == ')' or grid[m-1][n-1] == '(':
            return False
            
        @cache
        def dfs(r: int, c: int, bal: int) -> bool:
            # Invalid path if balance goes negative
            if bal < 0:
                return False
                
            # If we reached the destination, the path is valid if balance is exactly 0
            if r == m - 1 and c == n - 1:
                return bal == 0
                
            # Try moving Right and Down
            for dr, dc in [(0, 1), (1, 0)]:
                nr, nc = r + dr, c + dc
                if nr < m and nc < n:
                    next_bal = bal + (1 if grid[nr][nc] == '(' else -1)
                    # If any path works, return True
                    if dfs(nr, nc, next_bal):
                        return True
                        
            return False
            
        return dfs(0, 0, 1)