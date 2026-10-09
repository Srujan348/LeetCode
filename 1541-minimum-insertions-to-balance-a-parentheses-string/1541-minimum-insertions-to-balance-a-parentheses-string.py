class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        needed_right = 0
        
        for char in s:
            if char == '(':
                # If we have an odd number of needed_right, we are missing one ')'
                # for a previous '('. We must insert it before opening this new '('.
                if needed_right % 2 != 0:
                    insertions += 1
                    needed_right -= 1
                needed_right += 2
            else:
                needed_right -= 1
                # If we have too many ')', we need to insert a '('
                if needed_right < 0:
                    insertions += 1
                    # We inserted a '(', which needs two ')'. We just used one, so net +2
                    needed_right += 2
                    
        return insertions + needed_right