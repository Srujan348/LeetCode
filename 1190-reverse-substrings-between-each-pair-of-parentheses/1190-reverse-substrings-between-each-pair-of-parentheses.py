class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        pair = [0] * n
        stack = []
        
        # Step 1: Map matching parentheses
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                j = stack.pop()
                # Link both brackets to each other
                pair[i] = j
                pair[j] = i
                
        # Step 2: Traverse using teleportation
        res = []
        i = 0
        direction = 1
        
        while i < n:
            if s[i] == '(' or s[i] == ')':
                # Teleport to the matching bracket and reverse direction
                i = pair[i]
                direction = -direction
            else:
                # Add character and keep moving
                res.append(s[i])
            i += direction
            
        return "".join(res)