class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # Convert list of pairs into a dictionary for O(1) lookups
        lookup = {k: v for k, v in knowledge}
        
        res = []
        cur_key = []
        in_bracket = False
        
        for char in s:
            if char == '(':
                in_bracket = True
            elif char == ')':
                # Build the key and look it up
                key = "".join(cur_key)
                res.append(lookup.get(key, "?"))
                
                # Reset for the next potential bracket pair
                cur_key = []
                in_bracket = False
            elif in_bracket:
                cur_key.append(char)
            else:
                res.append(char)
                
        return "".join(res)