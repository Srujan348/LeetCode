class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        
        # Check if already sorted
        if all(s[i] <= s[i+1] for i in range(n - 1)):
            return 0
            
        # Unsorted strings of length 2 are impossible
        if n == 2:
            return -1
            
        # Find the FIRST occurrence of the absolute minimum character
        min_c = s.find(min(s))
        
        # Find the LAST occurrence of the absolute maximum character
        max_c = s.rfind(max(s))
        
        # If either extreme is already in its final correct place
        if min_c == 0 or max_c == n - 1:
            return 1
            
        # If the extremes are perfectly inverted
        if min_c == n - 1 and max_c == 0:
            return 3
            
        # All other cases can be resolved in exactly 2 moves
        return 2