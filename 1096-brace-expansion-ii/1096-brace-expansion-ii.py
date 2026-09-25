class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        stack = []
        res = []
        cur = [""]
        
        for char in expression:
            if char == '{':
                stack.append((res, cur))
                res = []
                cur = [""]
            elif char == '}':
                res.extend(cur)
                prev_res, prev_cur = stack.pop()
                # Cartesian product of the previous state and the evaluated block
                cur = [p + c for p in prev_cur for c in res]
                res = prev_res
            elif char == ',':
                res.extend(cur)
                cur = [""]
            else:
                # Concatenate character to all strings in the current group
                cur = [p + char for p in cur]
                
        res.extend(cur)
        # Remove duplicates and sort lexicographically
        return sorted(list(set(res)))