class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
 
        if not grid or not grid[0]:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        
        # Helper function to sink an island
        def sink(r: int, c: int):
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 0:
                grid[r][c] = 1  # Sink it
                sink(r + 1, c)
                sink(r - 1, c)
                sink(r, c + 1)
                sink(r, c - 1)
                
        # Step 1: Sink all islands connected to the perimeter
        for r in range(rows):
            if grid[r][0] == 0: sink(r, 0)
            if grid[r][cols - 1] == 0: sink(r, cols - 1)
            
        for c in range(cols):
            if grid[0][c] == 0: sink(0, c)
            if grid[rows - 1][c] == 0: sink(rows - 1, c)
            
        # Step 2: Count and sink the remaining closed interior islands
        closed_islands = 0
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if grid[r][c] == 0:
                    closed_islands += 1
                    sink(r, c)
                    
        return closed_islands