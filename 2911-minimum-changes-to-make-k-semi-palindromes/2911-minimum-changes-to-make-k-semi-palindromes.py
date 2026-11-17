class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        
        # cost[i][j] holds the minimum edits to make s[i...j] a semi-palindrome
        cost = [[float('inf')] * n for _ in range(n)]
        
        # 1. Precompute costs for all possible substrings of length >= 2
        for length in range(2, n + 1):
            # Find all proper divisors of the current length
            divisors = [d for d in range(1, length) if length % d == 0]
            
            for i in range(n - length + 1):
                j = i + length - 1
                min_edits = float('inf')
                
                # Check the replacement cost for each valid divisor
                for d in divisors:
                    current_edits = 0
                    # There are 'd' independent sub-sequences to verify
                    for offset in range(d):
                        left = i + offset
                        # Mathematically pinpoint the right boundary for this offset
                        right = j - (d - 1 - offset) 
                        
                        # Count mismatches pushing towards the center of the subsequence
                        while left < right:
                            if s[left] != s[right]:
                                current_edits += 1
                            left += d
                            right -= d
                            
                    if current_edits < min_edits:
                        min_edits = current_edits
                        
                cost[i][j] = min_edits
                
        # dp[i][parts] = min cost to partition first i characters into 'parts' semi-palindromes
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        
        # 2. Dynamic Programming Partitioning
        for i in range(1, n + 1):
            for parts in range(1, k + 1):
                # j represents the start index of the last partition.
                # Since min length of a semi-palindrome is 2, j can go up to i - 2.
                for j in range(i - 1):
                    if dp[j][parts - 1] != float('inf') and cost[j][i - 1] != float('inf'):
                        dp[i][parts] = min(dp[i][parts], dp[j][parts - 1] + cost[j][i - 1])
                        
        return dp[n][k]